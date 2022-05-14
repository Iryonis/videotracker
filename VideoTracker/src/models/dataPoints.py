
class dataPoints:
    def __init__(self):
        self.i = 0
        self.tabPts = [0 for i in range(int(self.controller.video.videoLenght))]
        self.tabTmp = [0 for i in range(int(self.controller.video.videoLenght))]

    def setController(self, controller):
        print("dataPoints.py: Controller set")
        self.controller = controller

    def tabPoints(self, i):
        for i in range(int(self.controller.video.videoLenght)):
                self.tabPts[i] = self.controller.point.Point(self.controller.point.Point.getX(), self.controller.point.Point.getY())
                self.tabTmp[i] = self.controller.drawpoint.time + i