#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:44:50 2023

@author: W. Morhan, A. Cesmat-Belliard
"""
import random
import time

def welcome_message_humain():
    print("""
----------------------------------------------------------------------------
            Règles du jeu de Whytoff (Humain contre Humain)
----------------------------------------------------------------------------
Règles : 1 - Deux joueurs s'affrontent.
         2 - Le jeu se déroule sur un damier.
         3 - Les joueurs jouent à tour de rôle en déplaçant un jeton.
         4 - Les mouvements possibles sont les suivants :
              - Se déplacer vers la gauche.
              - Se déplacer vers le bas.
              - Se déplacer le long d'une diagonale vers la gauche et le bas.
         5 - Le joueur qui atteint la case inférieure gauche du damier en premier
             est déclaré gagnant.

----------------------------------------------------------------------------
                           Instructions
----------------------------------------------------------------------------
1 - Le premier à rentrer son nom commence.
2 - À chaque tour, le joueur peut choisir parmi les mouvements possibles.
3 - Le jeu continue jusqu'à ce qu'un joueur atteigne la case inférieure gauche
    du damier et soit déclaré gagnant.

----------------------------------------------------------------------------
                        Que le meilleur gagne !
----------------------------------------------------------------------------
""")

################### Changement de joueur ##################
def changeJoueur(joueurActuel, joueur1, joueur2) :
    if joueur1 == joueurActuel :
        joueurActuel = joueur2
    else :
        joueurActuel = joueur1
    return joueurActuel

################### Condition de victoire ##################
def estGagnant(plateau) :
    res = False
    if plateau[0][0] == 'I' :
        res = True
    return res

################### Ajout du pion sur le plateau au debut de la partie ##################
def pionInitial(plateau) :

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

################### Afficher Plateau ##################
def affichePlateau(plateau):

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
def deplacePion(plateau):

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

################### Jeu Humain contre Humain ##################

def humainContreHumain() :

     #Affichage des règles
    welcome_message_humain() 
    time.sleep(1)

    # Saisie nom des joueurs
    joueur1 = input("Saisissez le nom du joueur 1 > ")
    joueur2 = input("Saisissez le nom du joueur 2 > ")
    joueurActuel = joueur1

    autrePartie = True
    while autrePartie :

        # Création et affichage du plateau
        lePlateau = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
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

            print("\n--Au tour de ", joueurActuel," !--")
            deplacePion(lePlateau)
            joueurActuel = changeJoueur(joueurActuel, joueur1, joueur2)
            affichePlateau(lePlateau)

        # Fin de partie, déclaration du vainqueur
        joueurActuel = changeJoueur(joueurActuel, joueur1, joueur2)
        print("\n----------------------------------------------------------------------------")
        print("Bravo", joueurActuel," ! Vous avez gagné ! ")
        print("----------------------------------------------------------------------------\n")

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

################### Jouer aux jeux ##################

humainContreHumain()
                
