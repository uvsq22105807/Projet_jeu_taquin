import tkinter as tk  #librairie Tkinter
from random import randint #choisir un nombre aléatoirement

##################
# Constantes

LARGEUR = 400 #Car chaque ligne a 4 cases de 100px chacune
HAUTEUR = 400 #Car il y a 4 lignes et chaque ligne fait 100px

###################
# Fonctions
FONT=('Ubuntu', 27, 'bold')


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
racine.title("Jeu du Taquin")
canvas.bind("<Button-1>")
canvas.pack()



# création des tuiles

tuile_1 = canvas.create_rectangle(0, 0, 100, 100, fill ="red"), canvas.create_text(50, 50,text="1", fill ="Black", font = FONT) 
tuile_2 = canvas.create_rectangle(100, 0, 200, 100, fill ="red"), canvas.create_text(150, 50,text="2", fill ="Black", font = FONT) 
tuile_3 = canvas.create_rectangle(200, 0, 300, 100, fill ="red"), canvas.create_text(250, 50,text="3", fill ="Black", font = FONT) 
tuile_4 = canvas.create_rectangle(300, 0, 400, 100, fill ="red"), canvas.create_text(350, 50,text="4", fill ="Black", font = FONT) 
tuile_5 = canvas.create_rectangle(0, 100, 100, 200, fill ="red"), canvas.create_text(50, 150,text="5", fill ="Black", font = FONT) 
tuile_6 = canvas.create_rectangle(100, 100, 200, 200, fill ="red"), canvas.create_text(150, 150,text="6", fill ="Black", font = FONT) 
tuile_7 = canvas.create_rectangle(200, 100, 300, 200, fill ="red"), canvas.create_text(250, 150,text="7", fill ="Black", font = FONT)
tuile_8 = canvas.create_rectangle(300, 100, 400, 200, fill ="red"), canvas.create_text(350, 150,text="8", fill ="Black", font = FONT) 
tuile_9 = canvas.create_rectangle(0, 200, 100, 300, fill ="red"), canvas.create_text(50, 250,text="9", fill ="Black", font = FONT) 
tuile_10 = canvas.create_rectangle(100, 200, 200, 300, fill ="red"), canvas.create_text(150, 250,text="10", fill ="Black", font = FONT) 
tuile_11 = canvas.create_rectangle(200, 200, 300, 300, fill ="red"), canvas.create_text(250, 250,text="11", fill ="Black", font = FONT) 
tuile_12 = canvas.create_rectangle(300, 200, 400, 300, fill ="red"), canvas.create_text(350, 250,text="12", fill ="Black", font = FONT) 
tuile_13 = canvas.create_rectangle(0, 300, 100, 400, fill ="red"), canvas.create_text(50, 350,text="13", fill ="Black", font = FONT) 
tuile_14 = canvas.create_rectangle(100, 300, 200, 400, fill ="red"), canvas.create_text(150, 350,text="14", fill ="Black", font = FONT)
tuile_15 = canvas.create_rectangle(200, 300, 300, 400, fill ="red"), canvas.create_text(250, 350,text="15", fill ="Black", font = FONT) 



# déplacement des tuiles


# boucle principale
racine.mainloop()
