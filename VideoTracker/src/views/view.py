import tkinter as tk
import platform
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class View:
    def __init__(self):
        print("View.py: View created")
        try:
            self.fenetre = tk.Tk()
            self.fenetre.configure(bg="black")
            self.fenetre.withdraw
            self.fenetre.title("VideoTracker - Final build")
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
            command=lambda: self.controller.play_or_pause_controller(),
        )
        self.fenetre.bind_all(
            "<Control-Key-p>", lambda p: self.controller.play_or_pause_controller()
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
        menuEdit = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit", menu=menuEdit)
        menuEdit.add_command(
            label="Show values...",
            underline=5,
            accelerator="(Ctrl + V)",
            command=lambda: self.go_to_SV(),
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

        menuHelp.add_command(
            label="Shortcuts's list",
            underline=14,
            accelerator="(Ctrl + I)",
            command=lambda: self.go_to_shortcut(),
        )
        self.fenetre.bind_all("<Control-Key-i>", lambda i: self.go_to_shortcut())

        menuHelp.add_command(
            label="About Us",
            accelerator="(Ctrl + U)",
            underline=7,
            command=lambda: self.go_to_about_us(),
        )
        self.fenetre.bind_all("<Control-Key-u>", lambda u: self.go_to_about_us())

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
            command=lambda: self.controller.first_frame_controller(button),
        ).pack(side=tk.LEFT, padx=30, pady=7)
        self.fenetre.bind_all(
            "<Control-Key-b>", lambda b: self.controller.first_frame_controller(button)
        )
        tk.Button(
            buttonsFrame,
            text="|<",
            bg="#FF9F45",
            activebackground="#ADDAEF",
            width=10,
            font=("calibri", 20, "bold"),
            command=lambda: self.controller.previous_frame_controller(button),
        ).pack(side=tk.LEFT, padx=30, pady=7, fill="none", expand=True)
        self.fenetre.bind_all(
            "<Left>", lambda l: self.controller.previous_frame_controller(button)
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
            command=lambda: self.controller.next_frame_controller(button),
        ).pack(side=tk.LEFT, padx=30, pady=7, fill="none", expand=True)
        self.fenetre.bind_all(
            "<Right>", lambda r: self.controller.next_frame_controller(button)
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
                    command=lambda: self.controller.choose_value_controller(
                        entry, F_Window
                    ),
                ).pack(side=tk.BOTTOM, padx=30, pady=7)
                F_Window.bind_all(
                    "<Return>",
                    lambda g: self.controller.choose_value_controller(entry, F_Window),
                )
        except:
            messagebox.showerror(
                "Error - Go to frame...", "You haven't opened a video yet."
            )

    def go_to_shortcut(self):
        messagebox.showinfo(
            "Shortcuts's list :",
            "You can find all the shortcuts by pressing the key 'Alt' :\n  - Ctrl + o => Open the video \n  - Ctrl + p => Play the video \n  - Ctrl + a => Save as \n  - Ctrl + s => Save (if you have already saved one time) \n  - Ctrl + q => Quit the application \n"
            + "  - Ctrl + v => Show values \n  - Ctrl + g => Go to frame \n  - Ctrl + e => Go to last frame \n  - Ctrl + x => Plot the graph x(t) \n  - Ctrl + y => Plot the graph y(t) \n  - Ctrl + t => Plot the graph y(x) \n"
            + "  - Ctrl + i => Help \n  - Ctrl + u => About us \n  - Ctrl + b => Start from the beginning button \n  - Left => Previous frame button \n  - Space => Play or Pause button \n  - Right => Next frame button \n \n"
            + "After pressing the 'Set up scale' button, you will be able to define a scale by right-clicking two times on the video. Then, with the key's combinaison 'Ctrl + left click', you will have to put a marker to define a new origin."
            + "To finish, by clicking on the 'Click to place the points' button, a left click on the video will put a point and allow you to track the object you want to track.\nDon't forget to stop the aiming when you want to save your work.",
        )

    def go_to_about_us(self):
        messagebox.showinfo(
            "About us",
            "Project VideoTracker - Final build\nAll rights reserved - 2022\n \n"
            + "We are Léo and Guilhem, two students at the University of Bordeaux, France.\n"
            + "We had 3 months to do the VideoTracker as a year-end project.\n This project allowed us to deepen our knowledge in the field of computer science,"
            + "more precisely in coding with Python, and with certain modules such as Tkinter or Opencv.",
        )

    def go_to_SV(self):
        Pts = self.controller.dp.dpts.get_tabPts()
        Tmp = self.controller.dp.dpts.get_tabTmp()
        Text = "Time\tX pos'\tY pos'\n \n"
        for i in range(len(Tmp)):
            if Tmp[i] != 0:
                Text += (
                    str(Tmp[i])
                    + "\t"
                    + str(Pts[i].getX())
                    + "\t"
                    + str(Pts[i].getY())
                    + "\n"
                )
        messagebox.showinfo("Array of points (in pixels)", Text)

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
