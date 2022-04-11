from tkinter import filedialog as fd
import os

class FileRepo:

    def __init__(self):
        pass

    def exportDataToString(self, dataTimes, dataPoints):
        text = ""
        delim = ";"
        for i in range(len(dataTimes)):
            text += str(dataTimes[i])  + delim + str(dataPoints[i].getX()) + delim + str(dataPoints[i].getY()) + " \n"
        print("aribau")
        return text

    def exportDataToCsv(self, dataTimes, dataPoints):
        try:
            filepath = fd.asksaveasfilename(initialdir= os.getcwd()+"/VideoTracker/resources/resultats", initialfile="releve_de_points.csv", defaultextension=".csv", filetypes=[("CSV Files", '*.csv')])
            file = open(filepath, mode='w')
            text = self.exportDataToString(self, dataTimes, dataPoints)
            file.write(text)
            file.close()
        except IOError:
            print("Erreur lors de la creation du fichier, veuillez reessayer.\n")





