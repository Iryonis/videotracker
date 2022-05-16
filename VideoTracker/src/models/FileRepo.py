from tkinter import filedialog as fd
import os


class FileRepo:
    def __init__(self):
        pass

    def cutting_tab(self, dataTime, dataPoints):
        new_dataTime = []
        new_dataPoints = []
        for i in range(len(dataTime)):
            if dataTime[i] != 0 and dataTime[i - 1] != 0:
                new_dataTime[i] = dataTime[i]
            if dataPoints[i] != (0, 0) and dataPoints[i - 1] != (0, 0):
                new_dataPoints[i].x = dataPoints[i].x
                new_dataPoints[i].y = dataPoints[i].y
        self.exportDataToString(new_dataTime, new_dataPoints)

    def exportDataToString(self, dataTime, dataPoints):
        text = ""
        delim = ";"
        for i in range(len(dataTime)):
            text += (
                str(dataTime[i])
                + delim
                + str(dataPoints[i].getX())
                + delim
                + str(dataPoints[i].getY())
                + " \n"
            )
        return text

    def exportDataToCsv(self, dataTime, dataPoints, filepath):
        try:
            file = open(filepath, mode="w")
            text = self.exportDataToString(dataTime, dataPoints)
            file.write(text)
            file.close()
        except IOError:
            print("Error when creating the file, please retry.\n")

    def saveAs(self, dataTime, dataPoints):
        nextPath = "/resources/resultats"
        self.filepath = fd.asksaveasfilename(
            initialdir = os.getcwd() + nextPath,
            initialfile = "releve_de_points.csv",
            defaultextension = ".csv",
            filetypes = [("CSV Files", "*.csv")],
        )
        self.exportDataToCsv(dataTime, dataPoints, self.filepath)

    def save(self, dataTime, dataPoints):
        try:
            self.exportDataToCsv(dataTime, dataPoints, self.filepath)
        except:
            self.saveAs(dataTime, dataPoints)
