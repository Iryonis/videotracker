import sys, os, unittest, filecmp

# Import FileRepo() and Point() :
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.models.FileRepo import FileRepo
from src.models.Point import Point


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
        self.nextPath = "/VideoTracker/resources/resultats"
        self.nextPathV = "/VideoTracker/TestsUnitaires"

    # Test pour export_data_to_string :

    def test_export_data_to_string_true(self):
        self.text = self.fileCSV.export_data_to_string(self.dataTimes, self.dataPoints)
        self.assertEqual(self.text, self.testTrue)

    def test_export_data_to_string_false(self):
        self.text = self.fileCSV.export_data_to_string(self.dataTimes, self.dataPoints)
        self.assertNotEqual(self.text, self.testFalse)

    # Test pour export_data_to_csv :

    def test_export_data_to_csv_true(self):
        filepath = os.getcwd() + self.nextPath + "/releve_de_points.csv"
        self.fileCSV.export_data_to_csv(self.dataTimes, self.dataPoints, filepath)
        self.assertTrue(
            filecmp.cmp(
                os.getcwd() + self.nextPath + "/releve_de_points.csv",
                os.getcwd() + self.nextPathV + "/verificationtrue.csv",
            )
        )

    def test_export_data_to_csv_false(self):
        filepath = os.getcwd() + self.nextPath + "/releve_de_points.csv"
        self.fileCSV.export_data_to_csv(self.dataTimes, self.dataPoints, filepath)
        self.assertFalse(
            filecmp.cmp(
                os.getcwd() + self.nextPath + "/releve_de_points.csv",
                os.getcwd() + self.nextPathV + "/verificationfalse.csv",
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
