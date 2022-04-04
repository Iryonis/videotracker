import tkinter as tk
from src.controllers.Controller import Controller
from src.views.view import View
from src.models.Video import Video

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Video Tracker')
        # create a view and place it on the root window
        view = View()
        # create a video model
        video = Video(view.get_window(), self.title)
        # create a controller
        controller = Controller(video, view)
        # set the controller to view
        view.setController(controller)

if __name__ == '__main__':
    app = Application()
    #app.mainloop()
