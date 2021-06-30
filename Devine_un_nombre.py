# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:48:24 2021

@author: Black Shadow
"""
from random import randint


print("Bonjour, je vous présente ici un jeu de devinette sur lequel l'ordinateur genère un nombre aleatoire d'un nombre 'x' à un nombre 'y' et vous aurez la tache de le deviviner en 'z' nombres des tentatives")

nom = input("Veuillez saisir votre nom S.V.P : ")
nom = str(nom)

debut = input("Saisir le nombre de début de l'interval : ")
debut = int(debut)

fin = input("Saisir le nombre de fin de l'interval : ")
fin = int(fin)

while fin < debut:
    print("ERREUR : Le nombre de fin doit être supérieur au nombre de début !!! ")
    debut = input("Veuillez Saisir le nombre de début de l'interval : ")
    debut = int(debut)
    
    fin = input("Veuillez Saisir le nombre de fin de l'interval : ")
    fin = int(fin)

nbre_aleatoire = randint(debut, fin)

nbre_essai = input("Veuillez entrer le nombre d'essai ou tentatives : ")
nbre_essai = int(nbre_essai)

i = 0
while i < nbre_essai:
    saisie = input("Tentative n° {0}  ".format(i+1))
    saisie = int(saisie)
    if saisie > nbre_aleatoire:
        print("Le aleatoire à deviner est plus petit que {0}".format(saisie))
    elif saisie < nbre_aleatoire:
        print("Le aleatoire à deviner est plus grand que {0}".format(saisie))
    elif saisie == nbre_aleatoire:
        print("Bravo M. {2}, vous avez reussi dans {0} essaies car le nombre a deviner est {1}".format(i, nbre_aleatoire, nom))
        break
    i += 1
if nbre_aleatoire != saisie:
    print("M. {0}, vous avez échoué à {1} tentatives sachant que le nombre à deviner était {2}".format(nom, i, nbre_aleatoire))
