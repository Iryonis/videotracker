from .Point import Point
import csv
from tkinter import filedialog as fd

class FileRepo:
    def exportDataToString(self, dataTimes, dataPoints):
        text = ""
        delim = ";"
        for i in range(len(dataTimes)):
            text += str(dataTimes[i])  + delim + str(dataPoints[i].getX()) + delim + str(dataPoints[i].getY()) + " \n"
        return text

    def exportDataToCsv(self, dataTimes, dataPoints):
        try:
            fichier = open("releve_de_points.csv", mode='w')
            res = self.exportDataToString(dataTimes, dataPoints)
            fichier.write(res)
            fichier.close()
        except IOError:
            print("Erreur lors de la creation du fichier, veuillez reessayer.\n")

    def save_as():
        dirName = fd.askdirectory()
        return dirName



