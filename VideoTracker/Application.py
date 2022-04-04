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
        if view == None:
            exit(84)
        print("View created")
        # create a video model
        video = Video(view.get_window(), self.title)
        if video == None:
            exit(84)
        print("Video created")
        # create a controller
        controller = Controller(video, view)
        print("Controller created")
        # set the controller to view
        view.setController(controller)
        print("Controller set")
        view.create_button_echelle()
        print("Button echelle created")
        controller.open_window()

if __name__ == '__main__':
    app = Application()
    #app.mainloop()
