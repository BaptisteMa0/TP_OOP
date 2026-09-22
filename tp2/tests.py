import unittest
from habitant import Habitant, Adulte, Enfant

h1 = Adulte("Aldric", 25, "Rue A", {"vaches": 3})

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
    



if __name__ == "__main__":
    unittest.main(verbosity=2)