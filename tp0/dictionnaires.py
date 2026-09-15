"""Exercice 5"""
#Question1
def quantite_piece(liste,modele,piece):
    """Renvoie la quantite d'une piece selon un modele"""
    return liste[modele][piece]

#Question2
def consommer_piece(liste,modele,piece,val):
    """retire la quantite d'une piece consommé selon un modele"""
    if liste[modele][piece] > val:
        liste[modele][piece] -= val

def ajouter_modele(liste,nom,moteurs,capteurs,roues):
    """ajoute la quantite d'une piece consommé selon un modele"""
    liste[nom] = {"moteurs": moteurs, "capteurs": capteurs, "roues": roues}

def total_pieces(stock):
    """Renvoie le nombre total d'une meme piece dans une liste de modeles"""
    total = {"moteurs": 0, "capteurs": 0, "roues": 0}
    for modele in stock:
        total["moteurs"] += stock[modele]["moteurs"]
        total["capteurs"] += stock[modele]["capteurs"]
        total["roues"] += stock[modele]["roues"]
    return total


pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10


consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

ajouter_modele(pieces_stock, "ModeleC",moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}

totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}
