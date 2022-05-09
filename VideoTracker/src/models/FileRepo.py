from tkinter import filedialog as fd
import os, platform


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
            text = self.exportDataToString(dataTimes, dataPoints)
            file.write(text)
            file.close()
        except IOError:
            print("Error when creating the file, please retry.\n")

    def saveAs(self, dataTimes, dataPoints):
        nextPath = "/resources/resultats"
        self.filepath = fd.asksaveasfilename(
            initialdir=os.getcwd() + nextPath,
            initialfile="releve_de_points.csv",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
        )
        self.exportDataToCsv(dataTimes, dataPoints, self.filepath)

    def save(self, dataTimes, dataPoints):
        try:
            self.exportDataToCsv(dataTimes, dataPoints, self.filepath)
        except:
            self.saveAs(dataTimes, dataPoints)
