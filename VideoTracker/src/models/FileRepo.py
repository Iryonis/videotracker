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
        print("aribau")
        return text

    def exportDataToCsv(self, dataTimes, dataPoints, filepath):
        try:
            file = open(filepath, mode="w")
            text = self.exportDataToString(self, dataTimes, dataPoints)
            file.write(text)
            file.close()
        except IOError:
            print("Erreur lors de la creation du fichier, veuillez reessayer.\n")
