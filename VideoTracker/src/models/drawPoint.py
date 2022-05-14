from tkinter import *

class drawPoint:
    def __init__(self):
        self.state = False
        self.marker = (0,0)
        self.i = 0

    def setController(self, controller):
        print("drawPoint.py: Controller set")
        self.controller = controller

    def clickPutPoint(self):
        if self.state == True:
            self.controller.video.canvas.bind("<Button-3>", self.putPoint)
        else:
            self.controller.video.canvas.unbind("<Button-3>")

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
        self.controller.video.canvas.create_oval(
            int(x-3),
            int(y-3),
            int(x + 4),
            int(y + 4),
            width=0,
            fill="red",
        )
        x = x - xRep
        y = yRep - y
        self.controller.point.setX(x)
        self.controller.point.setY(y)
        self.controller.datapoints.tabPoints(self.i)

    def clickMarker(self):
        self.controller.video.canvas.bind("<Control-1>", self.putMarker)

    def putMarker(self, event):
        x = int(
            event.x
        )
        y = int(
            event.y
        )
        self.controller.video.canvas.create_oval(
            int(x-3),
            int(y-3),
            int(x + 4),
            int(y + 4),
            width=0,
            fill="red",
        )
        self.controller.video.canvas.create_line(int(x), int(y), int(x+200), int(y), fill ="red")
        self.controller.video.canvas.create_line(int(x), int(y), int(x), int(y-200), fill ="red")
        self.marker = (x, y)
        self.time = self.controller.video.getTime()

    def clickPutScale(self):
        pass