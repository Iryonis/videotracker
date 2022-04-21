import sys
import os
import platform

if platform.system() == "Windows":
    nextPathA = "/VideoTracker/src/models"
elif platform.system() == "Linux":
    nextPathA = "/src/models"
sys.path.append(os.getcwd() + nextPathA)
from FileRepo import FileRepo
from Point import Point

sys.path.pop()
import unittest
import filecmp


class Test_FileRepo(unittest.TestCase):
    def setUp(self):
        self.Point1 = Point(0, 2)
        self.Point2 = Point(1.2, 4)
        self.Point3 = Point(1111, -4)
        self.dataTimes = [0, 1, 2]
        self.dataPoints = [self.Point1, self.Point2, self.Point3]
        self.fileCSV = FileRepo()
        self.testTrue = "0;0;2 \n1;1.2;4 \n2;1111;-4 \n"
        self.testFalse = "0;1;2\n1;3;4 2;1111;-4\n"
        if platform.system() == "Windows":
            self.nextPath = "/VideoTracker/resources/resultats"
            self.nextPathV = "/VideoTracker/TestsUnitaires"
        elif platform.system() == "Linux":
            self.nextPath = "/resources/resultats"
            self.nextPathV = "/TestsUnitaires"

    # Test pour exportDataToString :

    def test_exportDataToStringTrue(self):
        self.text = self.fileCSV.exportDataToString(self.dataTimes, self.dataPoints)
        self.assertEqual(self.text, self.testTrue)

    def test_exportDataToStringFalse(self):
        self.text = self.fileCSV.exportDataToString(self.dataTimes, self.dataPoints)
        self.assertNotEqual(self.text, self.testFalse)

    # Test pour exportDataToCsv :

    def test_exportDataToCsvTrue(self):
        filepath = os.getcwd() + self.nextPath + "/releve_de_points.csv"
        self.fileCSV.exportDataToCsv(self.dataTimes, self.dataPoints, filepath)
        self.assertTrue(
            filecmp.cmp(
                os.getcwd() + self.nextPath + "/releve_de_points.csv",
                os.getcwd() + self.nextPathV + "/verificationtrue.csv",
            )
        )

    def test_exportDataToCsvFalse(self):
        filepath = os.getcwd() + self.nextPath + "/releve_de_points.csv"
        self.fileCSV.exportDataToCsv(self.dataTimes, self.dataPoints, filepath)
        self.assertFalse(
            filecmp.cmp(
                os.getcwd() + self.nextPath + "/releve_de_points.csv",
                os.getcwd() + self.nextPathV + "/verificationfalse.csv",
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
