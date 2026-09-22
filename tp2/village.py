"""Exercice 5 - Classe Village"""
from habitant import Habitant

class Village:
    """Crée un Village initialisé par son nom"""
    def __init__(self,nom):
        self.nom = nom
        self.habitants = []

    def get_habitants(self):
        """Renvoie la liste d'habitants dans le village"""
        return self.habitants

    def ajouter_habitant_composition(self,nom,age,adresse, animaux =None):
        """Ajoute un habitant par composition"""
        self.habitants.append(Habitant(nom,age,adresse,animaux))

    def ajouter_habitant_agregation(self,habitant: Habitant):
        """Ajoute un habitant par agregation"""
        self.habitants.append(habitant)

    def afficher_habitants(self):
        """Affiche les habitants présent dans le village"""
        for i in self.habitants:
            print(i.get_nom())


pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()
pytown.afficher_habitants()

"""
Question 3:
La fonction ajouter_habitant_composition illustre une relation de composition car
on observe bien que la clase village est composé d'une classe habitant, si on supprime
La deuxième fonction illustre une agrégation car l'objet habitant Elise est indépendant
du villageVoisin.
"""
