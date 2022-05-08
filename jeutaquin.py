from ast import Pass
import tkinter as tk  #librairie Tkinter
import random #choisir un nombre aléatoirement
from tkinter import messagebox #Ouvrir une pop-up avec une information
from turtle import width
from unittest import case 

###############################################################################################

# Constantes
LARGEUR = 400 # Car chaque ligne a 4 cases de 100px chacune
HAUTEUR = 400 # Car il y a 4 lignes et chaque ligne fait 100px
mouvement = 0 # Nombre de mouvements
POLICE=('Arial', 30, 'bold') #Police d'écriture pour tout le jeu

###############################################################################################

# Fonctions Jeu

def identification(event):
    i=event.y//100 #On prends la cordonnée x et on divise par 100(taille de chaque tuile) on aura forcément un nombre compris entre 0 et 3
    j=event.x//100 #On prends la cordonnée y et on divise par 100(taille de chaque tuile) on aura forcément un nombre compris entre 0 et 3
    i_vide=3 #carré vide est situé en i=3 taquin[3][3]
    j_vide=3 #carré vide est situé en j=3 taquin[3][3]
    print("Ligne :", i, "Colonne :", j,"Tuile n° :", taquin[i][j]) #On va verifier dans taquin à quel numero ça correspond.
    if i-1==i_vide and j==j_vide:
        taquin[i][j],taquin[i_vide][j_vide]=(taquin[i_vide][j_vide],taquin[i][j])
        deplacer()
        tableaudejeu()
    elif i+1==i_vide and j==j_vide:
        taquin[i][j],taquin[i_vide][j_vide]=(taquin[i_vide][j_vide],taquin[i][j])
        deplacer()
        tableaudejeu()
    elif j-1==j_vide and i==i_vide:
        taquin[i][j],taquin[i_vide][j_vide]=(taquin[i_vide][j_vide],taquin[i][j])
        deplacer()
        tableaudejeu()
    elif j+1==j_vide and i==i_vide:
        taquin[i][j],taquin[i_vide][j_vide]=(taquin[i_vide][j_vide],taquin[i][j])
        deplacer()
        tableaudejeu()
    


# déplacement des tuiles
def deplacer():
    global taquin, taquin_victoire, taquinprecedent,mouvement
    if taquin == taquin_victoire:
        messagebox.showinfo("Taquin","Bravo, tu as gagné!")
        print("Tu as gagné en", mouvement, "coups.")
    else : 
        for i in range(4): 
            for j in range(4):
                taquinprecedent.append(taquin[i][j]) 
        mouvement= mouvement+1



# Cette fontion dessine le tableau de jeu
# Création des tuiles
def tableaudejeu():
    tuile=[None for i in range(17)] # 16 listes tuiles vides qu'on remplira avec le numero par la suite.
    for i in range(4):
        for j in range(4):
            x=100*j # definit la position x de chaque carré, boucle.
            y=100*i ## definit la position y de chaque carré, boucle.
            debutcarre=(x,y)
            fincarre= (x+100, y+100) #100 pixels chaque carré
            milieucarre=(x+50, y+50) #Creer une variable qui represente la moitié du carré pour pouvoir y mettre le numero
            carre=canvas.create_rectangle(debutcarre, fincarre, fill="dodgerblue")
            numero=taquin[i][j]  
            chiffre=canvas.create_text(milieucarre, text=numero, fill="white", font=POLICE) #on insère le numero à l'interieur de la tuile
            tuile[numero]=(carre, chiffre) #création de la tuile par numero.

    canvas.delete(carre) #permet de supprimer le dernier carré, le numero 16 dont nous avons pas besoin
    canvas.delete(chiffre) #permet de supprimer le dernier carré, le numero 16 dont nous avons pas besoin


###############################################################################################

# Fonctions des Boutons de l'interface graphique

def fermer_partie():
    racine.destroy()


def melanger():
    numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    global taquin
    for i in range(3): #Melange les 4 colonnes des 3 premières lignes de la matrice
        for j in range(4):
            x=random.randint(0,len(numeros)-1)
            taquin[i][j]=numeros[x]
            del numeros[x]
    for j in range(3): #Melange les 3 colonnes de la dernière ligne de la matrice, car la toute derniere case est vide.
        x=random.randint(0,len(numeros)-1)
        taquin[3][j]=numeros[x]
        del numeros[x]
    tableaudejeu()  #Redessine le tableau avec la nouvelle matrice, actualise le tableau.


def sauvegarde():
    fic=open("sauvegarde.txt", "w")
    for i in range(4):
        for j in range(4):
            fic.write(str(taquin[i][j]) + "\n")
    fic.close()
    messagebox.showinfo("Sauvegarde", "Sauvegarde réussie.") 


def charger_partie():
    global taquin
    fic=open("sauvegarde.txt", "r")
    ligne=fic.readlines() #ligne devient une liste contenant chaque ligne du fichier.
    l=0 #compte l'indice de la liste ligne
    for i in range(4): 
        for j in range(4):
            taquin[i][j]=int(ligne[l]) #on remplace taquin[0][0] par le premier élément de la liste et ainsi de suite.
            l=l+1 #on passe au prochain élément de la liste.
    fic.close()
    tableaudejeu() #Redessine le tableau avec la nouvelle matrice, actualise le tableau.


def annuler():
    global taquin, taquinprecedent,mouvement
    if mouvement>0:
        for i in range(4):
            for j in range(4):
                taquinprecedent[i][j]=taquin[i][j]
                mouvement=mouvement-1
    else:
        messagebox.showerror("Annuler Mouvement", "Vous n'avez pas de mouvement pouvant être annulé.")
    tableaudejeu()  #Redessine le tableau avec la nouvelle matrice, actualise le tableau. 
    

def aide():
    pass




###############################################################################################
###############################################################################################

# Matrices

taquin=[[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
#Les numeros sur les tuiles suivront cette matrice. Matrice qui est melangée à l'execution du code.

taquinprecedent=[None for x in range(100)] 
#On crée 100 listes vides, taquinprecedent[mouvement] representera la matrice apres chaque coup.
#mouvement sera le coup ou on est, mvmt-1 sera le coup précedent, pour pouvoir annuler le mouvement on remplace la matrice actuelle par la matrice precedente.
#100 listes donc on pourra reculer 100 coups, annuler 100 mouvements.


#On gagne quand on arrivé au resultat ci-dessous.
taquin_victoire=[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]

###############################################################################################
###############################################################################################

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
racine.title("Jeu du Taquin")
melanger() #lance le jeu melangé au demarrage.

bouton_fermer = tk.Button(racine, text="Fermer",command=fermer_partie)
bouton_melanger = tk.Button(racine, text="Melanger",command=melanger)
bouton_sauvegarder= tk.Button(racine, text="Sauvegarder", command=sauvegarde)
bouton_charger = tk.Button(racine, text="Charger",command=charger_partie)
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


canvas.bind("<Button-1>",identification)

###############################################################################################
###############################################################################################

# boucle principale
racine.mainloop()


