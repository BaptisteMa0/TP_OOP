"""Exercice 3 - Classe Habitant & Exercice 4 - Encapsulation"""
from multipledispatch import dispatch
from abc import ABC,abstractmethod



class Habitant(ABC):
    """Classe Habitant reprenant son adresse, son age, son nom et ses animaux"""
    def __init__(self, nom, age, adresse, animaux=None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        if animaux is not None:
            self.animaux = animaux
        else:
            self.animaux = {}

    #Accesseurs
    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_adresse(self):
        return self.__adresse

    def get_animaux(self):
        return self.__animaux

    #Mutateurs
    def set_nom(self,nom):
        self.__nom = nom

    def set_age(self,age):
        self.__age = age

    def set_adresse(self,adresse):
        self.__adresse = adresse

    def set_animaux(self,animaux):
        self.__animaux = animaux

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if 0<=age<=130:
            self.__age = age
        else:
            raise ValueError("L'age doit être compris en 0 et 130")

    #méthodes
    def affichage_adresse(self):
        """Affiche l'adresse de l'habitant dans le terminal"""
        print(f"{self.__nom} habite a {self.__adresse}")

    def compte_animal(self,animal):
        """Renvoie le nombre de "Animal" que l'habitant possede"""
        if animal in self.__animaux:
            return self.__animaux[animal]
        return 0

    #Exercice 7
    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        age_retraite = 62
        if self.age >= age_retraite:
            return "Déjà à la retraite"
        else:
            return age_retraite - self.age

#Exercice 6
@dispatch(object,str)
def set_info(habitant,nom):
    """Surcharge pour str"""
    habitant.set_nom(nom)

@dispatch(object,str,int)
def set_info(habitant,nom,age):
    """Surcharge pour str et int"""
    habitant.set_nom(nom)
    habitant.set_age(age)


#h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
""" 
#TESTS EXERCICE 3

assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"

#TESTS EXERCICE 4
h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass



#TESTS EXERCICE 6

h2 = Habitant("Bob", 40, "Rue C")
set_info(h2, "Robert") # met a jour le nom seulement
set_info(h2, "Robert", 41) # met a jour le nom et l’age
"""