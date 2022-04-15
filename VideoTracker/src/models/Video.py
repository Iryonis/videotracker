from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import platform


class Video:
    def __init__(self, window):
        print("Video.py: __init__()")
        try:
            print(os.getcwd())
            self.window = window
            self.canvas = Canvas(self.window, width=1000, height=600, bg="#03051E")
            self.canvas.pack(side=TOP, expand=True)
            self.delay = 18
            print("Video.py: __init__() - OK")
        except Exception as e:
            print("Video.py: ERROR detected on init: [", e, "]")

    def open_window(self):
        print("View.py: open_window called")
        try:
            self.window.mainloop()
        except Exception as e:
            print("View.py: ERROR detected on opening window: [", e, "]")

    def open_file(self):
        print("Video.py: open_file()")
        if platform.system() == "Windows":
            self.nextPath = "/VideoTracker/resources/videos"
        elif platform.system() == "Linux":
            self.nextPath = "/resources/videos"
        self.pause = True
        self.filename = fd.askopenfilename(
            initialdir=(os.getcwd() + self.nextPath),
            filetypes=(
                ("MP4 Files", "*.mp4"),
                ("MKV Files", "*.mkv"),
            ),
        )
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width=self.width, height=self.height)
        print(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    def play_or_pause(self, button):
        try:
            if self.cap.isOpened():
                self.changeText(button)
                self.pause = not self.pause
                if not self.pause:
                    self.play_video()
        except:
            messagebox.showerror(
                "Error - Button Play/Pause",
                "You haven't opened a video for the moment ; thus, you can't launch it.",
            )

    def changeText(self, button):
        if self.pause == False:
            button["text"] = ">"
        elif self.pause == True:
            button["text"] = "||"

    def nextFrame(self):
        try:
            if self.cap.isOpened():
                self.window.after(1, self.play_video)
                print(
                    "La frame actuelle (nextFrame) est :",
                    self.cap.get(cv2.CAP_PROP_POS_FRAMES),
                )
        except:
            messagebox.showerror(
                "Error - Next Frame", "You haven't opened a video yet."
            )

    def previousFrame(self):
        try:
            if self.cap.isOpened():
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

    def firstFrame(self):
        try:
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
            messagebox.showerror("Error", "You haven't opened a video yet.")

    def currentFrame(self):
        try:
            if self.cap.isOpened():
                frameActuelle = (
                    "The current frame is : "
                    + str(int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)))
                    + "/"
                    + str(int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)))
                )
                messagebox.showinfo("Current Frame", frameActuelle)
        except:
            messagebox.showerror(
                "Error - Current Frame", "You haven't opened a video yet."
            )

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
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

            if not self.pause:
                self.window.after(self.delay, self.play_video)
        except:
            messagebox.showerror(
                "Error - Playing the video",
                "The video has already ended or you haven't chosen a video.",
            )

    def __del__(self):
        try:
            if self.cap.isOpened():
                self.cap.release()
        except Exception as e:
            print("Video.py: ERROR detected on delete: [", e, "]")

    def quit(self, window):
        self.__del__()
        window.destroy()

    def closeHelp(self, H_Window):
        H_Window.quit()
