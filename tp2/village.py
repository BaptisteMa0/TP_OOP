"""Exercice 5 - Classe Village"""
from habitant import Habitant

class Village:
    """Crée un Village initialisé par son nom"""
    def __init__(self,nom):
        self.nom = nom
        self.habitants = []

    def ajouter_habitant_composition(self,nom,age,adresse, animaux =None):
        """Ajoute un habitant par composition"""
        self.habitants.append(Habitant(nom,age,adresse,animaux))

    def ajouter_habitant_agregation(self,habitant: Habitant):
        """Ajoute un habitant par agregation"""
        self.habitants.append(habitant)

    def afficher_habitants(self):
        """Affiche les habitants présent dans le village"""
        print(self.habitants)
        