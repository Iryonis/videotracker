from .Point import Point


class dataPoints:
    def __init__(self):
        self.point = Point()

    def create_tab(self, time):
        self.time = time
        print(self.time)
        self.tabPts = [0 for i in range(int(100))]
        self.tabTmp = [0 for i in range(int(100))]

    def tabPoints(self, i, x, y):
        self.tabPts[i] = Point(x, y)
        self.tabTmp[i] = int(self.time + i)
        print(self.tabPts[0].x, self.tabPts[0].y)
