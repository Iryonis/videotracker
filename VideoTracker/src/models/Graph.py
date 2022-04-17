import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import platform
import matplotlib.pyplot as plt
import csv


class Graph:
    def __init__(self):
        pass

    def window_pos(self, window, w_width, w_height):
        s_width = window.winfo_screenwidth()
        s_height = window.winfo_screenheight()
        self.center_x = int(s_width / 2 - w_width / 2)
        self.center_y = int(s_height / 2 - w_height / 2)
        pos = f"{w_width}x{w_height}+{self.center_x}+{self.center_y}"
        return pos

    def windowGraph(self):
        if platform.system() == "Windows":
            nextPath = "/VideoTracker/resources/resultats"
        elif platform.system() == "Linux":
            nextPath = "/resources/resultats"
        filename = fd.askopenfilename(
            initialdir=(os.getcwd() + nextPath),
            filetypes=(("CSV Files", "*.csv"),),
        )
        t = []
        x = []
        y = []
        with open(filename, "r") as headers:
            my_reader = csv.reader(headers, delimiter=";")
            for col in my_reader:
                t += [col[0]]
                x += [col[1]]
                y += [col[2]]
        t = [int(i) for i in t]
        x = [float(i) for i in x]
        y = [float(i) for i in y]
        G_Window = tk.Tk()
        G_Window.configure(background="#ADDAEF")
        G_Window.title("Graph")
        w_width = int(G_Window.winfo_screenwidth() / float(1.8))
        w_height = int(G_Window.winfo_screenheight() / float(1.5))
        G_Window.geometry(self.window_pos(self, G_Window, w_width, w_height))
        G_Window.resizable(False, False)

        plt.figure(figsize=(16, 12))
        plt.scatter(x, y, c=t)
        plt.show()

        tk.Button(
            G_Window,
            text="OK",
            width=20,
            height=2,
            background="#9DCDE3",
            activebackground="#ADDAEF",
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.close(G_Window),
        ).pack(side=tk.BOTTOM, padx=30, pady=7)
