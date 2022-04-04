import tkinter as tk
#import sys
#sys.path.append("../")
from ..models.Video import Video
from ..views.view import View
#sys.path.pop()

class Controller:

    def __init__(self, video, view):
        self.video = video
        self.view = view

    def get_video(self):
        self.video.open_file()
