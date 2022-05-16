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
        self.window = self.video.window

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

    def save(self, nb):
        if nb == 1:
            self.filerepo.saveAs(
                self.dp.dpts.get_tabTmp(),
                self.dp.dpts.get_tabPts(),
            )
        elif nb == 2:
            self.filerepo.save(
                self.dp.dpts.get_tabTmp(),
                self.dp.dpts.get_tabPts(),
            )

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

    # drawPoint controller :

    def clickButtonScale(self):
        try:
            if self.video.cap.isOpened():
                self.dp = drawPoint()
                self.dp.get_canvas(self.video.get_canvas())
                self.dp.clickPutScale()
                self.dp.dpts.create_tab(
                    self.video.get_currentframe(), self.video.getTotTime()
                )
        except:
            messagebox.showerror(
                "Error - Set up scale", "You haven't opened a video yet."
            )

    def clickButtonPoints(self, buttonPoint):
        try:
            if self.dp.value != 0:
                if self.dp.marker != (0, 0):
                    self.determineEnd()
                    self.buttonPoint = buttonPoint
                    self.state = self.dp.textButtonPoint(buttonPoint)
                    self.bindPutPoint()
                else:
                    messagebox.showerror(
                        "Error - Place the points", "You haven't set up a marker yet."
                    )
        except:
            messagebox.showerror(
                "Error - Place the points", "You haven't set up a scale yet."
            )

    def determineEnd(self):
        self.dp.calculEnd(self.video.get_currentframe(), self.video.getTotTime())

    def bindPutPoint(self):
        self.canvas = self.video.get_canvas()
        if self.state == True:
            self.canvas.bind("<Button-1>", self.putPointController)
            self.window.bind("<Escape>", self.stopPoint)
        else:
            self.canvas.unbind("<Button-1>")

    def stopPoint(self, event):
        self.canvas.unbind("<Button-1>")
        self.dp.putPointClicked(self.buttonPoint)
        self.stoppedPoint = True

    def putPointController(self, event):
        self.window.after(1, self.video.play_video)
        self.dp.putPoint(event)

    def reset(self):
        try:
            self.dp.value = 0
            self.dp.marker = (0, 0)
            self.dp.stateScale = 0
            if self.state == True:
                self.dp.textButtonPoint(self.buttonPoint)
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Button-3>")
            self.canvas.unbind("<Control-1>")
            self.determineEnd()
        except:
            print("The reset has failed !")
