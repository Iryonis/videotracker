from tkinter import *
import tkinter
import PIL.Image, PIL.ImageTk
import cv2
from tkinter import filedialog as fd


class Video:

    def __init__(self, window):
        print("Video.py: __init__()")
        try:
            self.window = window
            self.canvas = Canvas(self.window, bg="black")
            self.canvas.pack(side=TOP)
            self.delay = 5
            print("Video.py: __init__() - OK")
        except Exception as e:
            print("Video.py: ERROR detected on init: [", e, "]")
            return None

    def open_window(self):
        print("View.py: open_window called")
        try:
            self.window.mainloop()
        except Exception as e:
            print("View.py: ERROR detected on opening window: [", e, "]")
            return None

    def open_file(self):
        print("Video.py: open_file()")
        self.pause = False
        self.filename ="c:/Users/Guilhem/VideoTracker/VideoTracker/jamy.mp4"
        print(self.filename)
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)

    def play_button(self):
        self.pause = False

    def pause_button(self):
        self.pause = True

    def get_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            

    def play_video(self):
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        if not self.pause:
            self.window.after(self.delay, self.play_video)

"""     def __del__(self):
        try:
            if self.cap.isOpened():
                self.cap.release()
        except Exception as e:
            print("Video.py: ERROR detected on delete: [", e, "]")
            return None """
