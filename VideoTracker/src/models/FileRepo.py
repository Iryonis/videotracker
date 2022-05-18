from tkinter import filedialog as fd
import os


class FileRepo:
    def __init__(self):
        pass

    def export_data_to_string(self, dataTime, dataPoints, ratio):
        text = ""
        delim = ";"
        for i in range(len(dataTime)):
            if dataPoints[i] != 0:
                text += (
                    str(dataTime[i])
                    + delim
                    + str(round(dataPoints[i].getX() / ratio, 2))
                    + delim
                    + str(round(dataPoints[i].getY() / ratio, 2))
                    + " \n"
                )
                i = i + 1
        return text

    def export_data_to_csv(self, dataTime, dataPoints, filepath, ratio):
        try:
            file = open(filepath, mode="w")
            text = self.export_data_to_string(dataTime, dataPoints, ratio)
            file.write(text)
            file.close()
        except IOError:
            print("Error when creating the file, please retry.\n")

    def save_as(self, dataTime, dataPoints, ratio):
        nextPath = "/resources/resultats"
        self.filepath = fd.asksaveasfilename(
            initialdir=os.getcwd() + nextPath,
            initialfile="releve_de_points.csv",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
        )
        self.export_data_to_csv(dataTime, dataPoints, self.filepath, ratio)

    def save(self, dataTime, dataPoints, ratio):
        try:
            self.export_data_to_csv(dataTime, dataPoints, self.filepath, ratio)
        except:
            self.save_as(dataTime, dataPoints, ratio)


