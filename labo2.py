from datetime import datetime

def age(_annee_naissance_):
    return "Votre âge est " + str(datetime.now().year - _annee_naissance_) + "ans ."

def salutations(_nom_):
    return "Bonjour " + _nom_ + "."

