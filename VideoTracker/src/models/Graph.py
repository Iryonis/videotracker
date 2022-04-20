import tkinter as tk
from tkinter import filedialog as fd
import os
import platform
import matplotlib.pyplot as plt
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self):
        pass

    def setController(self, controller):
        print("Graph.py: Controller set")
        self.controller = controller

    def openFile(self):
        # Ouvre un explorateur de fichier pour que l'utilisateur indique quel fichier CSV il veut utiliser pour le graphe
        if platform.system() == "Windows":
            nextPath = "/VideoTracker/resources/resultats"
        elif platform.system() == "Linux":
            nextPath = "/resources/resultats"
        filename = fd.askopenfilename(
            initialdir=(os.getcwd() + nextPath),
            filetypes=(("CSV Files", "*.csv"),),
        )
        self.retrieveData(filename)
        self.windowGraph()

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
        G_Window.title("Graph")
        w_width = int(G_Window.winfo_screenwidth() / float(1.8))
        w_height = int(G_Window.winfo_screenheight() / float(1.5))
        G_Window.geometry(self.controller.view.window_pos(G_Window, w_width, w_height))
        G_Window.resizable(False, False)

        # Construit le graphique grâce à matplotlib
        plot = plt.figure(figsize=(11, 6))
        plt.scatter(self.x, self.y, c=self.t)
        plt.title("Graphique y = f(x)")
        plt.xlabel("Axe des X")
        plt.ylabel("Axe des Y")
        cbar = plt.colorbar()
        cbar.ax.set_title("Temps (en secondes)")
        axis = plt.gca()
        axis.set_facecolor("#ADDAEF")
        plot.patch.set_facecolor("#ADDAEF")
        graph = FigureCanvasTkAgg(plot, master=G_Window)
        graph.get_tk_widget().pack(side=tk.TOP)
        graph.draw()

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

    def window_t(self):
        self.t
        return self.t

    def window_x(self):
        return self.x

    def window_y(self):
        return self.y
