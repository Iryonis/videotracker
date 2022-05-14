from .Video import Video
from .Point import Point
from ..views.view import View


class dataPoints:
    def __init__(self, vL):
        view = View()
        self.video = Video(view.get_window())
        self.point = Point()
        self.videoLenght = vL

    def create_tab(self):
        self.tabPts = [0 for i in range(int(self.videoLenght))]
        self.tabTmp = [0 for i in range(int(self.videoLenght))]

    def tabPoints(self, i, x, y):
        for i in range(int(self.videoLenght)):
                self.tabPts[i] = self.point(x, y)
                self.tabTmp[i] = self.video.getTime() + i
                print(self.tabPts)