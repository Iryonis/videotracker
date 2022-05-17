from tkinter import *
from tkinter import messagebox
from .dataPoints import dataPoints


class drawPoint:
    def __init__(self):
        self.state = False
        self.marker = (0, 0)
        self.i = 0
        self.dpts = dataPoints()
        self.stateScale = 0

    def get_canvas(self, canvas):
        self.canvas = canvas

    # Put the scale :

    def clickPutScale(self):
        if self.stateScale == 0:
            self.canvas.bind("<Button-3>", self.putScale)
        else:
            self.canvas.unbind("<Button-3>")
            self.clickMarker(self.canvas)

    def putScale(self, event):
        if self.stateScale == 0:
            self.x1 = int(event.x)
            self.y1 = int(event.y)
            self.canvas.create_oval(
                int(self.x1 - 3),
                int(self.y1 - 3),
                int(self.x1 + 4),
                int(self.y1 + 4),
                width=0,
                fill="red",
                tags="scale",
            )
            self.stateScale = 1
        else:
            x2 = int(event.x)
            y2 = int(event.y)
            self.canvas.create_line(
                self.x1,
                self.y1,
                x2,
                y2,
                fill="red",
                tags="scale",
            )
            self.canvas.create_oval(
                int(x2 - 3),
                int(y2 - 3),
                int(x2 + 4),
                int(y2 + 4),
                width=0,
                fill="red",
                tags="scale",
            )
            self.chooseScale(x2, y2)
            self.clickPutScale()

    def chooseScale(self, x, y):
        try:
            S_Window = Toplevel()
            S_Window.configure(background="#ADDAEF")
            S_Window.title("Choose the value of the scale")
            S_Window.grab_set()
            w_width = 450
            w_height = 150
            S_Window.geometry(f"{w_width}x{w_height}+{x}+{y}")
            S_Window.resizable(False, False)
            Label(S_Window, text="Enter the real distance between the two points").pack(
                side=TOP, pady=7
            )
            entry = Entry(S_Window)
            entry.pack(side=TOP, pady=7)
            entry.focus()
            Button(
                S_Window,
                text="OK",
                width=20,
                height=2,
                background="#9DCDE3",
                activebackground="#ADDAEF",
                font=("calibri", 20, "bold"),
                command=lambda: self.get_scale(entry, S_Window),
            ).pack(side=BOTTOM, padx=25, pady=7)
            S_Window.bind_all(
                "<Return>",
                lambda g: self.get_scale(entry, S_Window),
            )
        except:
            pass

    def get_scale(self, entry, window):
        self.value = entry.get()
        self.value = int(self.value)
        self.canvas.delete("scale")
        window.destroy()

    # Put the marker :

    def clickMarker(self, canvas):
        canvas.bind("<Control-1>", self.putMarker)

    def putMarker(self, event):
        self.canvas.delete("marker")
        x = int(event.x)
        y = int(event.y)
        self.canvas.create_oval(
            int(x - 3),
            int(y - 3),
            int(x + 4),
            int(y + 4),
            width=0,
            fill="red",
            tags="marker",
        )
        self.canvas.create_line(
            int(x),
            int(y),
            int(x + 200),
            int(y),
            fill="red",
            tags="marker",
        )
        self.canvas.create_line(
            int(x),
            int(y),
            int(x),
            int(y - 200),
            fill="red",
            tags="marker",
        )
        self.marker = (x, y)

    # Put the points :

    def textButtonPoint(self, buttonPoint):
        if self.state == True:
            self.state = False
            buttonPoint["text"] = "Click to place the points"
            return self.state
        else:
            self.state = True
            buttonPoint["text"] = "Left-click on the video"
            return self.state

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
        self.i = self.i + 1
