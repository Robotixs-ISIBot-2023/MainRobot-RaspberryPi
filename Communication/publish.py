# -*- coding: utf-8 -*-
"""
ISIBot - Send datas to topic MQTT

Created on Mar 29 2023
Last modification on Mar 29 2023

Authors :
@AntoDB - Antonin De Breuck (BC informatique)
"""

#=========================================================================================================#

                        #-------------------- Modules imported --------------------#

#=========================================================================================================#

#from Communication.MQTTconnection import *
from MQTTconnection import *

#=========================================================================================================#

            #-------------------- Mofiable/Changeable variables | Options --------------------#

#=========================================================================================================#

#================================================== Parameters ==================================================#

# NOTHING HERE FOR THE MOMEMENT
# The connection datas are in "MQTTconnection.py"

#=========================================================================================================#

                        #-------------------- Homemade Function/Class --------------------#

#=========================================================================================================#

def publish(topic: str, message):
    """
    Description : Data to send to a topic on a MQTT broker
    Actions : Send the message at the topic in MQTT
    
    Input :
        topic (str) : the name of the topic to publish
        message (str/int) : message to send
    Output : /
    """
    try:
        client.publish(topic, message)
    except:
        print("[DEBUG] Failed to send data to broker MQTT with the topic {} \t with the message : {}".format(topic, message))

#=========================================================================================================#

                #-------------------- If directly excute, make that --------------------#

#=========================================================================================================#

if __name__ == '__main__':
    from MQTTconnection import *

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
    print(" @AntoDB                                                                       29/03/23") 
    print("=======================================================================================") 
    
    # Affichage des commandes possibles 
    print("Topic = Le nom du thème/salon où l'on veut publier") 
    print("Message = Le message que vous voulez envoyer") 
    print("---------------------------------------------------------------------------------------") 
    print("Remarques: ") 
    print("") 
    print("topic : En string uniquement !")
    print("Attention ! Un message peut être envoyé sur un topic même s'il n'a jamais existé auparavant.")
    print("=======================================================================================") 
    print("") 
    print("=> Commande ?")

    while True:
        topic = str(input("Entrez un nom de topic : "))
        message = input("Entrez un message : ")
        # Send a message to topic
        publish(topic, message)
