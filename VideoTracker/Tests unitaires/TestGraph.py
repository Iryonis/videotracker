import unittest
import sys
import os
import platform

# Import Graph.py :
if platform.system() == "Windows":
    nextPathA = "/VideoTracker/src/models"
elif platform.system() == "Linux":
    nextPathA = "/src/models"
sys.path.append(os.getcwd() + nextPathA)
from Graph import Graph

# Pour le moment, le test n'est pas très intéressant étant donné que les données utilisées pour contruire le graphique
# sont des données définies manuellement lors de la programmation ; ce test unitaire prendra plus de sens lorsque les
# points seront récupérés sur la vidéo.


class Test_Graph(unittest.TestCase, Graph):
    def setUp(self):
        self.graph = Graph()
        if platform.system() == "Windows":
            self.nextPath = "/VideoTracker/resources/resultats"
        elif platform.system() == "Linux":
            self.nextPath = "/resources/resultats"
        self.path = os.getcwd() + self.nextPath + "/releve_de_points.csv"

    def test_retrieveData_tTrue(self):
        self.graph.retrieveData(self.path)
        t = self.graph.window_t()
        true_t = [0, 1, 2]
        self.assertEqual(t, true_t)

    def test_retrieveData_xTrue(self):
        self.graph.retrieveData(self.path)
        x = self.graph.window_x()
        true_x = [0.0, 1.5, 111.0]
        self.assertEqual(x, true_x)

    def test_retrieveData_yTrue(self):
        self.graph.retrieveData(self.path)
        y = self.graph.window_y()
        true_y = [4.0, 5.0, -6.0]
        self.assertEqual(y, true_y)

    def test_retrieveData_tFalse(self):
        self.graph.retrieveData(self.path)
        t = self.graph.window_t()
        false_t = [0, 2, 1]
        self.assertNotEqual(t, false_t)

    def test_retrieveData_xFalse(self):
        self.graph.retrieveData(self.path)
        x = self.graph.window_x()
        false_x = [0, 1.7, 111]
        self.assertNotEqual(x, false_x)

    def test_retrieveData_yFalse(self):
        self.graph.retrieveData(self.path)
        y = self.graph.window_y()
        false_y = [4, 5, 6]
        self.assertNotEqual(y, false_y)


if __name__ == "__main__":
    unittest.main(verbosity=2)
