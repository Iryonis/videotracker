import sys
sys.path.append("../")
from src.models.FileRepo import FileRepo
from src.models.Point import Point
sys.path.pop()
import unittest
import filecmp

    
class Test_FileRepo(unittest.TestCase):
    def setUp(self):
        self.Point1 = Point(0,2)
        self.Point2 = Point(1.2,4)
        self.Point3 = Point(1111,-4)
        self.dataTime = [0,1,2]
        self.dataPoints = [self.Point1, self.Point2, self.Point3]
        self.fileCSV = FileRepo()
        self.testTrue = "0;0;2 \n1;1.2;4 \n2;1111;-4 \n"
        self.testFalse = "0;1;2\n1;3;4 2;1111;-4\n"

#Test pour exportDataToString :

    def test_exportDataToStringTrue(self):
        self.text = self.fileCSV.exportDataToString(self.dataTime, self.dataPoints)
        self.assertEqual(self.text, self.testTrue)

    def test_exportDataToStringFalse(self):
        self.text = self.fileCSV.exportDataToString(self.dataTime, self.dataPoints)
        self.assertNotEqual(self.text, self.testFalse)

#Test pour exportDataToCsv :
        
    def test_exportDataToCsvTrue(self):
        self.fileCSV.exportDataToCsv(self.dataTime, self.dataPoints)
        self.assertTrue(filecmp.cmp("releve_de_points.csv","verificationtrue.csv"))

    def test_exportDataToCsvFalse(self):
        self.fileCSV.exportDataToCsv(self.dataTime, self.dataPoints)
        self.assertFalse(filecmp.cmp("releve_de_points.csv","verificationfalse.csv"))

if __name__ == '__main__':
    print("pwar")
    unittest.main(verbosity=2)





