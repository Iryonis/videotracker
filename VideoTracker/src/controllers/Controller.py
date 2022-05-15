from tkinter import filedialog as fd
import os
from ..models.drawPoint import drawPoint
from tkinter import messagebox


class Controller:
    def __init__(self, video, view, point, filerepo, graph):
        self.video = video
        self.view = view
        self.point = point
        self.filerepo = filerepo
        self.graph = graph

    def changeTextPlay(self, buttonP):
        if self.video.pause == False:
            buttonP["text"] = "||"
        elif self.video.pause == True:
            buttonP["text"] = ">"

    def browse_file(self):
        nextPath = "/resources/videos"
        self.video.pause = True
        filename = fd.askopenfilename(
            initialdir=(os.getcwd() + nextPath),
            filetypes=(
                ("MP4 Files", "*.mp4"),
                ("MKV Files", "*.mkv"),
            ),
        )
        self.video.open_file(filename)

    def clickScale(self):
        try:
            if self.video.cap.isOpened():
                self.dp = drawPoint()
                self.dp.get_canvas(self.video.get_canvas())
                self.dp.clickMarker(self.video.get_canvas())
                self.dp.dpts.create_tab(self.video.getTime(), self.video.getTotTime())
        except:
            messagebox.showerror(
                "Error - Set up scale", "You haven't opened a video yet."
            )

    def putPointClickedController(self, buttonPoint):
        self.dp.putPointClicked(buttonPoint)

    def openFile(self):
        nextPath = "/resources/resultats"
        filename = fd.askopenfilename(
            initialdir=(os.getcwd() + nextPath),
            filetypes=(("CSV Files", "*.csv"),),
        )
        self.graph.retrieveData(filename)

    def get_t(self):
        return self.graph.window_t()

    def get_x(self):
        return self.graph.window_x()

    def get_y(self):
        return self.graph.window_y()
