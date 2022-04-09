import tkinter as tk
from src.controllers.Controller import Controller
from src.views.view import View
from src.models.Video import Video
from src.models.Point import Point
from src.models.FileRepo import FileRepo


class Application(tk.Tk):

    def __init__(self):
        view = View()
        if view == None:
            exit(84)
        print("View created")
        video = Video(view.get_window())
        if video == None:
            exit(84)
        print("Video created")
        controller = Controller(video, view, Point, FileRepo)
        print("Controller created")
        view.setController(controller)
        print("Controller set")
        view.create_interface()
        print("Interface created")
        view.open_window()

if __name__ == '__main__':
    app = Application()
