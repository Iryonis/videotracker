class FileRepo:
    def exportDataToString(dataTimes, dataPoints):
        text = ""
        for i in range(len(dataTimes)):
            text += str(dataTimes[i])  + str(dataPoints[i].getX()) + str(dataPoints[i].getY()) + " \n"
        return text
            
            
    def exportDataToCsv(dataTimes, dataPoints):
        fichier = open("releve_de_points.csv", mode='x')
        res = exportDataToString(dataTimes, dataPoints)
        fichier.write(res)
        fichier.close()
        
        
        
        
#Utiliser la fonction open pour créer un fichier
#Se renseigner sur try cash
        
            
        