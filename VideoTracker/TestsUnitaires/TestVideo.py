import unittest
import tkinter as tk
import cv2
import sys
import os
import platform

# Import Video.py :
if platform.system() == "Windows":
    pathA = "/VideoTracker/src/models"
elif platform.system() == "Linux":
    pathA = "/src/models"
else:
    pathA = "/VideoTracker/src/models"
sys.path.append(os.getcwd() + pathA)
from Video import Video


class Test_Video(unittest.TestCase):
    def setUp(self):
        window = tk.Toplevel()
        self.video = Video(window)
        if platform.system() == "Windows":
            self.filename = os.getcwd() + "/VideoTracker/resources/videos/jamy.mp4"
        elif platform.system() == "Linux":
            self.filename = os.getcwd() + "/resources/videos/jamy.mp4"
        self.button = tk.Button

    # Test pour vérifier que la première frame est bien affichée au chargement de la vidéo :

    def test_FirstFrame(self):
        self.video.open_file(self.filename)
        self.firstFrameTrue = 1
        self.frame = self.video.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.assertEqual(self.firstFrameTrue, self.frame)


if __name__ == "__main__":
    unittest.main(verbosity=2)
