"""Exercice  6"""

def cout_deplacement_propre(type,x1,y1,x2,y2):
    """Calcul du coût de déplacement selon le type de terrain allant de x1,y1 à x2,y2"""
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if type=="R":
        cout = distance * 1
    elif type=="H":
        cout = distance * 1.5
    elif type=="S":
        cout = distance * 2
    else:
        cout = distance * 3
    return cout
