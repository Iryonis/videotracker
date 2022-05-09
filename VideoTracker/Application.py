import tkinter as tk
from src.controllers.Controller import Controller
from src.views.view import View
from src.models.Video import Video
from src.models.Point import Point
from src.models.FileRepo import FileRepo
from src.models.Graph import Graph
from src.models.drawPoint import drawPoint


class Application(tk.Tk):
    def __init__(self):
        view = View()
        print("View created")
        video = Video(view.get_window())
        print("Video created")
        filerepo = FileRepo()
        print("FileRepo created")
        graph = Graph()
        print("Graph created")
        dp = drawPoint(video.get_canvas())
        print("drawPoint created")
        controller = Controller(video, view, Point, filerepo, graph, dp)
        print("Controller created")
        view.setController(controller)
        graph.setController(controller)
        dp.setController(controller)
        print("Controller set for view.py, graph.py and drawPoint.py")
        view.create_interface()
        print("Interface created")
        view.open_window()


if __name__ == "__main__":
    app = Application()
