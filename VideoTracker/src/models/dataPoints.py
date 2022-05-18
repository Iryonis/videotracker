from .Point import *


class dataPoints:
    def __init__(self):
        pass

    def create_tab(self, totTime):
        self.totTime = totTime
        self.tabPts = [0 for i in range(int(self.totTime))]
        self.tabTmp = [0 for i in range(int(self.totTime))]

    def tab_points(self, i, x, y, time):
        self.tabPts[i] = Point(x, y)
        self.tabTmp[i] = int(time)
        print(self.tabTmp[i], self.tabPts[i].x, self.tabPts[i].y)

    def get_tabPts(self):
        return self.tabPts

    def get_tabTmp(self):
        return self.tabTmp
