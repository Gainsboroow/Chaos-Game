"""
Chaos Game
Created by Gainsboroow 
Github : https://github.com/Gainsboroow
Github Repository : https://github.com/Gainsboroow/Chaos-Game

How to use : 
Right Click to begin the generation. 
You can choose the number of side and the number of displayed points in the two top right cases.
"""

from tkinter import *
from math import *

from random import randrange

height = 600
width = 1200

window = Tk()
window.title("Chaos Game")
window.geometry(str(width+100)+"x"+str(height)+"+0+0")

canvas = Canvas(window, bg = "black")
canvas.place(x=0,y=0, width = width, height = height)

line = []

nbCote = 3
nbPoints = 10**3
origineX, origineY = width / 2, height / 2
longueur = min( width, height ) / 2

sommet = []

dist = lambda ind1, ind2 : min( abs(ind1 - ind2), min(ind1, ind2) + nbCote - max(ind1, ind2) )

def generer(event):
    global sommet, nbCote, nbPoints

    print("Start")

    reset()

    nbCote = int(valeur.get())
    nbPoints = int(valeur2.get())
    angle = 2 / nbCote * pi

    sommet = [ (origineX + longueur, origineY) ]
    for i in range(1, nbCote):
        x,y = origineX + longueur * cos(i*angle), origineY + longueur * sin(i*angle)
        sommet.append((x,y))

    init(event.x, event.y)

def dessinerLigne(listePoints):
    precX, precY = listePoints[0][0], listePoints[0][1]
    
    listePoints = listePoints + [ listePoints[0] ]

    for x, y in listePoints:
        canvas.create_line(precX, precY, x, y, fill = "red", width = 2)
        precX, precY = x, y


def init(x,y):
    for i in line :
        canvas.delete(i)

    dessinerLigne(sommet)

    precIndice = 0
    indice = 0

    for i in range(nbPoints):
        indice = randrange(0,len(sommet))
        
        #Sommet adjacents
        
        while dist(precIndice, indice) > 1:
            indice = randrange(0,len(sommet))
        
        """
        if nbCote > 3:
            while indice == precIndice :
                indice = randrange(0,len(sommet))
        """

        precIndice = indice
        
        x,y = sommet[indice][0]/2 + x/2, sommet[indice][1]/2 + y/2 

        #line.append( canvas.create_line(x,y, x+1, y, fill = "light green") )
        line.append( canvas.create_oval(x,y, x, y, fill = "light green") )

    dessinerLigne(sommet)

    print("Done")

def reset(event = ""):
    """ Efface les dessins présents """

    global canvas, valeur, entree
    
    canvas.destroy()
    canvas = Canvas(window, bg = "black")
    canvas.place(x=0,y=0, width = width, height = height)

""" Création des cases de prise d'entrée """
label = Label(window, text="Nombre de côtés : ").place(x = width, y = 10)
valeur = StringVar()
entree = Entry(window, textvariable = valeur).place(x=width, y=30) #Modifie le nombre de cote
valeur.set("3")

label = Label(window, text="Nombre de points : ").place(x = width, y = 50)
valeur2 = StringVar()
entree2 = Entry(window, textvariable = valeur2).place(x=width, y=70) #Modifie le nombre de points affichés
valeur2.set("1000")


#Un Clic droit début le processus
window.bind("<Button-3>", generer)
window.bind("<KeyPress>", generer)

window.mainloop()
