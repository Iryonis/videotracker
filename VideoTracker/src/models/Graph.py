import tkinter as tk
from tkinter import filedialog as fd
import os, csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self):
        global nb
        nb = 0

    def setController(self, controller):
        print("Graph.py: Controller set")
        self.controller = controller

    def graphX(self):
        self.openFile()
        global nb
        nb = 1
        self.windowGraph()

    def graphY(self):
        self.openFile()
        global nb
        nb = 2
        self.windowGraph()

    def graph3(self):
        self.openFile()
        global nb
        nb = 3
        self.windowGraph()

    def openFile(self):
        # Ouvre un explorateur de fichier pour que l'utilisateur indique quel fichier CSV il veut utiliser pour le graphe
        nextPath = "/resources/resultats"
        filename = fd.askopenfilename(
            initialdir=(os.getcwd() + nextPath),
            filetypes=(("CSV Files", "*.csv"),),
        )
        self.retrieveData(filename)

    def retrieveData(self, filename):
        # Récupère les données des colonnes 0, 1 et 2
        self.t = []
        self.x = []
        self.y = []
        with open(filename, "r") as headers:
            my_reader = csv.reader(headers, delimiter=";")
            for col in my_reader:
                self.t += [col[0]]
                self.x += [col[1]]
                self.y += [col[2]]
        self.t = [int(i) for i in self.t]
        self.x = [float(i) for i in self.x]
        self.y = [float(i) for i in self.y]

        # Créer une fenêtre grâce à Tkinter

    def windowGraph(self):
        G_Window = tk.Toplevel()
        G_Window.configure(background="#ADDAEF")
        w_width = int(G_Window.winfo_screenwidth() / float(1.8))
        w_height = int(G_Window.winfo_screenheight() / float(1.5))
        G_Window.geometry(self.controller.view.window_pos(G_Window, w_width, w_height))
        G_Window.resizable(False, False)
        global nb

        # Construit le graphique demandé grâce à matplotlib
        if nb == 1:
            G_Window.title("Graph of X as a function of time T")
            self.drawGraphX(G_Window)
        elif nb == 2:
            G_Window.title("Graph of Y as a function of time T")
            self.drawGraphY(G_Window)
        elif nb == 3:
            G_Window.title("Graph of Y = f(X)")
            self.drawGraph3(G_Window)

        # Créer le bouton pour fermer la fenêtre avec Tkinter
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

    def drawGraphX(self, window):
        plot = plt.figure(figsize=(11, 6))
        plt.scatter(self.t, self.x, c="#BB620D")
        plt.title("Graph of X as a function of time T")
        plt.xlabel("Time axis T")
        plt.ylabel("X axis")
        axis = plt.gca()
        axis.set_facecolor("#ADDAEF")
        plot.patch.set_facecolor("#ADDAEF")
        graph = FigureCanvasTkAgg(plot, master=window)
        graph.get_tk_widget().pack(side=tk.TOP)
        graph.draw()

    def drawGraphY(self, window):
        plot = plt.figure(figsize=(11, 6))
        plt.scatter(self.t, self.y, c="#BB620D")
        plt.title("Graph of Y as a function of time T")
        plt.xlabel("Time axis T")
        plt.ylabel("Y axis")
        axis = plt.gca()
        axis.set_facecolor("#ADDAEF")
        plot.patch.set_facecolor("#ADDAEF")
        graph = FigureCanvasTkAgg(plot, master=window)
        graph.get_tk_widget().pack(side=tk.TOP)
        graph.draw()

    def drawGraph3(self, window):
        plot = plt.figure(figsize=(11, 6))
        plt.scatter(self.x, self.y, c=self.t)
        plt.title("Graph Y = f(X)")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        cbar = plt.colorbar()
        cbar.ax.set_title("Time (in seconds)")
        axis = plt.gca()
        axis.set_facecolor("#ADDAEF")
        plot.patch.set_facecolor("#ADDAEF")
        graph = FigureCanvasTkAgg(plot, master=window)
        graph.get_tk_widget().pack(side=tk.TOP)
        graph.draw()

    # Fonctions pour les tests unitaires de TestGraph.py
    def window_t(self):
        self.t
        return self.t

    def window_x(self):
        return self.x

    def window_y(self):
        return self.y
