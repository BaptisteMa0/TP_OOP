"""Exercice 7 - Test Unitaires"""
import unittest
from exercice3 import releves, recalibrer
from ensembles import robots_double_mission, ajouter_robot_mission , robots_exploration, robots_transport


class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""
    def test_recalibrer_capteur_existant(self):
        """Cas Usuel"""
        resultat = recalibrer(releves,"laser_avant", 2.40)
        self.assertEqual(resultat[0],("laser_avant", 2.40, "m"))

    def test_recalibrer_capteur_absent(self):
        """Cas limite : le capteur demande n’existe pas."""
        resultat = recalibrer(releves,"laser_inconnu", 2.40)
        self.assertEqual(resultat,releves)

class TestFlotteRobots(unittest.TestCase):
    """Tests pour les fonctions sur les flottes de robots (ensembles)"""
    def test_double_mission(self):
        """Cas Usuel"""
        resultat = robots_double_mission(robots_transport,robots_exploration)
        self.assertEqual(resultat, {"R5", "R7"})
    def test_double_mission_vide(self):
        """cas limite: robot vide"""
        resultat = robots_double_mission(robots_exploration,{"R1"})
        self.assertEqual(resultat,set())

    def test_ajout_mission(self):
        """Cas limite: robot déjà dans l'ensemble"""
        resultat = ajouter_robot_mission(robots_exploration,"R7")
        self.assertEqual(resultat,robots_exploration)
    
if __name__ == "__main__":

    unittest.main(verbosity=2)