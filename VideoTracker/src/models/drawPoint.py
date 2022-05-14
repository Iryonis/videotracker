from tkinter import *
from .dataPoints import dataPoints
from .Video import Video
from ..views.view import View

class drawPoint:
    def __init__(self):
        self.state = False
        self.marker = (0,0)
        self.i = 0
        view = View()
        self.video = Video(view.get_window())
        self.dpts = dataPoints(self.video.videoLenght)
        self.dpts.create_tab()

    def clickPutPoint(self):
        if self.state == True:
            self.video.canvas.bind("<Button-3>", self.putPoint)
        else:
            self.video.canvas.unbind("<Button-3>")

    def putPointClicked(self, buttonPoint):
        if self.state == True:
            self.state = False
            buttonPoint["text"] = "Click to place the points"
            self.clickPutPoint()
        else:
            self.state = True
            buttonPoint["text"] = "Right-click on the video"
            self.clickPutPoint()

    def putPoint(self, event):
        xRep, yRep = self.marker
        x = int(
            event.x
        )
        y = int(
            event.y
        )
        self.video.canvas.create_oval(
            int(x-3),
            int(y-3),
            int(x + 4),
            int(y + 4),
            width=0,
            fill="red",
        )
        x = x - xRep
        y = yRep - y
        self.dpts.tabPoints(self.i, x, y)

    def clickMarker(self):
        self.video.canvas.bind("<Control-1>", self.putMarker)

    def putMarker(self, event):
        x = int(
            event.x
        )
        y = int(
            event.y
        )
        self.video.canvas.create_oval(
            int(x-3),
            int(y-3),
            int(x + 4),
            int(y + 4),
            width=0,
            fill="red",
        )
        self.video.canvas.create_line(int(x), int(y), int(x+200), int(y), fill ="red")
        self.video.canvas.create_line(int(x), int(y), int(x), int(y-200), fill ="red")
        self.marker = (x, y)

    def clickPutScale(self):
        pass