
#Question1
def afficher_releve(capteur):
    return f"Capteur {capteur[0]} : {capteur[1]} {capteur[2]}"


#QUestion2
def recalibrer(releve,capteur,valeur):
    for i in range(len(releve)):
        if releve[i][0] == capteur:
            nouveau_releve = list(releve[i])
            nouveau_releve[1] = valeur
            releve[i] = tuple(nouveau_releve)
    return releve


releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]


assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"


nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3