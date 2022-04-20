import unittest
import sys
import os
import platform

if platform.system() == "Windows":
    nextPathA = "/VideoTracker/src/models"
elif platform.system() == "Linux":
    nextPathA = "/src/models"
sys.path.append(os.getcwd() + nextPathA)
from Graph import Graph

sys.path.pop()


class Test_Video(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_windowGraph(self):
        self.graph.windowGraph(
            "C:/Users/Guilhem/ProjetVideoTracker/VideoTracker/resources/resultats/releve_de_points.csv"
        )
        print(self.t)
        self.assertEqual()


if __name__ == "__main__":
    unittest.main(verbosity=2)
