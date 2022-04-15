import tkinter as tk  #librairie Tkinter
from random import randint #choisir un nombre aléatoirement

##################

# Constantes
LARGEUR = 400 #Car chaque ligne a 4 cases de 100px chacune
HAUTEUR = 400 #Car il y a 4 lignes et chaque ligne fait 100px
mouvement = 0 #Défini une fois fini le nombre de mouvement effectué pour gagné.

###################

# Fonctions
def identification(event):
    i=event.y//100
    j=event.x//100
    print("ligne :", i, "colonne :", j,"Tuile n° :", taquin[i][j])

def fermer_fenetre():
    pass

def charger_fenetre():
    pass

def melanger():
    pass

def sauvegarde():
    pass

def retour():
    pass

def aide():
    pass
######################

# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
racine.title("Jeu du Taquin")

bouton_fermer = tk.Button(racine, text="Fermer", command=fermer_fenetre)
bouton_charger = tk.Button(racine, text="Charger une partie", command=charger_fenetre)
bouton_melanger = tk.Button(racine, text="Melanger", command=melanger)
bouton_sauvegarder= tk.Button(racine, text="Sauvegarder la partie ",command=sauvegarde)
bouton_retour = tk.Button(racine, text="Annuler Mouvement",command=retour)
bouton_aide = tk.Button(racine, text="Aide",command=aide)

#Positionnement des Widgets
bouton_fermer.grid(column=1, row=1, sticky="nswe")
bouton_charger.grid(row=7, column=1)
bouton_melanger.grid(row=7, column=2)
bouton_sauvegarder.grid(row=7, column=3)
bouton_retour.grid(row=7, column=4)
bouton_aide.grid(row=7, column =5)

canvas.grid(row = 0, column = 0, rowspan = 5, columnspan = 5)

# création des tuiles
FONT=('Arial', 30, 'bold')

taquin=[[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

canvas.bind("<Button-1>",identification)

tuile=[None for i in range(17)]

for i in range(4):
    for j in range(4):
        x, y=100*j, 100*i
        A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
        carre=canvas.create_rectangle(A, B, fill="red")
        numero=taquin[i][j]
        chiffre=canvas.create_text(C, text=numero, fill="white", font=FONT)
        tuile[numero]=(carre, chiffre)
canvas.delete(carre)
canvas.delete(chiffre)


taquin_victoire=[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]

canvas.grid()
# déplacement des tuiles


# boucle principale
racine.mainloop()
