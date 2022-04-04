from tkinter import *
import PIL.Image, PIL.ImageTk
from tkinter import *


def create_button(fenetre, callback):
    Button(fenetre, text ="Définir l'échelle", command = callback, font = ('calibri', 10, 'bold', 'underline',)).pack(side=RIGHT, padx=5, pady=5)
    Button(fenetre, text ='|<<',font= 'calibri').pack(side=LEFT, padx=5, pady=5)
    Button(fenetre, text ="|<",font= 'calibri').pack(side=LEFT, padx=5, pady=5)
    button = Button(fenetre, text='||',font= 'calibri')
    button.pack(side=LEFT, padx=5, pady=5)
    Button(fenetre, text ='>|',font= 'calibri').pack(side=LEFT, padx=5, pady=5)
    Button(fenetre, text ='>>|',font= 'calibri').pack(side=LEFT, padx=5, pady=5)
    return button

def changeText(button):
    if(button['text']=='||'):
        button['text']='>'
    else:
        button['text']='||'

class View():

    def __init__(self):
        try:
            texte = "Ouvrez une vidéo en appuyant sur le menu Fichier en haut"
            texte += " à gauche ou avec le raccourci clavier Ctrl + O."
            self.fenetre = Tk()
            self.fenetre.title("Video Tracker")
            self.label = Label(self.fenetre, text=texte, width='100', height='20',
            font=('Arial', 15), bg='ivory')
            self.label.pack(side=TOP, padx=5, pady=5)
            self.button = create_button(self.fenetre, self.load_video)
            self.fenetre.mainloop()
        except:
            return None

    def setController(self, controller):
        self.controller = controller

    def load_video(self):
        try:
            self.controller.get_video()
        except AttributeError:
            print("controller is not set")

    def get_window(self):
        try:
            return self.fenetre
        except:
            return None

if __name__ == '__main__':
    app = View()
