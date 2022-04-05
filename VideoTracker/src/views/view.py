import PIL.Image, PIL.ImageTk
import tkinter as tk

def changeText(button):
    if(button['text']=='||'):
        button['text']='>'
    else:
        button['text']='||'

class View():

    def __init__(self):
        print("View.py: View created")
        try:
            self.fenetre = tk.Tk()
            self.fenetre.title("Video Tracker")
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

    def create_button_echelle(self):
        print("View.py: create_button_echelle called")
        buttonsFrame = tk.Frame(self.fenetre, bg='#FFFFFF')
        buttonsFrame.pack(side = tk.BOTTOM, fill =tk.X)
        tk.Button(buttonsFrame, text ="Définir l'échelle", command = self.load_video, font = ('calibri', 10, 'bold', 'underline',)).pack(side= tk.RIGHT, padx=5, pady=5)
        tk.Button(buttonsFrame, text ='|<<',font= ('calibri', 10, 'bold'), command = lambda: self.controller.video.play_video()).pack(side = tk.LEFT, padx=5, pady=5)
        tk.Button(buttonsFrame, text ="|<",font= ('calibri', 10, 'bold')).pack(side = tk.LEFT, padx=5, pady=5)
        button = tk.Button(buttonsFrame, text='||', font = ('calibri', 10, 'bold'))
        button.config(command = lambda :changeText(button))
        button.pack(side = tk.LEFT, padx=5, pady=5)
        tk.Button(buttonsFrame, text ='>|', font= ('calibri', 10, 'bold')).pack(side = tk.LEFT, padx=5, pady=5)
        tk.Button(buttonsFrame, text ='>>|',font= ('calibri', 10, 'bold')).pack(side = tk.LEFT, padx=5, pady=5)
        return button

    def get_window(self):
        print("View.py: get_window called")
        try:
            return self.fenetre
        except Exception as e:
            print("View.py: ERROR detected on getting window: [", e, "]")
            return None

    def load_video(self):
        print("View.py: load_video called")
        self.video.open_file
"""         except Exception as e:
            print("View.py: ERROR detected while loading a video: [", e, "]")
            return None """
