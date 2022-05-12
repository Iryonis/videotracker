from logging import makeLogRecord
from tkinter import *

class drawPoint:
    def __init__(self):
        self.state = False
        self.marker = (0,0)

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
        self.x = int(
            self.controller.video.canvas.winfo_pointerx()
            - self.controller.video.canvas.winfo_rootx()
        )
        self.y = int(
            self.controller.video.canvas.winfo_pointery()
            - self.controller.video.canvas.winfo_rooty()
        )
        xRep, yRep = self.marker
        print(xRep)
        print(yRep)
        self.x = int(self.x - xRep)
        self.y = int(self.y - yRep)
        print(self.x, self.y)
        self.controller.video.canvas.create_oval(
            int(self.x),
            int(self.y),
            int(self.x + 7),
            int(self.y + 7),
            width=0,
            fill="red",
        )

    def clickPutMarker(self):
        self.controller.video.canvas.bind("<Control-1>", self.putMarker)

    def putMarker(self, event):
        x = int(
            self.controller.video.canvas.winfo_pointerx()
            - self.controller.video.canvas.winfo_rootx()
        )
        y = int(
            self.controller.video.canvas.winfo_pointery()
            - self.controller.video.canvas.winfo_rooty()
        )
        self.controller.video.canvas.create_oval(
            int(x),
            int(y),
            int(x + 7),
            int(y + 7),
            width=0,
            fill="red",
        )
        self.controller.video.canvas.create_line(int(x+3), int(y+3), int(x+203), int(y+3), fill ="red")
        self.controller.video.canvas.create_line(int(x+3), int(y+3), int(x+3), int(y-203), fill ="red")
        self.marker = (x, y)
        print(self.marker)
