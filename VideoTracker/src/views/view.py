import tkinter as tk
import PIL.Image, PIL.ImageTk
import platform
from tkinter import messagebox


class View:
    def __init__(self):
        print("View.py: View created")
        try:
            self.fenetre = tk.Tk()
            self.fenetre.configure(bg="black")
            self.fenetre.withdraw
            self.fenetre.title("Video Tracker")
            if platform.system() == "Windows":
                self.fenetre.attributes("-fullscreen", True)
            elif platform.system() == "Linux":
                self.fenetre.attributes("-zoomed", True)
        except Exception as e:
            print("View.py: ERROR detected on init: [", e, "]")
            return None

    def open_window(self):
        print("View.py: open_window called")
        try:
            self.fenetre.mainloop()
        except Exception as e:
            print("View.py: ERROR detected on opening window: [", e, "]")
            return None

    def setController(self, controller):
        print("View.py: Controller set")
        self.controller = controller

    def create_interface(self):
        print("View.py: create_button_echelle called")
        menuBar = tk.Menu(self.fenetre)
        self.fenetre.config(menu=menuBar)
        menuFile = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Files", menu=menuFile)
        menuFile.add_command(
            label="Load the video",
            underline=1,
            command=lambda: self.load_video(),
        )
        self.fenetre.bind_all("<Control-Key-o>", lambda o: self.load_video())
        Point1 = self.controller.point(0, 2)
        Point2 = self.controller.point(1.2, 4)
        Point3 = self.controller.point(1111, -4)
        dataTimes = [0, 1, 2]
        dataPoints = [Point1, Point2, Point3]
        menuFile.add_command(
            label="Save as",
            underline=1,
            command=lambda: self.controller.filerepo.saveAs(
                self.controller.filerepo,
                dataTimes,
                dataPoints,
            ),
        )
        self.fenetre.bind_all(
            "<Control-Key-a>",
            lambda a: self.controller.filerepo.saveAs(
                self.controller.filerepo,
                dataTimes,
                dataPoints,
            ),
        )
        menuFile.add_command(
            label="Save",
            underline=0,
            command=lambda: self.controller.filerepo.save(
                self.controller.filerepo,
                dataTimes,
                dataPoints,
            ),
        )
        self.fenetre.bind_all(
            "<Control-Key-s>",
            lambda s: self.controller.filerepo.save(
                self.controller.filerepo,
                dataTimes,
                dataPoints,
            ),
        )
        menuFile.add_separator()
        menuFile.add_command(
            label="Quit the app",
            underline=0,
            command=lambda: self.controller.video.quit(self.fenetre),
        )
        self.fenetre.bind_all(
            "<Control-Key-q>", lambda q: self.controller.video.quit(self.fenetre)
        )
        menuTools = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Tools", menu=menuTools)
        menuTools.add_command(
            label="Go to frame...",
            underline=0,
            command=lambda: self.goToFrameWindow(),
        )
        self.fenetre.bind_all("<Return>", lambda g: self.goToFrameWindow())
        self.fenetre.bind_all("<Control-Key-g>", lambda g: self.goToFrameWindow())
        menuTools.add_command(
            label="Plot graph",
            underline=0,
            command=lambda: self.controller.graph.windowGraph(self.controller.graph),
        )
        menuHelp = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=menuHelp)
        menuHelp.add_command(
            label="Instruction manual",
            underline=1,
            command=lambda: self.goToFrameHelp(),
        )
        self.fenetre.bind_all("<Control-Key-h>", lambda h: self.goToFrameHelp())

        buttonsFrame = tk.Frame(self.fenetre, bg="#BB620D")
        buttonsFrame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Button(
            buttonsFrame,
            text="Set up scale",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            font=(
                "calibri",
                20,
            ),
        ).pack(side=tk.RIGHT, padx=20, pady=7)
        tk.Button(
            buttonsFrame,
            text="Start from the beginning",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            font=("calibri", 18),
            command=lambda: self.controller.video.firstFrame(button),
        ).pack(side=tk.LEFT, padx=30, pady=7)
        self.fenetre.bind_all(
            "<Control-Key-b>", lambda b: self.controller.video.firstFrame(button)
        )
        tk.Button(
            buttonsFrame,
            text="|<",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            width=10,
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.previousFrame(button),
        ).pack(side=tk.LEFT, padx=30, pady=7, fill="none", expand=True)
        self.fenetre.bind_all("<Left>", lambda l: self.controller.video.previousFrame(button))
        button = tk.Button(
            buttonsFrame,
            text=">",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            width=15,
            font=("calibri", 25, "bold"),
        )
        button.config(
            command=lambda: self.controller.video.play_or_pause(button),
        )
        self.fenetre.bind_all(
            "<space>", lambda s: self.controller.video.play_or_pause(button)
        )
        button.pack(side=tk.LEFT, padx=10, pady=7)
        tk.Button(
            buttonsFrame,
            text=">|",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            width=10,
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.nextFrame(button),
        ).pack(side=tk.LEFT, padx=30, pady=7, fill="none", expand=True)
        self.fenetre.bind_all("<Right>", lambda r: self.controller.video.nextFrame(button))

    def get_window(self):
        print("View.py: get_window called")
        try:
            return self.fenetre
        except Exception as e:
            print("View.py: ERROR detected on getting window: [", e, "]")
            return None

    def load_video(self):
        print("View.py: open_file called")
        self.controller.video.open_file()

    def window_pos(self, window, w_width, w_height):
        s_width = window.winfo_screenwidth()
        s_height = window.winfo_screenheight()
        self.center_x = int(s_width / 2 - w_width / 2)
        self.center_y = int(s_height / 2 - w_height / 2)
        pos = f"{w_width}x{w_height}+{self.center_x}+{self.center_y}"
        return pos

    def goToFrameWindow(self):
        try:
            if self.controller.video.videoOpened() == True:
                F_Window = tk.Tk()
                F_Window.configure(background="#ADDAEF")
                F_Window.title("Choose when to go")
                w_width = 450
                w_height = 150
                F_Window.geometry(self.window_pos(F_Window, w_width, w_height))
                F_Window.resizable(False, False)

                tk.Label(F_Window, text="Enter the frame you want to go").pack(
                    side=tk.TOP, pady=7
                )
                entry = tk.Entry(F_Window)
                entry.pack(side=tk.TOP, pady=7)
                entry.focus()
                tk.Label(F_Window, text=self.controller.video.currentFrame()).pack(
                    side=tk.LEFT, padx=10
                )
                tk.Button(
                    F_Window,
                    text="OK",
                    width=20,
                    height=2,
                    background="#9DCDE3",
                    activebackground="#ADDAEF",
                    font=("calibri", 20, "bold"),
                    command=lambda: self.controller.video.chooseValue(entry, F_Window),
                ).pack(side=tk.BOTTOM, padx=30, pady=7)
                F_Window.bind_all(
                    "<Return>",
                    lambda g: self.controller.video.chooseValue(entry, F_Window),
                )
        except:
            messagebox.showerror(
                "Error - Go to frame", "You haven't opened a video yet."
            )

    def goToFrameHelp(self):
        H_Window = tk.Tk()
        H_Window.configure(background="#ADDAEF")
        H_Window.title("Instruction manual")
        w_width = int(H_Window.winfo_screenwidth() / float(2.2))
        w_height = int(H_Window.winfo_screenheight() / float(2))
        H_Window.geometry(self.window_pos(H_Window, w_width, w_height))
        H_Window.resizable(False, False)
        tk.Button(
            H_Window,
            text="OK",
            width=20,
            height=2,
            background="#9DCDE3",
            activebackground="#ADDAEF",
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.close(H_Window),
        ).pack(side=tk.BOTTOM, padx=30, pady=7)
