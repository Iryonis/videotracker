from tkinter import *
import PIL.Image, PIL.ImageTk
from tkinter import *

def changeText(button):
    if(button['text']=='||'):
        button['text']='>'
    else:
        button['text']='||'

class View():

    def __init__(self):
        print("View.py: View created")
        try:
            texte = "Ouvrez une vidéo en appuyant sur le menu Fichier en haut"
            texte += " à gauche ou avec le raccourci clavier Ctrl + O."
            self.fenetre = Tk()
            self.fenetre.title("Video Tracker")
            self.label = Label(self.fenetre, text=texte, width='100', height='20',
            font=('Arial', 15), bg='ivory')
            self.label.pack(side=TOP, padx=5, pady=5)
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

    def load_video(self):
        print("View.py: load_video called")
        try:
            self.controller.get_video()
        except Exception as e:
            print("View.py: ERROR detected while loading a video: [", e, "]")
            return None

    def create_button_echelle(self):
        print("View.py: create_button_echelle called")
        Button(self.fenetre, text ="Définir l'échelle", command = self.load_video, font = ('calibri', 10, 'bold', 'underline',)).pack(side=RIGHT, padx=5, pady=5)
        Button(self.fenetre, text ='|<<',font= 'calibri').pack(side=LEFT, padx=5, pady=5)
        Button(self.fenetre, text ="|<",font= 'calibri').pack(side=LEFT, padx=5, pady=5)
        button = Button(self.fenetre, text='||',font= 'calibri')
        button.pack(side=LEFT, padx=5, pady=5)
        Button(self.fenetre, text ='>|',font= 'calibri').pack(side=LEFT, padx=5, pady=5)
        Button(self.fenetre, text ='>>|',font= 'calibri').pack(side=LEFT, padx=5, pady=5)
        return button

    def get_window(self):
        print("View.py: get_window called")
        try:
            return self.fenetre
        except Exception as e:
            print("View.py: ERROR detected on getting window: [", e, "]")
            return None
