import csv


class Graph:
    def __init__(self):
        pass

    def retrieveData(self, filename):
        # Récupère les données des colonnes 0, 1 et 2
        self.t = []
        self.x = []
        self.y = []
        with open(filename, "r") as headers:
            my_reader = csv.reader(headers, delimiter=";")
            for col in my_reader:
                self.t += [col[0]]
                self.x += [col[1]]
                self.y += [col[2]]
        self.t = [int(i) for i in self.t]
        self.x = [float(i) for i in self.x]
        self.y = [float(i) for i in self.y]

    # Fonctions pour permettre d'avoir les valeurs de t dans les autres fichiers .py
    def window_t(self):
        return self.t

    def window_x(self):
        return self.x

    def window_y(self):
        return self.y
