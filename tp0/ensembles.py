"""Exercice 4 - Ensembles"""
#Question1
def robots_double_mission(exploration, transport):
    """Renvoie l'intersection des 2 ensembles"""
    return exploration & transport

def robots_toutes_missions(exploration, transport):
    """Renvoie l'union des 2 ensembles"""
    return exploration | transport

def robots_exploration_seulement(exploration, transport):
    """Renvoie la valeur de robot_Explo qui n'est pas dans robot_transport"""
    return exploration - transport


#Question2
def ajouter_robot_mission(rob, val):
    """Ajoute une mission dans le robot rob"""
    ensemble = rob
    ensemble.add(val)
    return ensemble


def retirer_robot_mission(rob, val):
    """Retire une mission val dans le robot rob"""
    ensemble = set()
    for i in rob:
        if i!=val:
            ensemble.add(i)
    return ensemble

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}


ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}
