# -*- coding: utf-8 -*-
"""
ISIBot - Catch datas to topic MQTT

Created on Apr 04 2023
Last modification on Apr 04 2023

Authors :
@AntoDB - Antonin De Breuck (BC informatique)
"""

#=========================================================================================================#

                        #-------------------- Modules imported --------------------#

#=========================================================================================================#

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

# Define the function to handle incoming messages
def on_message(client, userdata, message):
    print("Received message on topic {}: {}".format(message.topic, message.payload))
    if message.topic == datas["topic1"]:
        datas["Commande"] = int(message.payload.decode())

def subscribe(topic):
    # Start the background thread for MQTT communication
    client.loop_start()

    # Check for new messages on topic
    client.subscribe(topic)
    client.on_message = on_message  # Define the function to handle incoming messages

#=========================================================================================================#

                #-------------------- If directly excute, make that --------------------#

#=========================================================================================================#

if __name__ == '__main__':
    import time
    global datas, Commande

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
    print(" @AntoDB                                                                       04/04/23") 
    print("=======================================================================================") 

    print("Nothing to see here :p")

    # Initialize variables
    datas = {"Commande": 0, "topic1" : "main_move"}

    # Subscribe to MQTT broker
    subscribe(datas["topic1"])

    # Wait for incoming messages and update variables
    while True:
        print("DEBUG1 Commande:", datas["Commande"])
        datas["Commande"] = 0
        time.sleep(1)
