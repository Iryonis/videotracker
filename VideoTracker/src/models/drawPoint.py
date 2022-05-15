from tkinter import *
from .dataPoints import dataPoints


class drawPoint:
    def __init__(self):
        self.state = False
        self.marker = (0, 0)
        self.i = 0
        self.dpts = dataPoints()
        global isScalePut
        isScalePut = 0

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
        global isScalePut
        if isScalePut == 0:
            self.canvas.bind("<Button-1>", self.putScale)
        else:
            self.canvas.unbind("<Button-1>")
            self.clickMarker(self.canvas)

    def putScale(self, event):
        global isScalePut
        if isScalePut == 0:
            self.x1 = int(event.x)
            self.y1 = int(event.y)
            self.canvas.create_oval(
                int(self.x1 - 3),
                int(self.y1 - 3),
                int(self.x1 + 4),
                int(self.y1 + 4),
                width=0,
                fill="red",
            )
            isScalePut = 1
        else:
            x2 = int(event.x)
            y2 = int(event.y)
            self.canvas.create_line(self.x1, self.y1, x2, y2, fill="red")
            self.canvas.create_oval(
                int(x2 - 3),
                int(y2 - 3),
                int(x2 + 4),
                int(y2 + 4),
                width=0,
                fill="red",
            )
            self.clickPutScale()
