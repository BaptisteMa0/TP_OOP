
def quantite_piece(liste,modele,piece):
    return liste[modele][piece]

pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10