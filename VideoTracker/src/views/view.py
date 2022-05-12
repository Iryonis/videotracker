from cProfile import label
import tkinter as tk
import platform
from tkinter import BOTTOM, TOP, Label, messagebox
import tkinter
from tkinter.tix import TEXT
from typing import Text


class View:
    def __init__(self):
        print("View.py: View created")
        try:
            self.fenetre = tk.Tk()
            self.fenetre.configure(bg="black")
            self.fenetre.withdraw
            self.fenetre.title("Video Tracker - V0.1.0")
            if platform.system() == "Windows":
                self.fenetre.attributes("-fullscreen", True)
            elif platform.system() == "Linux":
                self.fenetre.attributes("-zoomed", True)
        except Exception as e:
            print("View.py: ERROR detected on init: [", e, "]")

    def open_window(self):
        print("View.py: open_window called")
        try:
            self.fenetre.mainloop()
        except Exception as e:
            print("View.py: ERROR detected on open_window(): [", e, "]")

    def setController(self, controller):
        print("View.py: Controller set")
        self.controller = controller

    def create_interface(self):
        print("View.py: create_interface called")
        menuBar = tk.Menu(self.fenetre)
        self.fenetre.config(menu=menuBar)
        menuFile = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Files", menu=menuFile)
        menuFile.add_command(
            label="Open the video",
            underline=0,
            accelerator="(Ctrl + O)",
            command=lambda: self.load_video(),
        )
        self.fenetre.bind_all("<Control-Key-o>", lambda o: self.load_video())
        Point1 = self.controller.point(0, 4)
        Point2 = self.controller.point(1.5, 5)
        Point3 = self.controller.point(111, -6)
        dataTimes = [0, 1, 2]
        dataPoints = [Point1, Point2, Point3]
        menuFile.add_command(
            label="Save as",
            underline=1,
            accelerator="(Ctrl + A)",
            command=lambda: self.controller.filerepo.saveAs(
                dataTimes,
                dataPoints,
            ),
        )
        self.fenetre.bind_all(
            "<Control-Key-a>",
            lambda a: self.controller.filerepo.saveAs(
                dataTimes,
                dataPoints,
            ),
        )
        menuFile.add_command(
            label="Save",
            underline=0,
            accelerator="(Ctrl + S)",
            command=lambda: self.controller.filerepo.save(
                dataTimes,
                dataPoints,
            ),
        )
        self.fenetre.bind_all(
            "<Control-Key-s>",
            lambda s: self.controller.filerepo.save(
                dataTimes,
                dataPoints,
            ),
        )
        menuFile.add_separator()
        menuFile.add_command(
            label="Quit the app",
            underline=0,
            accelerator="(Ctrl + Q)",
            command=lambda: self.controller.video.quit(),
        )
        self.fenetre.bind_all("<Control-Key-q>", lambda q: self.controller.video.quit())
        menuEdit = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit", menu=menuEdit)
        menuEdit.add_command(
            label="Show values...",
            underline=5,
            accelerator="(Ctrl + V)",
            state=tk.DISABLED,
            command=lambda: self.goToFrameSV(),
        )
        self.fenetre.bind_all("<Control-Key-v>", lambda v: self.goToFrameSV())
        menuTools = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Tools", menu=menuTools)
        menuTools.add_command(
            label="Go to frame...",
            underline=0,
            accelerator="(Ctrl + G)",
            command=lambda: self.goToFrameWindow(),
        )
        self.fenetre.bind_all("<Control-Key-g>", lambda g: self.goToFrameWindow())
        menuGraph = tk.Menu(menuTools, tearoff=0)
        menuTools.add_cascade(label="Plot Graph...", menu=menuGraph)
        menuGraph.add_command(
            label="X depending of T",
            underline=13,
            accelerator="(Ctrl + X)",
            command=lambda: self.controller.graph.graphX(),
        )
        self.fenetre.bind_all(
            "<Control-Key-x>", lambda x: self.controller.graph.graphX()
        )
        menuGraph.add_command(
            label="Y depending of T",
            underline=13,
            accelerator="(Ctrl + Y)",
            command=lambda: self.controller.graph.graphY(),
        )
        self.fenetre.bind_all(
            "<Control-Key-y>", lambda y: self.controller.graph.graphY()
        )
        menuGraph.add_command(
            label="X and Y depending of T",
            underline=34,
            accelerator="(Ctrl + T)",
            command=lambda: self.controller.graph.graph3(),
        )
        self.fenetre.bind_all(
            "<Control-Key-t>", lambda t: self.controller.graph.graph3()
        )
        menuHelp = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=menuHelp)
        # WORK IN PROGRESS
        menuHelp.add_command(
            label="Instruction manual",
            underline=0,
            accelerator="(Ctrl + I)",
            command=lambda: self.goToFrameHelp(),
        )
        self.fenetre.bind_all("<Control-Key-i>", lambda h: self.goToFrameHelp())

        # WORK IN PROGRESS
        buttonsFrame = tk.Frame(self.fenetre, bg="#BB620D")
        buttonsFrame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Button(
            buttonsFrame,
            text="Set up scale",
            bg="#FF9F45",
            state=tk.DISABLED,
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
        self.fenetre.bind_all(
            "<Left>", lambda l: self.controller.video.previousFrame(button)
        )
        button = tk.Button(
            buttonsFrame,
            text=">",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            width=15,
            font=("calibri", 25, "bold"),
        )
        button.config(
            command=lambda: [
                self.controller.video.play_or_pause(),
                self.controller.changeTextPlay(button),
            ]
        )
        self.fenetre.bind_all(
            "<space>",
            lambda s: [
                self.controller.video.play_or_pause(),
                self.controller.changeTextPlay(button),
            ],
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
        self.fenetre.bind_all(
            "<Right>", lambda r: self.controller.video.nextFrame(button)
        )
        buttonsFrame.pack(side=tk.BOTTOM, fill=tk.X)
        buttonPoint = tk.Button(
            buttonsFrame,
            text="Click to place the points",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            font=(
                "calibri",
                15,
            ),
        )
        buttonPoint.config(
            command=lambda: self.controller.drawpoint.putPointClicked(buttonPoint)
        )
        buttonPoint.pack(side=tk.LEFT, padx=30, pady=7)

    def get_window(self):
        try:
            print("View.py : get_window() called")
            return self.fenetre
        except Exception as e:
            print("View.py : ERROR detected on get_window: [", e, "]")

    def load_video(self):
        print("View.py: open_file() called")
        self.controller.browse_file()

    def window_pos(self, window, w_width, w_height):
        s_width = window.winfo_screenwidth()
        s_height = window.winfo_screenheight()
        self.center_x = int(s_width / 2 - w_width / 2)
        self.center_y = int(s_height / 2 - w_height / 2)
        pos = f"{w_width}x{w_height}+{self.center_x}+{self.center_y}"
        return pos

    def goToFrameWindow(self):
        try:
            # Si video ouverte --> creation d'une fenetre fille
            if self.controller.video.videoOpened() == True:
                F_Window = tk.Toplevel()
                F_Window.configure(background="#ADDAEF")
                F_Window.title("Choose when to go")
                F_Window.grab_set()
                w_width = 450
                w_height = 150
                F_Window.geometry(self.window_pos(F_Window, w_width, w_height))
                F_Window.resizable(False, False)

                # Creation d'un label et d'un bouton
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
                "Error - Go to frame...", "You haven't opened a video yet."
            )

    # WORK IN PROGRESS
    def goToFrameHelp(self):
        H_Window = tk.Toplevel()
        H_Window.configure(background="#ADDAEF")
        H_Window.title("Instruction manual")
        w_width = int(H_Window.winfo_screenwidth() / float(2.2))
        w_height = int(H_Window.winfo_screenheight() / float(2))
        H_Window.geometry(self.window_pos(H_Window, w_width, w_height))
        TEXTE = "Liste des raccourcis clavier :\n  -Ctrl+0 = Open the video \n  -Ctrl+A = Save as \n  -Ctrl+S = Save \n  -Ctrl+Q = Quit the application \n  -Ctrl+V = Show values \n  -Ctrl+G = Go to frame \n  -Ctrl+I = Help" 
        label = tk.Label(H_Window, text=TEXTE, background="#9DCDE3", wraplength = 500,justify = tk.LEFT)
        label.pack(side=TOP, fill='x')
        label.place(x=0, y=0)
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
    # WORK IN PROGRESS
    def goToFrameSV(self):
        pass
