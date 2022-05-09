import tkinter as tk  #librairie Tkinter
import random #choisir un nombre aléatoirement
from tkinter import messagebox #Ouvrir une pop-up avec une information


###############################################################################################

# Constantes
LARGEUR = 400 # Car chaque ligne a 4 cases de 100px chacune
HAUTEUR = 400 # Car il y a 4 lignes et chaque ligne fait 100px
mouvement = 0 # Nombre de mouvements
POLICE=('Arial', 30, 'bold') #Police d'écriture pour tout le jeu

###############################################################################################

# Fonctions Jeu

# Cette fontion dessine le tableau de jeu
# Création des tuiles
tuile=[None for i in range(17)] # 16 listes tuiles vides qu'on remplira avec le numero par la suite.
def tableaudejeu():
    global taquin,i_vide,j_vide
    for i in range(4):
        for j in range(4):
            x=100*j # definit la position x de chaque carré, boucle.
            y=100*i ## definit la position y de chaque carré, boucle.
            debutcarre=(x,y)
            fincarre= (x+100, y+100) #100 pixels chaque carré
            milieucarre=(x+50, y+50) #Creer une variable qui represente la moitié du carré pour pouvoir y mettre le numero, centré.
            numero=taquin[i][j]
            if numero==16: #Lorsqu'on arrive à 16 dans la matrice on dessine un carré noir.
                carre=canvas.create_rectangle(debutcarre, fincarre, fill="black")
                chiffre=canvas.create_text(milieucarre, text=numero, fill="black", font=POLICE)
                tuile[numero]=(carre, chiffre)
                i_vide=i
                j_vide=j
            else: #Sinon on crée un carré normal
                carre=canvas.create_rectangle(debutcarre, fincarre, fill="blue3")
                chiffre=canvas.create_text(milieucarre, text=numero, fill="lightblue3", font=POLICE) #on insère le numero à l'interieur de la tuile
                tuile[numero]=(carre, chiffre) #création de la tuile par numero.

    


def identification(event):
    global i_vide,j_vide,taquin
    i=event.y//100 #On prends la cordonnée x et on divise par 100(taille de chaque tuile) on aura forcément un nombre compris entre 0 et 3
    j=event.x//100 #On prends la cordonnée y et on divise par 100(taille de chaque tuile) on aura forcément un nombre compris entre 0 et 3
    #print("Ligne :", i, "Colonne :", j,"Tuile n° :", taquin[i][j]) #On va verifier dans taquin à quel numero ça correspond.

    if taquin[i][j]:
        numero=taquin[i][j]
        (carre,chiffre)=tuile[numero]
        #Si possible, on déplace.
        if i-1==i_vide and j==j_vide: #On verifie si au dessus c'est le carré noir
           canvas.move(carre, 0, -100) #On change la partie graphique maintenant en deplaçant le carré et le chiffre.
           canvas.move(chiffre, 0, -100)

        elif i+1==i_vide and j==j_vide: #On verifie si en dessous c'est le carré noir
            canvas.move(carre, 0, 100)
            canvas.move(chiffre, 0, 100)

        elif j-1==j_vide and i==i_vide: #On verifie si à gauche c'est le carré noir
            canvas.move(carre, -100, 0)
            canvas.move(chiffre, -100, 0)

        elif j+1==j_vide and i==i_vide: #On verifie si à droite c'est le carré noir
            canvas.move(carre, 100, 0)
            canvas.move(chiffre, 100, 0)
        
        else:
            return

        taquin[i][j],taquin[i_vide][j_vide]=taquin[i_vide][j_vide],taquin[i][j] #On actualise la matrice en echangeant les valeurs de la matrice qui correspond au changement qu'on vient de faire.
        i_vide=i #La nouvelle case vide sera celle ou on a appuyé au debut, car apres le deplacement c'est elle qui devient vide.
        j_vide=j #La nouvelle case vide sera celle ou on a appuyé au debut, car apres le deplacement c'est elle qui devient vide.
        tableaudejeu() #Redessine le tableau avec la nouvelle matrice, actualise le tableau. Resout probleme case vide en bas à droite meme apres deplacement.
        deplacer() #Fontion qui verifie si on a gagné et qui enregistre le mouvement.

i_vide=3 #carré vide est situé en i=3 taquin[3][3] #Sauf quand on charge une nouvelle partie, valeurs seront actualisées par tableaujeu() - l.35
j_vide=3 #carré vide est situé en j=3 taquin[3][3] #Sauf quand on charge une nouvelle partie, valeurs seront actualisées par tableaujeu() - L.36


# déplacement des tuiles
def deplacer():
    global taquin, taquin_victoire,mouvement,taquinprecedent
    if taquin == taquin_victoire:
        messagebox.showinfo("Taquin","Bravo, tu as gagné!")
        messagebox.showinfo("Victoire","Veuillez appuyer sur le bouton Mélanger afin de rejouer une partie.")
        mouvement=mouvement+1 #Car le mouvement qui mene à la victoire compte aussi.
    else :
        taquinprecedent=taquin.copy()
        mouvement= mouvement+1


###############################################################################################

# Fonctions des Boutons de l'interface graphique

def fermer_partie():
    racine.destroy()


def melanger():
    global taquin
    taquin[3][3]=16 #On place le carré vide en bas à droite.
    numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
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

####
def annuler():
    global taquin, taquinprecedent,mouvement
    if mouvement>0:
        for x in range(len(taquinprecedent)):   
            for i in range(4):
                for j in range(4):
                    taquin[i][j]=int(taquinprecedent[x])
        mouvement=mouvement-1
    else:
        messagebox.showerror("Annuler Mouvement", "Vous n'avez pas de mouvement pouvant être annulé.")
    tableaudejeu()  #Redessine le tableau avec la nouvelle matrice, actualise le tableau.
    

def aide():
    if mouvement < 10 :
        messagebox.showinfo("Aide", "Trop tôt! Essayez encore quelques coups.")
    elif mouvement>11 and mouvement<35:
            messagebox.showinfo("Aide", "Si vous avez des difficultés à aligner la tuile n°3 et n°4, essayez de descendre la n°1 et de décaler la n°2 ainsi que n°3 sur la gauche, faites monter la n°4 et descendez la tuile que l'on ne veut pas et réalignez les tuiles  n°1 n°2 n°3")
    elif mouvement >36 and mouvement <55:
            messagebox.showinfo("Aide", "Si vous avez des difficultés à aligner la tuile n°7 et n°8, essayez de descendre la n°5 et de décaler la n°6 ainsi que n°7 sur la gauche, faites monter la n°8 et descendez la tuile que l'on ne veut pas et réalignez les tuiles  n°5 n°6 n°7")
    elif mouvement > 56 and mouvement <75:
            messagebox.showinfo("Aide","Le but ici est d'avoir la tuile n°13 ainsi que la tuile n°9 au bon emplacement, sinon ça devient compliqué d'aligner le reste.")
    elif mouvement >76:
            messagebox.showinfo("Aide", "Vous n'avez plus d'aides.")
     

###############################################################################################
###############################################################################################

# Matrices

taquin=[[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
#Les numeros sur les tuiles suivront cette matrice. Matrice qui est melangée à l'execution du code.

taquinprecedent=[None for i in range(100)]
print(taquinprecedent)
taquinprecedent[mouvement]=taquin[i][j]
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


