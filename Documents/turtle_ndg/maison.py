"""Module maison
   Auteur : Paul-Emile Razafindrakoto
   Construction d'une maison avec Turtle
   Compatible avec Numworks (Python 3.4 et MicroPython 1.2) 
"""

from turtle import * 

setpos(0,0)
couleur='black'  #couleur par défaut

####################################
# Défintion de fonctions générales #
####################################

def carre(longueur,angle):
    """Construit un carré
    Paramètres:
        longueur
        angle
    Résultat:
        un carré
    """
    for i in range(1,5):
        forward(longueur)
        right(angle)

def rectangle(longueur,largeur,angle):
    """Construit un rectangle
    Paramètres:
        longueur
        largeur
        angle
    Résultats:
        un rectangle
    """
    for i in range(1,3):
        forward(longueur)
        right(angle)
        forward(largeur)
        right(angle)

#reposition avec penup pendown
def reposition(abscisse,ordonnee):
    penup()
    setpos(abscisse,ordonnee)
    pendown()

###########################################
# Définition des fonctions pour la maison #
# avec porte, fenêtres, murs et toit      #
###########################################

#murs
def murs(couleur):
    """Construit des murs
    Appelle la fonction carré avec une longueur et un angle prédéfinis
    Paramètres:
        couleur
    Résultats:
        Des murs
    """
    color(couleur)
    carre(100,90)


#toit de la maison
def toit(couleur):
  color(couleur)
  setheading(45)
  forward(75)
  right(93)
  forward(75)


#fenêtres
def fenetre(couleur):
    """Construit une fenêtre
    Appelle la fonction carré avec une longueur et un angle prédéfinis
    Paramètres:
        couleur
    Résultats:
        Une fenêtre 
    """
    color(couleur) 
    setheading(0)
    carre(20,90)


#porte
def porte(couleur):
    """Construit une porte
    Appelle la fonction rectangle avec une longueur, une largeur et un angle prédéfinis
    Paramètres:
        couleur
    Résultats:
        Une porte 
    """
    color(couleur)
    right(90)
    rectangle(40,30,90)


#############################
# Construction de la maison #
#############################

murs(couleur='brown')
toit(couleur='red')
reposition(10,-20)
fenetre(couleur='blue')
reposition(70,-20)
fenetre(couleur='blue')
reposition(60,-60)
porte(couleur='black')

