import unittest
import cv2
import PIL.Image, PIL.ImageTk
import os
import platform


class Test_Video(unittest.TestCase):
    def setUp(self):
        pass

    def open_file(self):
        if platform.system() == "Windows":
            self.filename = os.getcwd() + "/VideoTracker/resources/videos/jamy.mp4"
        elif platform.system() == "Linux":
            self.filename = os.getcwd() + "/resources/videos/jamy.mp4"
        self.pause = True
        self.cap = cv2.VideoCapture(self.filename)
        self.delay = (1 / self.cap.get(cv2.CAP_PROP_FPS)) * 1000
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    def test_FirstFrame(self):
        self.open_file()
        self.trueFrame = 0
        self.frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.assertNotEqual(self.trueFrame, self.frame)


if __name__ == "__main__":
    unittest.main(verbosity=2)
