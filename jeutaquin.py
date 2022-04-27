import tkinter as tk  #librairie Tkinter
from random import randint #choisir un nombre aléatoirement
from turtle import width 

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
    print("Ligne :", i, "Colonne :", j,"Tuile n° :", taquin[i][j])

def fermer_partie():
    racine.destroy()

def charger_partie():
    pass

def melanger():
    pass

def sauvegarde():
    pass

def annuler():
    mouvement = mouvement - 1
    pass

def aide():
    pass
######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
racine.title("Jeu du Taquin")

bouton_fermer = tk.Button(racine, text="Fermer",command=fermer_partie)
bouton_charger = tk.Button(racine, text="Charger",command=charger_partie)
bouton_melanger = tk.Button(racine, text="Melanger",command=melanger)
bouton_sauvegarder= tk.Button(racine, text="Sauvegarder",command=sauvegarde)
bouton_annuler = tk.Button(racine, text="Annuler mouvement",command=annuler)
bouton_aide = tk.Button(racine, text="Aide",command=aide)

#Positionnement des Widgets
bouton_sauvegarder.grid(row=7, column=0, pady=2, padx=2,sticky=tk.W+tk.E, columnspan=1)
bouton_charger.grid(row=7, column=1, pady=2, padx=2,sticky=tk.W+tk.E, columnspan=1)
bouton_annuler.grid(row=8, column=0, pady=2, padx=2,sticky=tk.W+tk.E, columnspan=1)
bouton_aide.grid(row=8, column =1, pady=2, padx=2, sticky=tk.W+tk.E, columnspan=1)
bouton_fermer.grid(row=10, column = 0, pady=2, padx=2, columnspan=2, sticky=tk.W+tk.E)
bouton_melanger.grid(row=9, column=0, pady=2, padx=2, columnspan=2,sticky=tk.W+tk.E)
canvas.grid(row = 0, column = 0, columnspan=2, sticky=tk.W+tk.E) #Tout le tableau de jeu est considéré comme une seule colonne, on doit alors l'étendre sur 2 colonnes pour pouvoir aligner les boutons en bas.

racine.columnconfigure(1, minsize=200) #permet au canvas d'être centré avec les boutons
racine.columnconfigure(0, minsize=200) #permet au canvas d'être centré avec les boutons

# création des tuiles
POLICE=('Arial', 30, 'bold')
taquin=[[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

canvas.bind("<Button-1>",identification)

tuile=[None for i in range(17)] #numero des tuiles commencera à 1 et non pas 0

for i in range(4):
    for j in range(4):
        x=100*j # definit la position x de chaque carré, boucle.
        y=100*i ## definit la position y de chaque carré, boucle.
        debutcarre=(x,y)
        fincarre= (x+100, y+100) #100 pixels chaque carré
        milieucarre=(x+50, y+50) #Creer une variable qui represente la moitié du carré pour pouvoir y mettre le numero
        carre=canvas.create_rectangle(debutcarre, fincarre, fill="gold")
        numero=taquin[i][j]  
        chiffre=canvas.create_text(milieucarre, text=numero, fill="black", font=POLICE) #on insère le numero à l'interieur de la tuile
        tuile[numero]=(carre, chiffre) #création de la tuile par numero.

canvas.delete(carre) #permet de supprimer le dernier carré, le numero 16 dont nous avons pas besoin
canvas.delete(chiffre) #permet de supprimer le dernier carré, le numero 16 dont nous avons pas besoin


taquin_victoire=[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]


# déplacement des tuiles
def mouvement():
    pass

# boucle principale
racine.mainloop()
