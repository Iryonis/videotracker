from tkinter import filedialog as fd
import os
from ..models.drawPoint import drawPoint
from tkinter import messagebox
import time


class Controller:
    def __init__(self, video, view, point, filerepo, graph):
        self.video = video
        self.view = view
        self.point = point
        self.filerepo = filerepo
        self.graph = graph
        self.window = self.video.window

    def change_text_play(self, buttonP):
        if self.video.pause == False:
            buttonP["text"] = "||"
        elif self.video.pause == True:
            buttonP["text"] = ">"

    def browse_file_video(self):
        nextPath = "/resources/videos"
        self.video.pause = True
        filename = fd.askopenfilename(
            initialdir=(os.getcwd() + nextPath),
            filetypes=(
                ("MP4 Files", "*.mp4"),
                ("MKV Files", "*.mkv"),
            ),
        )
        self.video.open_file_video(filename)

    def save(self, nb):
        if self.aimingState == False:
            if nb == 1:
                self.filerepo.save_as(
                    self.dp.dpts.get_tabTmp(),
                    self.dp.dpts.get_tabPts(),
                    self.dp.get_ratio(),
                )
            elif nb == 2:
                self.filerepo.save(
                    self.dp.dpts.get_tabTmp(),
                    self.dp.dpts.get_tabPts(),
                    self.dp.get_ratio(),
                )
        else:
            messagebox.showwarning(
                "Warning - Save",
                "You haven't ended the aiming yet.\nEnd it before trying again.",
            )

    def open_file_graph(self):
        nextPath = "/resources/resultats"
        filename = fd.askopenfilename(
            initialdir=(os.getcwd() + nextPath),
            filetypes=(("CSV Files", "*.csv"),),
        )
        self.graph.retrieve_data(filename)

    def get_t(self):
        return self.graph.window_t()

    def get_x(self):
        return self.graph.window_x()

    def get_y(self):
        return self.graph.window_y()

    # drawPoint controller :

    def click_button_scale(self):
        try:
            if self.video.cap.isOpened():
                self.dp = drawPoint()
                self.aimingState = False
                self.dp.get_canvas(self.video.get_canvas())
                self.dp.click_put_scale()
                self.dp.dpts.create_tab(self.video.get_TotTime())
        except:
            messagebox.showerror(
                "Error - Set up scale", "You haven't opened a video yet."
            )

    def click_button_points(self, buttonPoint):
        try:
            if self.dp.value != 0:
                if self.dp.marker != (0, 0):
                    self.buttonPoint = buttonPoint
                    self.state = self.dp.text_button_point(buttonPoint)
                    self.bind_put_point()
                else:
                    messagebox.showerror(
                        "Error - Place the points", "You haven't set up a marker yet."
                    )
        except:
            messagebox.showerror(
                "Error - Place the points", "You haven't set up a scale yet."
            )

    def bind_put_point(self):
        self.canvas = self.video.get_canvas()
        if self.state == True:
            self.aimingState = True
            self.canvas.bind("<Button-1>", self.put_point_controller)
            self.window.bind("<Escape>", self.stop_point)
        else:
            self.aimingState = False
            self.canvas.unbind("<Button-1>")

    def stop_point(self, event):
        self.aimingState = False
        self.canvas.unbind("<Button-1>")
        self.dp.text_button_point(self.buttonPoint)
        self.stoppedPoint = True
        messagebox.showinfo("Info - Aiming", "You have stopped the aiming.")

    def put_point_controller(self, event):
        if self.video.get_next_frame() == True:
            if self.aimingState == False:
                self.aimingState = True
            frame = int(self.video.get_current_frame())
            self.video.cap.set(frame, frame + 1)
            self.video.play_video()
            self.time = self.video.get_current_frame()
            self.dp.put_point(event, self.time)
        else:
            self.canvas.unbind("<Button-1>")
            self.aimingState = False
            self.dp.text_button_point(self.buttonPoint)
            messagebox.showinfo(
                "Info - Aiming",
                "You have arrived at the end of the video, thus the aiming has stopped.",
            )

    def reset(self):
        try:
            self.dp.value = 0
            self.dp.marker = (0, 0)
            self.dp.stateScale = 0
            if self.state == True:
                self.dp.text_button_point(self.buttonPoint)
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Button-3>")
            self.canvas.unbind("<Control-1>")
        except:
            print("The reset has failed !")

    # Video.py controller :

    def go_to_frame_end(self):
        self.video.last_frame()
