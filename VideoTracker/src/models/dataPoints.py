from .Point import Point


class dataPoints:
    def __init__(self):
        self.point = Point()

    def create_tab(self, time, totTime):
        self.time = time
        self.totTime = totTime
        print(self.time, self.totTime)
        self.tabPts = [0 for i in range(int(self.totTime))]
        self.tabTmp = [0 for i in range(int(self.totTime))]

    def tabPoints(self, i, x, y):
        self.tabPts[i] = Point(x, y)
        self.tabTmp[i] = int(self.time + i)
        print(self.tabPts[0].x, self.tabPts[0].y)
