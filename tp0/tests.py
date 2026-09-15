"""Exercice 7 - Test Unitaires"""
import unittest
from exercice3 import releves, recalibrer
from ensembles import robots_double_mission,ajouter_robot_mission,robots_exploration,robots_transport
from dictionnaires import consommer_piece, total_pieces, pieces_stock


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

class TestInventaire(unittest.TestCase):
    """Tests pour les fonctions consommer_piece et total_pieces"""
    def test_consommer(self):
        """Cas Usuel"""
        consommer_piece(pieces_stock, "ModeleA", "roues", 5)
        self.assertEqual(pieces_stock["ModeleA"]["roues"],35)

    def test_consommer_piece_absente(self):
        """Cas limite: la piece consommé n'est pas en quantité suffisante"""
        consommer_piece(pieces_stock, "ModeleA", "capteurs", 50)
        self.assertEqual(pieces_stock["ModeleA"]["capteurs"],25)

    def test_total_pieces(self):
        """Cas Usuel"""
        resultat = total_pieces(pieces_stock)
        self.assertEqual(resultat,{"moteurs": 17, "capteurs": 50, "roues": 75})

    def test_total_limite(self):
        """Cas Limite : stock sans modèle"""
        resultat = total_pieces({
        "ModeleA": {"moteurs": 0, "capteurs": 0, "roues": 0},
        "ModeleB": {"moteurs": 0, "capteurs": 0, "roues": 0},
        })
        self.assertEqual(resultat,{"moteurs": 0, "capteurs": 0, "roues": 0})

if __name__ == "__main__":

    unittest.main(verbosity=2)
