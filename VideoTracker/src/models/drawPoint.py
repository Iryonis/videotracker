from tkinter import *
from .dataPoints import dataPoints


class drawPoint:
    def __init__(self):
        self.state = False
        self.marker = (0, 0)
        self.i = 0
        self.dpts = dataPoints()

    def get_canvas(self, canvas):
        self.canvas = canvas

    def clickPutPoint(self, canvas):
        if self.state == True:
            canvas.bind("<Button-3>", self.putPoint)
        else:
            canvas.unbind("<Button-3>")

    def putPointClicked(self, buttonPoint):
        if self.state == True:
            self.state = False
            buttonPoint["text"] = "Click to place the points"
            self.clickPutPoint(self.canvas)
        else:
            self.state = True
            buttonPoint["text"] = "Right-click on the video"
            self.clickPutPoint(self.canvas)

    def putPoint(self, event):
        xRep, yRep = self.marker
        x = int(event.x)
        y = int(event.y)
        self.canvas.create_oval(
            int(x - 3),
            int(y - 3),
            int(x + 4),
            int(y + 4),
            width=0,
            fill="red",
        )
        x = x - xRep
        y = yRep - y
        self.dpts.tabPoints(self.i, x, y)

    def clickMarker(self, canvas):
        canvas.bind("<Control-1>", self.putMarker)

    def putMarker(self, event):
        x = int(event.x)
        y = int(event.y)
        self.canvas.create_oval(
            int(x - 3),
            int(y - 3),
            int(x + 4),
            int(y + 4),
            width=0,
            fill="red",
        )
        self.canvas.create_line(int(x), int(y), int(x + 200), int(y), fill="red")
        self.canvas.create_line(int(x), int(y), int(x), int(y - 200), fill="red")
        self.marker = (x, y)

    def clickPutScale(self):
        pass
