import time

print("Hello")
time.sleep(3)
print("World")

# TEST with TKinter to see if a action is executed by another file (here is beeing exectued by "fileToExectuteOther.py")

# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *
# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Mon application")
# Affichage de la fenêtre créée :
fenetre.mainloop()

while True : # To see if the code is executting outside for run this will be stop
    time.sleep(1)
    print("hey")
