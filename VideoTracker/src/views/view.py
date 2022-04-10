import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk

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
        menuFile.add_command(label='Load the video', underline = 1, command = self.load_video)
        self.fenetre.bind_all('<Control-Key-o>', lambda o : self.load_video())
        Point1 = self.controller.point(0,2)
        Point2 = self.controller.point(1.2,4)
        Point3 = self.controller.point(1111,-4)
        dataTimes = [0,1,2]
        dataPoints = [Point1, Point2, Point3]
        menuFile.add_command(label="Save as", underline = 1, command = lambda: self.controller.filerepo.exportDataToCsv([], dataTimes, dataPoints))
        self.fenetre.bind_all('<Control-Key-a>', lambda a : self.controller.filerepo.exportDataToCsv([], dataTimes, dataPoints))
        menuFile.add_command(label="Save", underline = 0, command = lambda: save)
        self.fenetre.bind_all('<Control-Key-s>', lambda s : save)
        menuFile.add_separator()
        menuFile.add_command(label = "Quit the app", underline = 0, command = lambda: self.controller.video.quit(self.fenetre))
        self.fenetre.bind_all('<Control-Key-q>', lambda q : self.controller.video.quit(self.fenetre))

        buttonsFrame = tk.Frame(self.fenetre, bg='#FFFFFF')
        buttonsFrame.pack(side = tk.BOTTOM, fill =tk.X)
        tk.Button(buttonsFrame, text ="Définir l'échelle", font = ('calibri', 20, 'bold', 'underline',)).pack(side= tk.RIGHT, padx=20, pady=7)
        tk.Button(buttonsFrame, text ="|<", font= ('calibri', 20, 'bold'), command = lambda: self.controller.video.previousFrame()).pack(side = tk.LEFT, padx=30, pady=7)
        button = tk.Button(buttonsFrame, text='>', font = ('calibri', 20, 'bold'))
        button.config(command = lambda: self.controller.video.play_or_pause(button))
        button.pack(side = tk.LEFT, padx=10, pady=7)
        tk.Button(buttonsFrame, text ='>|', font= ('calibri', 20, 'bold'), command = lambda: self.controller.video.nextFrame()).pack(side = tk.LEFT, padx=30, pady=7)

        timelineFrame = tk.Frame(self.fenetre)
        timelineFrame.pack(side = tk.BOTTOM, fill = tk.X)
        self.frame_number = cv2.CAP_PROP_POS_FRAMES
        self.timeline = tk.Scale(timelineFrame, orient = 'horizontal', width= 15, from_= 0, to=self.frame_number-1, showvalue=0)
        self.timeline.pack(side = tk.BOTTOM, fill= tk.X)
        self.timeline.bind("<Button-1>", lambda x: (self.controller.video.set_to_frame(self.timeline.get())))
        tk.Scale(self.fenetre, orient='horizontal', from_=0, to=10,
        resolution=0.1, tickinterval=2, length=350,
        label='Volume (db)')

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

