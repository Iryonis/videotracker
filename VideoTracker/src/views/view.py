import tkinter as tk
import PIL.Image, PIL.ImageTk
import platform

def save():
    print("Saved")


class View:
    def __init__(self):
        print("View.py: View created")
        try:
            self.fenetre = tk.Tk()
            self.fenetre.configure(bg="#C1F4C5")
            self.fenetre.withdraw
            self.fenetre.title("Video Tracker")
            if platform.system() == 'Windows':
                self.fenetre.attributes("zoomed", True)
            elif platform.system() == 'Linux' :
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
        menuBar = tk.Menu(self.fenetre,bg="#FF9F45")
        self.fenetre.config(menu=menuBar)
        menuFile = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Files", menu=menuFile)
        menuFile.add_command(
            label="Load the video",
            underline=1,
            command=self.load_video,
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
            label="Current frame",
            underline=1,
            command=lambda: self.controller.video.currentFrame(),
        )
        self.fenetre.bind_all(
            "<Control-Key-u>", lambda u: self.controller.video.currentFrame()
        )
        menuTools.add_command(
            label="Go to frame",
            underline=0,
            command=lambda: self.goToFrameWindow(),
        )
        menuHelp = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=menuHelp)
        menuHelp.add_command(
            label="Shortcut",
            underline=0)
        self.fenetre.bind_all("<Control-Key-g>", lambda g: self.goToFrameWindow())

        buttonsFrame = tk.Frame(self.fenetre, bg="#FF9F45")
        buttonsFrame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Button(
            buttonsFrame,
            text="Définir l'échelle",
            bg="#FF9F45",
            activebackground='#E9967A',
            font=(
                "calibri",
                20,
            ),
        ).pack(side=tk.RIGHT, padx=20, pady=7)
        tk.Button(
            buttonsFrame,
            text="Beginning of the video",
            bg="#FF9F45",
            activebackground='#E9967A',
            font=("calibri", 18),
            command=lambda: self.controller.video.firstFrame(),
        ).pack(side=tk.LEFT, padx=30, pady=7)
        self.fenetre.bind_all(
            "<Control-Key-b>", lambda b: self.controller.video.firstFrame()
        )
        tk.Button(
            buttonsFrame,
            text="|<",
            bg="#FF9F45",
            activebackground='#E9967A',
            width = 10,
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.previousFrame(),
        ).pack(side=tk.LEFT, padx=30, pady=7, fill="none", expand=True)
        self.fenetre.bind_all("<Left>", lambda l: self.controller.video.previousFrame())
        button = tk.Button(buttonsFrame, text=">",bg="#FF9F45", activebackground='#E9967A', width = 15, font=("calibri", 25, "bold"))
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
            activebackground='#E9967A',
            width = 10,
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.nextFrame(),
        ).pack(side=tk.LEFT, padx=30, pady=7, fill="none", expand=True)
        self.fenetre.bind_all("<Right>", lambda r: self.controller.video.nextFrame())

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

    def goToFrameWindow(self):
        F_Window = tk.Tk()
        F_Window.title("Choose when to go")
        F_Window.geometry("800x500")
        F_Window.resizable(False, False)
        tk.Button(
            F_Window,
            text="OK",
            font=("calibri", 20, "bold"),
            command=lambda: self.chooseValue(),
        ).pack(side=tk.BOTTOM, padx=30, pady=7)

    def chooseValue(self):
        pass
