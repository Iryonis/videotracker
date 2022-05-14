from .Video import Video
from .Point import Point


class dataPoints:
    def __init__(self):
        self.point = Point()

    def create_tab(self):
        self.tabPts = [0 for i in range(int(100))]
        self.tabTmp = [0 for i in range(int(100))]

    def tabPoints(self, i, x, y):
        for i in range(int(100)):
            self.tabPts[i] = self.point(x, y)
            self.tabTmp[i] = Video.getTime() + i
            print(self.tabPts)
