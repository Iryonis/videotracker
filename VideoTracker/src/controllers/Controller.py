import tkinter as tk
#import sys
#sys.path.append("../")
from ..models.Video import Video
from ..views.view import View
#sys.path.pop()

class Controller:

    def __init__(self, video, view):
        print("Controller")
        self.video = video
        self.view = view

    def get_video(self):
        print("get_video")
        self.video.open_file()
        self.video.open_window()

    def open_window(self):
        self.view.open_window()
