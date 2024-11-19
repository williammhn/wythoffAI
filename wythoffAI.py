#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:44:50 2023

@author: W. Morhan, A. Cesmat-Belliard
"""
import random
import time

def welcome_message():

    """
    Affiche le message de bienvenue et les règles du jeu de Whytoff.
    Cette fonction ne prend aucun paramètre et ne retourne rien. Elle se contente d'afficher un message sur la console.
    """

    print("""
----------------------------------------------------------------------------
            Règles du jeu de Whytoff (Humain contre Ordinateur)
----------------------------------------------------------------------------
Règles : 1 - Un joueur affronte l'ordinateur.
         2 - Le jeu se déroule sur un damier.
         3 - Les joueurs jouent à tour de rôle en déplaçant un jeton.
         4 - Les mouvements possibles sont les suivants :
              - Se déplacer vers la gauche.
              - Se déplacer vers le bas.
              - Se déplacer le long d'une diagonale vers la gauche et le bas.
         5 - L'ordinateur commence en premier.

----------------------------------------------------------------------------
                            Modes de jeu
----------------------------------------------------------------------------
        1 - Normal (L'IA part de 0)
        2 - Impossible (L'IA s'entraine contre elle-même avant de lançer la partie)
----------------------------------------------------------------------------
                           Apprentissage
----------------------------------------------------------------------------                        
Suivant qu'il gagne ou perd, l'ordinateur reçoit une récompense ou une punition.
          
""")


################### Condition de victoire ##################
def estGagnant(plateau) :

    """
    Détermine si la condition de victoire est atteinte dans le jeu.
    Args:
        plateau (list): Une liste de listes représentant l'état actuel du plateau de jeu.
    Returns:
        bool: Retourne True si la condition de victoire est atteinte, sinon False. La condition de victoire est 
        spécifique à la logique du jeu, par exemple, si un certain pion (marqué 'I') atteint une position spécifique.
    """
        
    res = False
    if plateau[0][0] == 'I' :
        res = True
    return res

################### Ajout du pion sur le plateau au debut de la partie ##################
def pionInitial(plateau) :

    """
    Place un pion initial sur le plateau de jeu en début de partie.
    Le pion est placé aléatoirement soit sur la dernière rangée soit sur la dernière colonne du plateau,
    à l'exception des coins.
    Args:
        plateau (list): Une liste de listes représentant l'état actuel du plateau de jeu. 
        Le plateau est modifié directement dans cette fonction.
    Cette fonction ne retourne rien. Elle modifie le plateau de jeu en y ajoutant un pion initial.
    """

    # Generation de la case
    extrem = random.randint(0, 1)

    if extrem == 0 :
        x = random.randint(1, len(plateau)-2)
        y = len(plateau)-1
    else :
        x = len(plateau)-1
        y = random.randint(1, len(plateau)-2)

    #Ajout du pion    
    plateau[x][y] = 'I'

################### Affiche le plateau ##################
def affichePlateau(plateau):

    """
    Affiche l'état actuel du plateau de jeu.
    Args:
        plateau (list): Une liste de listes représentant l'état actuel du plateau de jeu.
    Cette fonction ne retourne rien. Elle affiche le plateau sur la console dans un format lisible par l'utilisateur.
    """

    # Initialisation
    i = len(plateau) - 1;
    print("")

    # Condition d'arret : i >=-1
    while i > -1:
        j = 0
        print(i,end="")
        while j < len(plateau):
            print(" |", plateau[i][j],end="")
            j = j + 1
        print(" |",end="")
        print()
        i = i - 1
    k = 0
    print(" ",end="")


    while k < len(plateau):
        print("  ", k,end="")
        k = k + 1
    print("")

################### Pour que le joueur déplace le pion ##################

def deplacePionHumain(plateau):

    """
    Gère le déplacement du pion par le joueur humain.
    Args:
        plateau (list): Une liste de listes représentant l'état actuel du plateau de jeu.
    Le plateau mis à jour après le déplacement du pion humain.
    """

    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if plateau[i][j] == 'I':
                x = i
                y = j

    mv = str(input("Dans quelle sens voulez vous deplacer le pion ? (dire soit 'gauche','bas','diagonale')"))
    while ((mv != "bas" or x == 0) and (mv != "gauche" or y == 0) and (mv != "diagonale" or x == 0 or y == 0)):
        mv = str(input("Dans quelle sens voulez vous deplacer le pion ? (dire soit 'gauche','bas','diagonale')"))

    if mv == "bas":
        nbcases = int(input("De combien de cases voulez vous deplacer le pion vers la bas ?"))
        while nbcases > x or nbcases == 0:
           nbcases = int(input("De combien de cases voulez vous deplacer le pion vers la bas ?"))
        plateau[x][y] = ' '
        plateau[x-nbcases][y] = 'I'

    if mv == "gauche":
        nbcases = int(input("De combien de cases voulez vous deplacer le pion vers le gauche ?"))
        while nbcases > y or nbcases == 0 :
           nbcases = int(input("De combien de cases voulez vous deplacer le pion vers le gauche ?"))
        plateau[x][y] = ' '
        plateau[x][y-nbcases] = 'I'

    if mv == "diagonale":
        nbcases = int(input("De combien de cases voulez vous deplacer le pion vers la diagonale bas gauche ?"))
        while nbcases > x or nbcases > y or nbcases == 0:
           nbcases = int(input("De combien de cases voulez vous deplacer le pion vers la diagonale bas gauche ?"))
        plateau[x][y] = ' '
        plateau[x-nbcases][y-nbcases] = 'I'


################### Pour que le bot déplace le pion Aleatoirement ##################

def deplacerPionAleatoire(plateau):

    """
    Effectue un déplacement aléatoire de pion sur le plateau.
    Args:
        plateau (list): Une liste de listes représentant l'état actuel du plateau de jeu.
    Le plateau mis à jour après le déplacement aléatoire d'un pion.
    """

    x, y = -1, -1  # Initialisation par défaut
    estDeplace = False

    # Trouver la position du pion
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] == 'I':
                x, y = i, j

    while estDeplace == False :
        direct = random.randint(1, 3)

        # Déplacement vers le bas
        if direct == 1 and x > 0:
            nbcases = random.randint(1, x)
            plateau[x][y], plateau[x-nbcases][y] = ' ', 'I'
            estDeplace = True
        
        # Déplacement vers la gauche
        elif direct == 2 and y > 0:
            nbcases = random.randint(1, y)
            plateau[x][y], plateau[x][y-nbcases] = ' ', 'I'
            estDeplace = True

        # Déplacement en diagonale
        elif direct == 3 and x > 0 and y > 0:
            nbcases = random.randint(1, min(x, y))
            plateau[x][y], plateau[x-nbcases][y-nbcases] = ' ', 'I'
            estDeplace = True


################### Pour que le bot déplace le pion ##################

def deplacerPionOrdi(plateau, plateauBille):

    """
    Gère le déplacement du pion par l'ordinateur.
    Args:
        plateau (list): Une liste de listes représentant l'état actuel du plateau de jeu.
        plateauBille (list): Une liste de listes utilisée pour la logique de déplacement de l'ordinateur.
    Le plateau mis à jour après le déplacement du pion par l'ordinateur.
    """
    x, y = -1, -1  # Initialisation par défaut

    # Trouver la position du pion
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] == 'I':
                x, y = i, j

    plusDeBilles, a, b = 0, 0, 0

    # Parcourir à gauche
    for i in range(y - 1, -1, -1):  # y-1 car on ne va pas vers la droite
        if plusDeBilles <= plateauBille[x][i]:
            plusDeBilles = plateauBille[x][i]
            a, b = x, i

    # Parcourir en bas
    for j in range(x - 1, -1, -1):
        if plusDeBilles <= plateauBille[j][y]:
            plusDeBilles = plateauBille[j][y]
            a, b = j, y

    # Diagonale
    for d in range(1, min(x + 1, y + 1)):  # x+1 et y+1 car on ne peut pas aller au-delà des limites du plateau
        if plusDeBilles <= plateauBille[x - d][y - d]:
            plusDeBilles = plateauBille[x - d][y - d]
            a, b = x - d, y - d

    # Déplacement du pion
    if plusDeBilles > 0:
        plateau[x][y] = ' '
        plateau[a][b] = 'I'
    else:
        deplacerPionAleatoire(plateau)


def stockagePositions(plateau, poses) :
    
    for x in range(0, len(plateau)) :
        for y in range(0, len(plateau)):
            if plateau[x][y] == 'I' :
                poses[x][y] = 'X'

################### Jeu IA contre IA Boostée ##################

def entrainementContreAutreIA() :

    LesGobelets1 =  [[0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
    
    LesGobelets2 =  [[0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0]]

    nbrPartie = 0
    victoires = 0
    while nbrPartie < 100000 :

        win = 1

        # Création et affichage du plateau
        lePlateau =[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        
        LesPoses1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        
        LesPoses2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        pionInitial(lePlateau)

        
        # Séquences de la partie
        while not estGagnant(lePlateau) :

            deplacerPionOrdi(lePlateau, LesGobelets1)
            stockagePositions(lePlateau, LesPoses1)

            if estGagnant(lePlateau) :
                win = 0
                break

            deplacerPionOrdi(lePlateau, LesGobelets1)
            stockagePositions(lePlateau, LesPoses2)


        # Fin de partie, vainqueur bot adverse
        if win != 0 :
            # Punition
            for y in range(0, len(LesPoses1)) :
                for x in range(0, len(LesPoses1)):
                    if LesPoses1[y][x] =='X' :
                        if LesGobelets1[x][y] > 0 :
                            LesGobelets1[x][y] -= 1

            for y in range(0, len(LesPoses2)) :
                for x in range(0, len(LesPoses2)):
                    if LesPoses2[y][x] =='X' :
                        LesGobelets2[x][y] += 1
                     
        else :
            victoires+=1

            # Récompense
            for y in range(0, len(LesPoses1)) :
                for x in range(0, len(LesPoses1)):
                    if LesPoses1[y][x] =='X' :
                        LesGobelets1[x][y] += 1

            for y in range(0, len(LesPoses2)) :
                for x in range(0, len(LesPoses2)):
                    if LesPoses2[y][x] =='X' :
                        if LesGobelets2[x][y] > 0 :
                            LesGobelets2[x][y] -= 1
        
        nbrPartie+=1
    
    return LesGobelets1

################### Bonus : jeu avec IA entrainée ou non ##################

def jouerWythoff() :

     #Affichage des règles
    welcome_message() 
    time.sleep(1)

    # Saisie nom des joueurs
    joueur = input("Saisissez le nom du joueur : > ")
    time.sleep(1)
    print("****** Bienvenue et bonne chance ", joueur,". ******")
    time.sleep(1)

    test=True
    while test:
        mdj = input("Choisissez le mode de jeu (1, 2) : > ")
        time.sleep(1)
        if mdj == "1" :
            test=False
        elif mdj == "2":
            test=False
        else:
            print("\nChoix invalide. Recommencez !")
            time.sleep(1)

    if mdj == "1" :
        LesGobelets =  [[0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]]
    else :
        LesGobelets = entrainementContreAutreIA()
        print("****** L'IA est désormais entrainée. ******")
        time.sleep(2)

    
    autrePartie = True
    while autrePartie :
        print("****** Début de la partie ******")

        win = 1

        # Création et affichage du plateau
        lePlateau =[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        
        LesPoses = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        pionInitial(lePlateau)
        affichePlateau(lePlateau)

        
        # Séquences de la partie
        while not estGagnant(lePlateau) :

            print("\n--L'ordinateur choisis son mouvement ...--")
            deplacerPionOrdi(lePlateau, LesGobelets)
            stockagePositions(lePlateau, LesPoses)

            time.sleep(1)
            affichePlateau(lePlateau)
            time.sleep(1)

            if estGagnant(lePlateau) :
                win = 0
                break

            print("\n--Au tour de ", joueur," !--")
            time.sleep(1)
            deplacePionHumain(lePlateau)
            time.sleep(1)
            affichePlateau(lePlateau)
            time.sleep(1)

        # Fin de partie, déclaration du vainqueur
        if win != 0 :
            print("\n----------------------------------------------------------------------------")
            print("Bravo", joueur," ! Vous avez gagné ! ")
            print("----------------------------------------------------------------------------\n")
            print("L'ordinateur va recevoir une punition.\n")
            print("----------------------------------------------------------------------------\n")
            time.sleep(1)

            # Punition
            for y in range(0, len(LesPoses)) :
                for x in range(0, len(LesPoses)):
                    if LesPoses[y][x] =='X' :
                        if LesGobelets[x][y] > 0 :
                            LesGobelets[x][y] -= 1

            print("****** Les contenus des cases de stockages de l'IA ont étés modifiés ******")
            time.sleep(1)
            affichePlateau(LesGobelets)
                    
        else :
            print("\n----------------------------------------------------------------------------")
            print("L'ordinateur a gagné la partie.")
            print("----------------------------------------------------------------------------\n")
            print("L'ordinateur va recevoir une récompense.\n")
            print("----------------------------------------------------------------------------\n")
            time.sleep(1)

            # Récompense
            for y in range(0, len(LesPoses)) :
                for x in range(0, len(LesPoses)):
                    if LesPoses[y][x] =='X' :
                        LesGobelets[x][y] += 1
            print("****** Les contenus des cases de stockages de l'IA ont étés modifiés ******")
            time.sleep(1)
            affichePlateau(LesGobelets)

############ Recommencer partie ################    
        test=True
        while test:
            another_go = input("\nVoulez-vous rejouer ?[O/N]: ")
            if another_go in ("o","O"):
                autrePartie=True
                test=False
            elif another_go in ("n","N"):
                autrePartie=False
                test=False
            else:
                print("\nChoix invalide. Recommencez !")   

    print("****** Merci d'avoir joué ******") 

################### Jouer aux jeu ##################

jouerWythoff()