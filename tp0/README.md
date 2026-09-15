# TP0 - Python : bases et structures de données

Ce dossier contient plusieurs exercices de programmation Python visant à pratiquer les structures de base : tuples, ensembles, dictionnaires et tests unitaires.

## Contenu du dossier

### `exercice3.py`
Exercice sur les tuples.

- `afficher_releve(capteur)`: affiche le relevé d’un capteur sous forme lisible.
- `recalibrer(releve, capteur, valeur)`: modifie la valeur associée à un capteur donné dans une liste de relevés.
- Le fichier contient aussi des assertions de vérification.

### `ensembles.py`
Exercice sur les ensembles (`set`).

- `robots_double_mission(exploration, transport)`: retourne les robots présents dans les deux missions.
- `robots_toutes_missions(exploration, transport)`: retourne l’union des robots.
- `robots_exploration_seulement(exploration, transport)`: retourne les robots de l’exploration uniquement.
- `ajouter_robot_mission(...)` et `retirer_robot_mission(...)`: ajout/suppression d’un robot dans un ensemble.

### `dictionnaires.py`
Exercice sur les dictionnaires.

- `quantite_piece(liste, modele, piece)`: retourne la quantité d’une pièce pour un modèle donné.
- `consommer_piece(...)`: diminue la quantité d’une pièce consommée.
- `ajouter_modele(...)`: ajoute un nouveau modèle au stock.
- `total_pieces(stock)`: calcule le total des pièces pour tous les modèles.

### `qualite.py`
Exercice sur le calcul de coût de déplacement selon le type de terrain.

- `cout_deplacement_propre(type, x1, y1, x2, y2)`: calcul le coût de déplacement en fonction du terrain.

### `Exercice8`
Fichier dédié à un exercice de gestion de stock de pièces pour plusieurs modèles de robots.

- Gestion de dictionnaires imbriqués.
- Ajout de modèles.
- Consommation de pièces.
- Calcul du total des pièces disponibles.

### `tests.py`
Fichier de tests unitaires.

- Il vérifie le bon fonctionnement de plusieurs fonctions de ce dossier.
- Utilise le module `unittest`.

## Fichiers de configuration

- `.gitignore`: règles Git pour ignorer certains fichiers.
- `python.gitignore`: configuration spécifique pour les projets Python.

## Objectif général

Ce TP permet d’apprendre à manipuler les structures fondamentales de Python :

- tuples
- listes
- ensembles
- dictionnaires
- assertions
- tests unitaires

## Exemple d’exécution

Pour lancer les tests du dossier :

```bash
python3 tests.py
```

Pour lancer un fichier d’exercice spécifique :

```bash
python3 exercice3.py
```
