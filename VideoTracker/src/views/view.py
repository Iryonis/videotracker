from tkinter import *
import PIL.Image, PIL.ImageTk
from tkinter import *

class Application():


    def __init__(self):

        self.fenetre = Tk()
        self.fenetre.title("Video Tracker")
        self.label = Label(self.fenetre, text="Ouvrez une vidéo en appuyant sur le menu Fichier en haut à gauche ou avec le raccourci clavier Ctrl + O.", width='100', height = '20', font = ('Arial', 15), bg='ivory')
        self.label.pack(side=TOP, padx=5, pady=5)



        Button(self.fenetre, text ="Définir l'échelle",font = ('calibri', 10, 'bold', 'underline')).pack(side=RIGHT, padx=5, pady=5)
        Button(self.fenetre, text ='|<<',font= 'calibri').pack(side=LEFT, padx=5, pady=5)
        Button(self.fenetre, text ="|<",font= 'calibri').pack(side=LEFT, padx=5, pady=5)
        def changeText():
            if(btn['text']=='||'):
                btn['text']='>'
            else:
                btn['text']='||'
        btn = Button(self.fenetre, text='||',font= 'calibri', command=changeText)
        btn.pack(side=LEFT, padx=5, pady=5)
        Button(self.fenetre, text ='>|',font= 'calibri').pack(side=LEFT, padx=5, pady=5)
        Button(self.fenetre, text ='>>|',font= 'calibri').pack(side=LEFT, padx=5, pady=5)


        self.fenetre.mainloop()



if __name__ == '__main__':
    app = Application()
    