import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import platform
import os
from tkinter import filedialog as fd


def save():
    print("Saved")


class View:
    def __init__(self):
        print("View.py: View created")
        try:
            self.fenetre = tk.Tk()
            self.fenetre.withdraw
            self.fenetre.title("Video Tracker")
            if platform.system() == "windows":
                self.fenetre.state("zoomed", True)
            elif platform.system() == "linux":
                self.fenetre.state("-zoomed", True)
            self.fenetre.state("zoomed")
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
            command=lambda: [
                self.load_video,
                self.controller.video.resetStopwatch(stopwatch),
            ],
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
            command=lambda: self.controller.filerepo.exportDataToCsv(
                self.controller.filerepo,
                dataTimes,
                dataPoints,
                fd.asksaveasfilename(
                    initialdir=os.getcwd() + "/VideoTracker/resources/resultats",
                    initialfile="releve_de_points.csv",
                    defaultextension=".csv",
                    filetypes=[("CSV Files", "*.csv")],
                ),
            ),
        )
        self.fenetre.bind_all(
            "<Control-Key-a>",
            lambda a: self.controller.filerepo.exportDataToCsv(
                self.controller.filerepo,
                dataTimes,
                dataPoints,
                fd.asksaveasfilename(
                    initialdir=os.getcwd() + "/VideoTracker/resources/resultats",
                    initialfile="releve_de_points.csv",
                    defaultextension=".csv",
                    filetypes=[("CSV Files", "*.csv")],
                ),
            ),
        )
        menuFile.add_command(label="Save", underline=0, command=lambda: save)
        self.fenetre.bind_all("<Control-Key-s>", lambda s: save)
        menuFile.add_separator()
        menuFile.add_command(
            label="Quit the app",
            underline=0,
            command=lambda: self.controller.video.quit(self.fenetre),
        )
        self.fenetre.bind_all(
            "<Control-Key-q>", lambda q: self.controller.video.quit(self.fenetre)
        )

        buttonsFrame = tk.Frame(self.fenetre, bg="#FFFFFF")
        buttonsFrame.pack(side=tk.BOTTOM, fill=tk.X)
        self.running = False
        self.update_time = ""
        self.secondssSw = 0
        stopwatch = tk.Label(buttonsFrame, text="00", font=("Arial", 20))
        stopwatch.place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(
            buttonsFrame,
            text="Définir l'échelle",
            font=(
                "calibri",
                20,
                "bold",
                "underline",
            ),
        ).pack(side=tk.RIGHT, padx=20, pady=7)
        tk.Button(
            buttonsFrame,
            text="Beginning of the video",
            font=("calibri", 18),
            command=lambda: [
                self.controller.video.firstFrame(),
                self.controller.video.resetStopwatch(stopwatch),
            ],
        ).pack(side=tk.LEFT, padx=30, pady=7)
        self.fenetre.bind_all(
            "<Control-Key-b>", lambda b: self.controller.video.firstFrame()
        )
        tk.Button(
            buttonsFrame,
            text="|<",
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.previousFrame(),
        ).pack(side=tk.LEFT, padx=30, pady=7)
        self.fenetre.bind_all("<Left>", lambda l: self.controller.video.previousFrame())
        button = tk.Button(buttonsFrame, text=">", font=("calibri", 20, "bold"))
        button.config(
            command=lambda: [
                self.controller.video.play_or_pause(button),
                self.controller.video.startStopwatch(stopwatch),
            ]
        )
        self.fenetre.bind_all(
            "<space>", lambda s: self.controller.video.play_or_pause(button)
        )
        button.pack(side=tk.LEFT, padx=10, pady=7)
        tk.Button(
            buttonsFrame,
            text=">|",
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.nextFrame(),
        ).pack(side=tk.LEFT, padx=30, pady=7)
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
