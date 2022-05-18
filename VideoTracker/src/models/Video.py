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

    def open_file_video(self, filename):
        print("Video.py: open_file_video()")
        if filename == "":
            messagebox.showwarning(
                "Warning - Open_file (Video.py)",
                "You haven't chosen any videos ; please try again.",
            )
        else:
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

    def next_frame(self, buttonP):
        try:
            buttonP["text"] = ">"
            if self.cap.isOpened():
                if self.pause == False:
                    self.pause = True
                self.window.after(1, self.play_video)
                print(
                    "La frame actuelle (next_frame) est :",
                    self.cap.get(cv2.CAP_PROP_POS_FRAMES),
                )
        except:
            messagebox.showerror(
                "Error - Next Frame", "You haven't opened a video yet."
            )

    def previous_frame(self, buttonP):
        try:
            buttonP["text"] = ">"
            if self.cap.isOpened():
                if self.pause == False:
                    self.pause = True
                frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame - 2)
                print(
                    "La frame actuelle (previous_frame) est :",
                    self.cap.get(cv2.CAP_PROP_POS_FRAMES),
                )
                self.play_video()
        except:
            messagebox.showerror(
                "Error - Previous Frame", "You haven't opened a video yet."
            )

    def first_frame(self, buttonP):
        try:
            buttonP["text"] = ">"
            if self.cap.isOpened():
                if self.pause == False:
                    self.pause = True
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                print(
                    "La frame actuelle (first_frame) est :",
                    self.cap.get(cv2.CAP_PROP_POS_FRAMES),
                )
                self.play_video()
        except:
            messagebox.showerror(
                "Error - First Frame", "You haven't opened a video yet."
            )

    def last_frame(self):
        try:
            if self.cap.isOpened():
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, (int(self.videoLenght) - 1))
                print(
                    "La frame actuelle (last_frame) est :", (int(self.videoLenght) - 1)
                )
                self.play_video()
        except:
            messagebox.showerror(
                "Error - Last Frame", "You haven't opened a video yet."
            )

    def current_frame(self):
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

    def choose_value(self, entry, window):
        value = entry.get()
        if value == "":
            self.close(window)
            return None
        if float(value) > (self.cap.get(cv2.CAP_PROP_FRAME_COUNT)):
            maxF = (self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, maxF)
            self.play_video()
            self.close(window)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, float(value) - 1)
        self.play_video()
        self.close(window)

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

    def get_TotTime(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_current_frame(self):
        return int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))

    def get_next_frame(self):
        if int(self.get_current_frame() + 1) > self.get_TotTime():
            nf = False
        else:
            nf = True
        return nf

    # Ferme toutes les fenetres et quitte le processus
    def quit(self):
        sys.exit()

    # Ferme juste la fenetre specifiee
    def close(self, window):
        window.destroy()
