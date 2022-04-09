import tkinter as tk

class Controller:

    def __init__(self, video, view, point, filerepo):
        print("Controller")
        self.video = video
        self.view = view
        self.point = point
        self.filerepo = filerepo
