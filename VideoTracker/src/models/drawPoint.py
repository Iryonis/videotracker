from tkinter import *


class drawPoint:
    def __init__(self):
        self.state = False

    def setController(self, controller):
        print("drawPoint.py: Controller set")
        self.controller = controller

    def click(self):
        self.controller.video.canvas.bind("<Button-3>", self.putMarker)

    def putPointClicked(self, buttonPoint):
        if self.state == True:
            self.state = False
            buttonPoint["text"] = "Click to place the points"
        else:
            self.state = True
            buttonPoint["text"] = "Right-click on the video"

    def putPoint(self, event):
        self.x = int(
            self.controller.video.canvas.winfo_pointerx()
            - self.controller.video.canvas.winfo_rootx()
        )
        self.y = int(
            self.controller.video.canvas.winfo_pointery()
            - self.controller.video.canvas.winfo_rooty()
        )
        print(self.x, self.y)
        xRep = 0
        yRep = 0
        xRep, yRep = self.marker
        self.x = self.x - xRep
        self.y = self.y - yRep
        self.controller.video.canvas.create_oval(
            int(self.x),
            int(self.y),
            int(self.x + 7),
            int(self.y + 7),
            width=0,
            fill="red",
        )

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
        self.marker = (x, y)
        print(self.marker)
