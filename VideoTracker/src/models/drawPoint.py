from tkinter import *


class drawPoint:
    def __init__(self, canvas):
        self.canvas = canvas

    def setController(self, controller):
        print("drawPoint.py: Controller set")
        self.controller = controller

    def getorigin(self, event):
        try:
            x0 = event.x_root
            y0 = event.y_root
            x1 = x0 + 1
            y1 = y0 + 1
            self.canvas.create_oval(x0, y0, x1, y1, width=0, fill="red")
        except:
            print("Error when trying to draw a point.")
