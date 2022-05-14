from tkinter import filedialog as fd
import os


class Controller:
    def __init__(self, video, view, point, filerepo, graph, drawpoint):
        self.video = video
        self.view = view
        self.point = point
        self.filerepo = filerepo
        self.graph = graph
        self.drawpoint = drawpoint

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
