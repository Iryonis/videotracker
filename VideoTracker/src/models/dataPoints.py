from .Point import *


class dataPoints:
    def __init__(self):
        pass

    def create_tab(self, totTime):
        self.totTime = totTime
        self.tabPts = [0 for i in range(int(self.totTime))]
        self.tabTmp = [0 for i in range(int(self.totTime))]

    def tab_points(self, x, y, time):
        self.tabPts[time] = Point(x, y)
        self.tabTmp[time] = int(time)

    def get_tabPts(self):
        return self.tabPts

    def get_tabTmp(self):
        return self.tabTmp
