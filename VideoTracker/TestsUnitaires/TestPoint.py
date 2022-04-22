import sys, os, unittest

# Import Point() :
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.models.Point import Point


class Test_Point(unittest.TestCase):
    def setUp(self):
        self.Point = Point()
        self.X1 = 6
        self.Y1 = 7
        self.X2 = -5
        self.Y2 = 58
        self.X3 = 75
        self.Y3 = -8
        self.X4 = 5.7
        self.Y4 = 9.9
        self.X5 = "g"
        self.Y5 = "o"

    def test_setXPetitEntier(self):
        self.Point.setX(self.X1)
        self.assertTrue(self.Point.getX() is self.X1)

    def test_setYPetitEntier(self):
        self.Point.setY(self.Y1)
        self.assertTrue(self.Point.getY() is self.Y1)

    def test_XNegatif(self):
        self.Point.setX(self.X2)
        self.assertTrue(self.Point.getX() is self.X2)

    def test_YDeuxChiffres(self):
        self.Point.setY(self.Y2)
        self.assertTrue(self.Point.getY() is self.Y2)

    def test_YNegatif(self):
        self.Point.setX(self.Y3)
        self.assertTrue(self.Point.getX() is self.Y3)

    def test_XDeuxChiffres(self):
        self.Point.setY(self.X3)
        self.assertTrue(self.Point.getY() is self.X3)

    def test_XDecimal(self):
        self.Point.setX(self.X4)
        self.assertTrue(self.Point.getX() is self.X4)

    def test_YDecimal(self):
        self.Point.setY(self.Y4)
        self.assertTrue(self.Point.getY() is self.Y4)

    def test_XLettres(self):
        self.Point.setX(self.X5)
        self.assertTrue(self.Point.getX() is self.X5)

    def test_YLettres(self):
        self.Point.setY(self.Y5)
        self.assertTrue(self.Point.getY() is self.Y5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
