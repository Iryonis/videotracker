from .Point import Point


class dataPoints:
    def __init__(self):
        pass

    def create_tab(self, time, totTime):
        self.time = time
        self.totTime = totTime
        self.tabPts = [0 for i in range(int(self.totTime))]
        self.tabTmp = [0 for i in range(int(self.totTime))]

    def tabPoints(self, i, x, y):
        self.tabPts[i] = Point(x, y)
        self.tabTmp[i] = int(self.time + i)
        print(self.tabPts[i])

    def get_tabPts(self):
        return self.tabPts

    def get_tabTmp(self):
        return self.tabTmp
