import PIL.Image, PIL.ImageTk
import tkinter as tk

def saveAs():
    print("Save as...")

def save():
    print("Saved")


class View():

    def __init__(self):
        print("View.py: View created")
        try:
            self.fenetre = tk.Tk()
            self.fenetre.withdraw
            self.fenetre.title("Video Tracker")
            self.fenetre.state('zoomed')
        except Exception as e:
            print("View.py: ERROR detected on init: [", e, "]")
            return None

    def open_window(self):
        print("View.py: open_window called")
        try:
            self.fenetre.mainloop()
        except Exception as e:
            print("View.py: ERROR detected on opening window: [", e, "]")
            return None

    def setController(self, controller):
        print("View.py: Controller set")
        self.controller = controller

    def create_interface(self):
        print("View.py: create_button_echelle called")
        menuBar = tk.Menu(self.fenetre)
        self.fenetre.config(menu=menuBar)
        menuFile = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Files", menu = menuFile)
        menuFile.add_command(label='Load the video', command = self.load_video)
        menuFile.add_command(label="Save as", command = saveAs)
        menuFile.add_command(label="Save", command = save)

        buttonsFrame = tk.Frame(self.fenetre, bg='#FFFFFF')
        buttonsFrame.pack(side = tk.BOTTOM, fill =tk.X)
        tk.Button(buttonsFrame, text ="Définir l'échelle", font = ('calibri', 20, 'bold', 'underline',)).pack(side= tk.RIGHT, padx=20, pady=7)
        tk.Button(buttonsFrame, text ="|<",font= ('calibri', 20, 'bold'), command = lambda: self.controller.video.previousFrame()).pack(side = tk.LEFT, padx=30, pady=7)
        button = tk.Button(buttonsFrame, text='>', font = ('calibri', 20, 'bold'))
        button.config(command = lambda: self.controller.video.play_or_pause(button))
        button.pack(side = tk.LEFT, padx=10, pady=7)
        tk.Button(buttonsFrame, text ='>|', font= ('calibri', 20, 'bold'), command = lambda: self.controller.video.nextFrame()).pack(side = tk.LEFT, padx=30, pady=7)
        return button

    def get_window(self):
        print("View.py: get_window called")
        try:
            return self.fenetre
        except Exception as e:
            print("View.py: ERROR detected on getting window: [", e, "]")
            return None

    def load_video(self):
        print("View.py: open_file called")
        self.controller.video.open_file()
"""         except Exception as e:
            print("View.py: ERROR detected while loading a video: [", e, "]")
            return None """
