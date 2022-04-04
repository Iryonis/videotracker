from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
from tkinter import filedialog as fd


class Video:

    def __init__(self, window, window_title):
        print("Video.py: __init__()")
        try:
            self.window = window
            self.window.title(window_title)
            self.canvas = Canvas(window)
            self.canvas.pack()
            self.delay = 15   # ms
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
        self.pause = True
        self.filename = fd.askopenfilename()
        print(self.filename)
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)

    def play_button(self):
        self.pause = False

    def pause_button(self):
        self.pause = True

    # get only one frame
    def get_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        if not self.pause:
            self.window.after(self.delay, self.play_video)

    # Release the video source when the object is destroyed
    def __del__(self):
        try:
            if self.cap.isOpened():
                self.cap.release()
        except Exception as e:
            print("Video.py: ERROR detected on delete: [", e, "]")
            return None
