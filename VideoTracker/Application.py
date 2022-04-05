import tkinter as tk
from src.controllers.Controller import Controller
from src.views.view import View
from src.models.Video import Video

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Video Tracker')
        view = View()
        if view == None:
            exit(84)
        print("View created")
        video = Video(view.get_window())
        if video == None:
            exit(84)
        print("Video created")
        controller = Controller(video, view)
        print("Controller created")
        view.setController(controller)
        print("Controller set")
        view.create_button_echelle()
        print("Button echelle created")
        controller.open_window()

if __name__ == '__main__':
    app = Application()
