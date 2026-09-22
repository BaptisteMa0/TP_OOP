"""Exercice 3 - Classe Habitant"""
class Habitant:
    """Classe Habitant reprenant son adresse, son age, son nom et ses animaux"""
    def __init__(self, nom, age, adresse, animaux=None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        if animaux is not None:
            self.animaux = animaux
        else:
            self.animaux = {}

    def affichage_adresse(self):
        """Affiche l'adresse de l'habitant dans le terminal"""
        print(f"{self.nom} habite a {self.adresse}")

    def compte_animal(self,animal):
        """Renvoie le nombre de "Animal" que l'habitant possede"""
        if animal in self.animaux:
            return self.animaux[animal]
        return 0


h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"
