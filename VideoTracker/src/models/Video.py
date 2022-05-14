from tkinter import *
import PIL.Image, PIL.ImageTk, cv2, sys
from tkinter import messagebox


class Video:
    def __init__(self, window):
        try:
            self.window = window
            self.canvas = Canvas(self.window, width=1000, height=600, bg="#03051E")
            self.canvas.pack(side=TOP, expand=True)
            self.delay = 0
            self.max_height = self.window.winfo_screenheight() - 107
            print("Video.py: __init__() called")
        except Exception as e:
            print("Video.py: ERROR detected on __init__(): [", e, "]")

    def open_file(self, filename):
        print("Video.py: open_file()")
        self.cap = cv2.VideoCapture(filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        if self.height > self.max_height:
            self.canvas.config(width=self.width, height=self.max_height)
        else:
            self.canvas.config(width=self.width, height=self.height)
        self.delay = (1 / self.cap.get(cv2.CAP_PROP_FPS)) * 1000
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.videoLenght = str(int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    def get_canvas(self):
        return self.canvas

    def play_or_pause(self):
        try:
            if self.cap.isOpened():
                self.pause = not self.pause
                if not self.pause:
                    self.play_video()
        except:
            messagebox.showerror(
                "Error - Play video",
                "You haven't opened a video for the moment ; thus, you can't start it.",
            )

    def nextFrame(self, buttonP):
        try:
            buttonP["text"] = ">"
            if self.cap.isOpened():
                if self.pause == False:
                    self.pause = True
                self.window.after(1, self.play_video)
                print(
                    "La frame actuelle (nextFrame) est :",
                    self.cap.get(cv2.CAP_PROP_POS_FRAMES),
                )
        except:
            messagebox.showerror(
                "Error - Next Frame", "You haven't opened a video yet."
            )

    def previousFrame(self, buttonP):
        try:
            buttonP["text"] = ">"
            if self.cap.isOpened():
                if self.pause == False:
                    self.pause = True
                frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame - 2)
                print(
                    "La frame actuelle (previousFrame) est :",
                    self.cap.get(cv2.CAP_PROP_POS_FRAMES),
                )
                self.play_video()
        except:
            messagebox.showerror(
                "Error - Previous Frame", "You haven't opened a video yet."
            )

    def firstFrame(self, buttonP):
        try:
            buttonP["text"] = ">"
            if self.cap.isOpened():
                if self.pause == False:
                    self.pause = True
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                print(
                    "La frame actuelle (firstFrame) est :",
                    self.cap.get(cv2.CAP_PROP_POS_FRAMES),
                )
                self.play_video()
        except:
            messagebox.showerror(
                "Error - First Frame", "You haven't opened a video yet."
            )

    def currentFrame(self):
        try:
            if self.cap.isOpened():
                frameActuelle = (
                    "The current frame is : "
                    + str(int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)))
                    + "/"
                    + self.videoLenght
                )
                return frameActuelle
        except:
            messagebox.showerror(
                "Error - Current Frame", "You haven't opened a video yet."
            )

    def chooseValue(self, entry, window):
        value = entry.get()
        if value == "":
            window.destroy()
        value = float(value)
        if value > (self.cap.get(cv2.CAP_PROP_FRAME_COUNT)):
            print(value > (self.cap.get(cv2.CAP_PROP_FRAME_COUNT)))
            maxF = (self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, maxF)
            self.play_video()
            window.destroy()
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, value - 1)
        self.play_video()
        window.destroy()

    def get_frame(self):
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except:
            print("The video has come to an end.")

    def play_video(self):
        try:
            ret, frame = self.get_frame()
            if (not self.pause) and ret:
                self.window.after(int(self.delay), self.play_video)
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        except:
            print("play_video() - ERROR --> this is probably that the video has ended.")

    def getTime(self):
        return int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))

    # Ferme toutes les fenetres et quitte le processus
    def quit(self):
        sys.exit()

    # Ferme juste la fenetre specifiee
    def close(self, window):
        window.destroy()
