from tkinter import filedialog as fd
import os
import platform


class FileRepo:
    def __init__(self):
        pass

    def exportDataToString(self, dataTimes, dataPoints):
        text = ""
        delim = ";"
        for i in range(len(dataTimes)):
            text += (
                str(dataTimes[i])
                + delim
                + str(dataPoints[i].getX())
                + delim
                + str(dataPoints[i].getY())
                + " \n"
            )
        return text

    def exportDataToCsv(self, dataTimes, dataPoints, filepath):
        try:
            file = open(filepath, mode="w")
            text = self.exportDataToString(self, dataTimes, dataPoints)
            file.write(text)
            file.close()
        except IOError:
            print("Erreur lors de la creation du fichier, veuillez reessayer.\n")

    def saveAs(self, dataTimes, dataPoints):
        if platform.system() == "Windows":
            self.nextPath = "/VideoTracker/resources/resultats"
        elif platform.system() == "Linux":
            self.nextPath = "/resources/resultats"
        self.filepath = fd.asksaveasfilename(
            initialdir=os.getcwd() + self.nextPath,
            initialfile="releve_de_points.csv",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
        )
        self.exportDataToCsv(self, dataTimes, dataPoints, self.filepath)

    def save(self, dataTimes, dataPoints):
        try:
            self.exportDataToCsv(self, dataTimes, dataPoints, self.filepath)
        except:
            self.saveAs(self, dataTimes, dataPoints)
