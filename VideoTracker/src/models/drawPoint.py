from tkinter import *


class drawPoint:
    def __init__(self, canvas):
        self.canvas = canvas

    def setController(self, controller):
        print("drawPoint.py: Controller set")
        self.controller = controller

    def click(self):
        self.canvas.bind("<Button-3>", self.getCoord)

    def getCoord(self, event):
        self.x = int(self.canvas.winfo_pointerx() - self.canvas.winfo_rootx())
        self.y = int(self.canvas.winfo_pointery() - self.canvas.winfo_rooty())
        print(self.x, self.y)
        self.canvas.create_oval(
            int(self.x),
            int(self.y),
            int(self.x + 7),
            int(self.y + 7),
            width=0,
            fill="red",
        )
