import unittest
import cv2
import PIL.Image, PIL.ImageTk


class Test_Video(unittest.TestCase):
    def setUp(self):
        pass

    def open_file(self):
        self.pause = True
        self.cap = cv2.VideoCapture(
            "C:/Users/Guilhem/ProjetVideoTracker/VideoTracker/resources/videos/Jamy.mp4"
        )
        self.delay = 15
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    def get_frame(self):
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except:
            print("The video has come to an end.")

    def play_video(self):
        try:
            ret, frame = self.get_frame()
            if (not self.pause) and ret:
                self.window.after(int(self.delay), self.play_video)
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        except:
            print("play_video - Error")

    def test_FirstFrame(self):
        self.pause = False
        self.trueFrame = 0
        self.frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.assertEqual(self.trueFrame, self.frame)


if __name__ == "__main__":
    unittest.main(verbosity=2)
