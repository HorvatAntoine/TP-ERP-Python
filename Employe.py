import datetime


class Employe():

    def __init__(self, id, dateEmbauche, type):
        self.id = id
        dateEmbaucheSplit = dateEmbauche.split("/")
        self.dateEmbauche = datetime(dateEmbaucheSplit[2], dateEmbaucheSplit[1], dateEmbaucheSplit[0])
        self.type = type
