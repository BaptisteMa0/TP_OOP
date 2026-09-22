"""Exercice 9 - Tests unitaires"""
import unittest
from habitant import Adulte, Enfant
from village import Village

h1 = Adulte("Aldric", 25, "Rue A", {"vaches": 3})
h2 = Enfant("Marin", 12, "Rue W", {"cochons": 302})


class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation."""
    def test_age_setter_valide(self):
        """Cas usuel"""
        h1.age = 27
        self.assertEqual(h1.get_age(),27)

    def test_age_setter_invalide(self):
        """Cas limite : age negatif."""
        try:
            h1.age = -5
            assert False, "une ValueError aurait du etre levee"
        except ValueError:
            pass

    def test_compte_animal_valide(self):
        """Cas usuel"""
        resultat = h1.compte_animal("vaches")
        self.assertEqual(resultat,3)

    def test_compte_animal_invalide(self):
        """Cas limite: animal non possédé"""
        resultat = h1.compte_animal("cochons")
        self.assertEqual(resultat,0)

class TestVillage(unittest.TestCase):
    """Tests pour la classe Village"""
    def test_composition(self):
        """Cas usuel"""
        ville1 = Village("ville1")
        ville1.ajouter_habitant_composition("Joe", 23, "Rue canard")
        self.assertEqual(ville1.get_habitants()[0].get_nom(), "Joe")

    def test_agregation(self):
        """Cas Usuel"""
        ville2 = Village("ville2")
        ville2.ajouter_habitant_agregation(h1)
        self.assertEqual(ville2.get_habitants()[0].get_nom(),"Aldric")

    def test_agregation_limite(self):
        """Cas limite : même habitant dans 2 villages"""
        ville1 = Village("ville1")
        ville2 = Village("ville2")
        ville1.ajouter_habitant_agregation(h1)
        ville2.ajouter_habitant_agregation(h1)
        self.assertEqual(ville2.get_habitants()[0].get_nom(),ville1.get_habitants()[0].get_nom())

class TestHeritage(unittest.TestCase):
    """Tests pour le calcul de retraite et la création d'un enfant"""
    def test_retraite_adulte(self):
        """Cas Usuel"""
        resultat = h1.calcul_nombre_annee_avant_retraite()
        self.assertEqual(resultat,62-27)

    def test_retraite_enfant(self):
        """Cas limte: Calcul retraite pour un enfant"""
        resultat = h2.calcul_nombre_annee_avant_retraite()
        self.assertEqual(resultat,"enfant")

    def test_enfant(self):
        """Test de la création d'un enfant de plus de 18 ans"""
        try:
            Enfant("Jacques",32,"Rue du potimarron")
            assert False, "une ValueError aurait du etre levee"
        except ValueError:
            pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
