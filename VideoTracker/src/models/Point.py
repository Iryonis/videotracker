class Point:
    def setController(self, controller):
        print("Graph.py: Controller set")
        self.controller = controller

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
