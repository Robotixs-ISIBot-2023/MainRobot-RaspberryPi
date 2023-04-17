# -*- coding: utf-8 -*-
"""
ISIBot - Main code for the Main Robot

Created on Mar 29 2023
Last modification on Mar 29 2023

Authors : 
@AntoDB - Antonin De Breuck (BC informatique)
"""

#=========================================================================================================#

                        #-------------------- Modules imported --------------------#

#=========================================================================================================#

#from Move.sendDataToTeensy import *
#from Communication.subscribe import *
from Communication.publish import *
from Communication.subscribe2 import subscribe

import time

print("=======================================================================================")
print("                                                              |_| ") 
print("                 _____  _____ _____ ____        _            (* *)") 
print("                |_   _|/ ____|_   _|  _ \\      | |          __)#(__") 
print("                  | | | (___   | | | |_) | ___ | |_        ( )...( )(_)") 
print("                  | |  \\___ \\  | | |  _ < / _ \\| __|       || |_| ||//") 
print("                 _| |_ ____) |_| |_| |_) | (_) | |_     >==() | | ()/") 
print("                |_____|_____/|_____|____/ \\___/ \\__|        _(___)_") 
print("                                                           [-]   [-]") 
print("") 
print(" @NoWayCall, @AntoDB & @Hugoo                                                  29/03/23") 
print("=======================================================================================") 

#=========================================================================================================#

            #-------------------- Mofiable/Changeable variables | Options --------------------#

#=========================================================================================================#
            
#================================================== Parameters ==================================================#

# NOTHING HERE FOR THE MOMEMENT

#================================================== Don't touch ==================================================#

# NOTHING HERE FOR THE MOMEMENT

#=========================================================================================================#

                        #-------------------- Homemade Function/Class --------------------#

#=========================================================================================================#

#================================================== Operations ==================================================#

# NOTHING HERE FOR THE MOMEMENT

#=========================================================================================================#

                            #-------------------- Executed code --------------------#

#=========================================================================================================#

#goForward(275) # Avancer à la première réserve d'étage gâteau
# First sequence for cake here
"""
ETAGE ROSE
La séquence à effectuer pour faire des gâteaux (sans remplir tout le réservoir) :
RIEN (tout stocker en 1 pile)
"""
#goForward(200) # Avancer à la prochaine réserve d'étage gâteau
# Sequence for cake here
"""
ETAGE JAUNE
La séquence à effectuer pour faire des gâteaux :
- pince niveau moyen
- ouvrir pince
- monter pince
- avancer d'un gâteau
- pince niveau bas
- fermer pince
- monter pince
- reculer de 2 gâteau (pour prendre l'étage rose)
- pince niveau haut
- ouvrir pince
- monter pince
- avancer 2 gâteaux
- pince niveau haut
- fermer pince
- monter pince
- reculer 2 gâteaux (pour prendre l'étage rose 2)
- pince niveau moyen
- ouvrir pince
- monter pince
- avancer d'un gâteau
- pince niveau moyen
- fermer pince
- pince niveau bas
- ouvrir pince
- pince niveau milieu (un peu plus haut)
- reculer d'un gâteau
- fermer pince
- monter pince
"""

# IF BLUE
#turnLeft(90)

# IF GREEN
#turnRight(90)

#goForward(300)

# Relay with camera on Jetson

"""
    MQTT communication
"""
# Initialize variables
datas = {"Commande": 0, "topic1" : "main_move"}

# ===== Subscribe to MQTT broker ===== #
# Initialize variables
Commande = 0
userdata = {"Commande": Commande}

# Subscribe to MQTT broker
subscribe(userdata)

# Wait for incoming messages and update variables
while True:
    print("Commande:", Commande)
    time.sleep(1)
