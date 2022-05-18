from msilib.schema import tables
import tkinter as tk
import platform
from tkinter import messagebox
from src.models.dataPoints import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class View:
    def __init__(self):
        print("View.py: View created")
        try:
            self.fenetre = tk.Tk()
            self.fenetre.configure(bg="black")
            self.fenetre.withdraw
            self.fenetre.title("Video Tracker - V0.1.0")
            if platform.system() == "Windows":
                self.fenetre.attributes("-fullscreen", True)
            elif platform.system() == "Linux":
                self.fenetre.attributes("-zoomed", True)
        except Exception as e:
            print("View.py: ERROR detected on init: [", e, "]")

    def open_window(self):
        print("View.py: open_window called")
        try:
            self.fenetre.mainloop()
        except Exception as e:
            print("View.py: ERROR detected on open_window(): [", e, "]")

    def set_controller(self, controller):
        print("View.py: Controller set")
        self.controller = controller

    def create_interface(self):
        print("View.py: create_interface called")
        menuBar = tk.Menu(self.fenetre)
        self.fenetre.config(menu=menuBar)
        menuFile = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Files", menu=menuFile)
        menuFile.add_command(
            label="Open the video",
            underline=0,
            accelerator="(Ctrl + O)",
            command=lambda: self.load_video(),
        )
        self.fenetre.bind_all("<Control-Key-o>", lambda o: self.load_video())
        menuFile.add_command(
            label="Play the video",
            underline=0,
            accelerator="(Ctrl + P)",
            command=lambda: self.controller.video.play_or_pause(),
        )
        self.fenetre.bind_all(
            "<Control-Key-p>", lambda p: self.controller.video.play_or_pause()
        )
        menuFile.add_command(
            label="Save as",
            underline=1,
            accelerator="(Ctrl + A)",
            command=lambda: self.controller.save(1),
        )
        self.fenetre.bind_all("<Control-Key-a>", lambda a: self.controller.save(1))
        menuFile.add_command(
            label="Save",
            underline=0,
            accelerator="(Ctrl + S)",
            command=lambda: self.controller.save(2),
        )
        self.fenetre.bind_all("<Control-Key-s>", lambda s: self.controller.save(2))
        menuFile.add_separator()
        menuFile.add_command(
            label="Quit the app",
            underline=0,
            accelerator="(Ctrl + Q)",
            command=lambda: self.controller.video.quit(),
        )
        self.fenetre.bind_all("<Control-Key-q>", lambda q: self.controller.video.quit())
        # WORK IN PROGRESS
        menuEdit = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit", menu=menuEdit)
        menuEdit.add_command(
            label="Show values...",
            underline=5,
            accelerator="(Ctrl + V)",
            command=lambda: self.go_to_edit(),
        )
        self.fenetre.bind_all("<Control-Key-v>", lambda v: self.go_to_SV())
        menuTools = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Tools", menu=menuTools)
        menuTools.add_command(
            label="Go to frame...",
            underline=0,
            accelerator="(Ctrl + G)",
            command=lambda: self.go_to_frame_window(),
        )
        self.fenetre.bind_all("<Control-Key-g>", lambda g: self.go_to_frame_window())
        menuTools.add_command(
            label="Go to last frame",
            underline=16,
            accelerator="(Ctrl + E)",
            command=lambda: self.controller.go_to_frame_end(),
        )
        self.fenetre.bind_all(
            "<Control-Key-e>", lambda e: self.controller.go_to_frame_end()
        )
        menuGraph = tk.Menu(menuTools, tearoff=0)
        menuTools.add_cascade(label="Plot Graph...", menu=menuGraph)
        menuGraph.add_command(
            label="X depending of T",
            underline=13,
            accelerator="(Ctrl + X)",
            command=lambda: self.graph(1),
        )
        self.fenetre.bind_all("<Control-Key-x>", lambda x: self.graph(1))
        menuGraph.add_command(
            label="Y depending of T",
            underline=13,
            accelerator="(Ctrl + Y)",
            command=lambda: self.graph(2),
        )
        self.fenetre.bind_all("<Control-Key-y>", lambda y: self.graph(2))
        menuGraph.add_command(
            label="X and Y depending of T",
            underline=34,
            accelerator="(Ctrl + T)",
            command=lambda: self.graph(3),
        )
        self.fenetre.bind_all("<Control-Key-t>", lambda t: self.graph(3))
        menuHelp = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=menuHelp)
     

        # WORK IN PROGRESS
        menuHelp.add_command(
            label="Instruction manual",
            underline=0,
            accelerator="(Ctrl + I)",
            command=lambda: self.go_to_help(),
        )
        self.fenetre.bind_all("<Control-Key-i>", lambda h: self.go_to_help())

        menuHelp.add_command(
            label="About Us",

            accelerator="(Ctrl + L)",
            underline=0,
            command=lambda: self.About_Us(),
        )
        self.fenetre.bind_all("<Control-Key-l>", lambda h: self.About_Us())

        # WORK IN PROGRESS
        buttonsFrame = tk.Frame(self.fenetre, bg="#BB620D")
        buttonsFrame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Button(
            buttonsFrame,
            text="Set up scale",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            font=(
                "calibri",
                20,
            ),
            command=lambda: self.controller.click_button_scale(),
        ).pack(side=tk.RIGHT, padx=20, pady=7)
        tk.Button(
            buttonsFrame,
            text="Start from the beginning",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            font=("calibri", 18),
            command=lambda: self.controller.video.first_frame(button),
        ).pack(side=tk.LEFT, padx=30, pady=7)
        self.fenetre.bind_all(
            "<Control-Key-b>", lambda b: self.controller.video.first_frame(button)
        )
        tk.Button(
            buttonsFrame,
            text="|<",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            width=10,
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.previous_frame(button),
        ).pack(side=tk.LEFT, padx=30, pady=7, fill="none", expand=True)
        self.fenetre.bind_all(
            "<Left>", lambda l: self.controller.video.previous_frame(button)
        )
        button = tk.Button(
            buttonsFrame,
            text="▶",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            width=15,
            font=("calibri", 25, "bold"),
        )
        button.config(
            command=lambda: [
                self.controller.video.play_or_pause(),
                self.controller.change_text_play(button),
            ]
        )
        self.fenetre.bind_all(
            "<space>",
            lambda s: [
                self.controller.video.play_or_pause(),
                self.controller.change_text_play(button),
            ],
        )
        button.pack(side=tk.LEFT, padx=10, pady=7)
        tk.Button(
            buttonsFrame,
            text=">|",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            width=10,
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.next_frame(button),
        ).pack(side=tk.LEFT, padx=30, pady=7, fill="none", expand=True)
        self.fenetre.bind_all(
            "<Right>", lambda r: self.controller.video.next_frame(button)
        )
        buttonsFrame.pack(side=tk.BOTTOM, fill=tk.X)
        buttonPoint = tk.Button(
            buttonsFrame,
            text="Click to place the points",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            font=(
                "calibri",
                15,
            ),
        )
        buttonPoint.config(
            command=lambda: self.controller.click_button_points(buttonPoint)
        )
        buttonPoint.pack(side=tk.LEFT, padx=30, pady=7)

    def get_window(self):
        try:
            print("View.py : get_window() called")
            return self.fenetre
        except Exception as e:
            print("View.py : ERROR detected on get_window: [", e, "]")

    def load_video(self):
        print("View.py: open_file() called")
        self.controller.browse_file_video()
        self.controller.reset()

    def window_pos(self, window, w_width, w_height):
        s_width = window.winfo_screenwidth()
        s_height = window.winfo_screenheight()
        self.center_x = int(s_width / 2 - w_width / 2)
        self.center_y = int(s_height / 2 - w_height / 2)
        pos = f"{w_width}x{w_height}+{self.center_x}+{self.center_y}"
        return pos

    def go_to_frame_window(self):
        try:
            # Si video ouverte --> creation d'une fenetre fille
            if self.controller.video.cap.isOpened() == True:
                F_Window = tk.Toplevel()
                F_Window.configure(background="#ADDAEF")
                F_Window.title("Choose when to go")
                F_Window.grab_set()
                w_width = 450
                w_height = 150
                F_Window.geometry(self.window_pos(F_Window, w_width, w_height))
                F_Window.resizable(False, False)

                # Creation d'un label et d'un bouton
                tk.Label(F_Window, text="Enter the frame you want to go").pack(
                    side=tk.TOP, pady=7
                )
                entry = tk.Entry(F_Window)
                entry.pack(side=tk.TOP, pady=7)
                entry.focus()
                tk.Label(F_Window, text=self.controller.video.current_frame()).pack(
                    side=tk.LEFT, padx=10
                )
                tk.Button(
                    F_Window,
                    text="OK",
                    width=20,
                    height=2,
                    background="#9DCDE3",
                    activebackground="#ADDAEF",
                    font=("calibri", 20, "bold"),
                    command=lambda: self.controller.video.choose_value(entry, F_Window),
                ).pack(side=tk.BOTTOM, padx=30, pady=7)
                F_Window.bind_all(
                    "<Return>",
                    lambda g: self.controller.video.choose_value(entry, F_Window),
                )
        except:
            messagebox.showerror(
                "Error - Go to frame...", "You haven't opened a video yet."
            )

    # WORK IN PROGRESS
    def go_to_help(self):
        H_Window = tk.Toplevel()
        H_Window.configure(background="#ADDAEF")
        H_Window.title("Instruction manual")
        w_width = 1000
        w_height = int(H_Window.winfo_screenheight() / float(2))
        H_Window.geometry(self.window_pos(H_Window, w_width, w_height))
        TEXTE = "Liste des raccourcis clavier :\n  -Ctrl+0 = Open the video \n  -Ctrl+A = Save as \n  -Ctrl+S = Save \n  -Ctrl+Q = Quit the application \n  -Ctrl+V = Show values \n  -Ctrl+G = Go to frame \n  -Ctrl+I = Help"
        label = tk.Label(
            H_Window, text=TEXTE, background="#9DCDE3", wraplength=500, justify=tk.LEFT
        )
        label.pack(side=tk.TOP, fill="x")
        label.place(x=0, y=0)
        tk.Button(
            H_Window,
            text="OK",
            width=20,
            height=2,
            background="#9DCDE3",
            activebackground="#ADDAEF",
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.close(H_Window),
        ).pack(side=tk.BOTTOM, padx=30, pady=7)

    def About_Us(self):
        H_Window = tk.Toplevel()
        H_Window.configure(background="#ADDAEF")
        H_Window.title("About Us")
        w_width = 1000
        w_height = int(H_Window.winfo_screenheight() / float(2))
        H_Window.geometry(self.window_pos(H_Window, w_width, w_height))
        TEXTE = "Hello. \nWe are two students at the University of Bordeaux. We are called Léo Tarpin and Guilhem Bonnefous. We made this video tracker as a year-end project. This project allowed us to deepen our knowledge in the field of computer science. Specifically in coding with Python. This project also allowed us to learn new things like tkinter."
        label = tk.Label(
            H_Window, text=TEXTE, background="#9DCDE3", wraplength=500, justify=tk.LEFT
        )
        label.pack(side=tk.TOP, fill="x")
        label.place(x=0, y=0)
        tk.Button(
            H_Window,
            text="OK",
            width=20,
            height=2,
            background="#9DCDE3",
            activebackground="#ADDAEF",
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.close(H_Window),
        ).pack(side=tk.BOTTOM, padx=30, pady=7)

    def go_to_edit(self):
        H_Window = tk.Toplevel()
        H_Window.configure(background="#ADDAEF")
        H_Window.title("Points")
        w_width = 1000
        w_height = int(H_Window.winfo_screenheight() / float(2))
        H_Window.geometry(self.window_pos(H_Window, w_width, w_height))
        TEXTE = 'test'
        label = tk.Label(
            H_Window, text=TEXTE, background="#9DCDE3", wraplength=500, justify=tk.LEFT
        )
        label.pack(side=tk.TOP, fill="x")
        label.place(x=0, y=0)
        tk.Button(
            H_Window,
            text="OK",
            width=20,
            height=2,
            background="#9DCDE3",
            activebackground="#ADDAEF",
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.video.close(H_Window),
        ).pack(side=tk.BOTTOM, padx=30, pady=7)
    # WORK IN PROGRESS
    def go_to_SV(self):
        pass

    # PLOT GRAPH :

    def graph(self, nb):
        # Ouvre un explorateur de fichier pour que l'utilisateur indique quel fichier CSV il veut utiliser pour le graphe
        self.controller.open_file_graph()
        self.window_graph(nb)

    def window_graph(self, nb):
        self.t = self.controller.get_t()
        self.x = self.controller.get_x()
        self.y = self.controller.get_y()
        G_Window = tk.Toplevel()
        G_Window.configure(background="#ADDAEF")
        w_width = int(G_Window.winfo_screenwidth() / float(1.8))
        w_height = int(G_Window.winfo_screenheight() / float(1.5))
        G_Window.geometry(self.window_pos(G_Window, w_width, w_height))
        G_Window.resizable(False, False)

        # Construit le graphique demandé grâce à matplotlib
        if nb == 1:
            G_Window.title("Graph of X as a function of time T")
            self.draw_graphX(G_Window)
        elif nb == 2:
            G_Window.title("Graph of Y as a function of time T")
            self.draw_graphY(G_Window)
        elif nb == 3:
            G_Window.title("Graph of Y = f(X)")
            self.draw_graph3(G_Window)

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
        G_Window.bind_all(
            "<Return>",
            lambda g: self.controller.video.close(G_Window),
        )

    def draw_graphX(self, window):
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

    def draw_graphY(self, window):
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

    def draw_graph3(self, window):
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
