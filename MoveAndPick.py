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
from Communication.publish import *

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

"""
    MQTT communication
"""
# MQTT Topics
topics = {"main_start" : 0, "color" : "null", "main_move_straight" : 0, "main_move_turn" : 0}

#=========================================================================================================#

                        #-------------------- Homemade Function/Class --------------------#

#=========================================================================================================#

#================================================== MQTT communication ==================================================#

# Initialize variables

# ===== Subscribe to MQTT broker ===== #
# Initialize variables
def on_message(client, userdata, message):
    global topics
    print("Received message on topic {}: {}".format(message.topic, message.payload))
    for key in topics:
        if message.topic == key:
            topics[key] = int(message.payload.decode())

#=========================================================================================================#

                            #-------------------- Executed code --------------------#

#=========================================================================================================#

"""
    MQTT communication
"""
# Start the background thread for MQTT communication
client.loop_start()

# Subscribe for new messages on topics
for key in topics:
    #print(key)
    client.subscribe(key)
client.on_message = on_message

while topics["main_start"] == 0:
    print("WAIT")
    print(topics["main_start"])
    time.sleep(1)

"""
    MQTT communication
"""
# Wait for incoming messages and update variables
while True:
    print("Commande:", topics["main_move_straight"])
    topics["main_move_straight"] = 0
    time.sleep(1)



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

