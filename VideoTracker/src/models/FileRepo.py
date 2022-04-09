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
            filepath = fd.asksaveasfilename(initialdir= '~/VideoTracker/VideoTracker/resources', initialfile="releve_de_points", filetypes=[("CSV Files", '*.csv')])
            file = open(filepath, mode='w')
            res = self.exportDataToString(dataTimes, dataPoints)
            file.write(res)
            file.close()
        except IOError:
            print("Erreur lors de la creation du fichier, veuillez reessayer.\n")





