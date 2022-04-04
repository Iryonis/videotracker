import cv2
import numpy as np
from tkinter import *

class Video:

    def __init__(self):


        cap = cv2.VideoCapture('jamy.mp4')
 
        if (cap.isOpened()== False):
            print("Erreur lors de l'ouverture du fichier.")
 
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
 
                cv2.imshow('Frame',frame)
 
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
 
                else:
                    break
 
        cap.release()
 
        cv2.destroyAllWindows()

Video()