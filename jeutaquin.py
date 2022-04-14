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

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
racine.title("Jeu du Taquin")


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
        oval=canvas.create_oval(A, B, fill="red")
        numero=taquin[i][j]
        chiffre=canvas.create_text(C, text=numero, fill="black", font=FONT)
        tuile[numero]=(oval, chiffre)
canvas.delete(oval)
canvas.delete(chiffre)


taquin_victoire=[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]

canvas.pack()
# déplacement des tuiles


# boucle principale
racine.mainloop()
