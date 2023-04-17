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

from Communication.MQTTconnection import *

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
def on_message(client, datas: dict, message):
    print("Received message on topic {}: {}".format(message.topic, message.payload))
    if message.topic == datas["topic1"]:
        datas["Commande"] = int(message.payload.decode())
        print("DEBUG1")
"""
def subscribe(datas):
    # Create a client instance
    global client
    client = mqtt.Client(datas=datas)

    # Connect to the broker
    client.connect(broker_address)

    # Start the background thread for MQTT communication
    client.loop_start()

    # Check for new messages on topic "main_move"
    client.subscribe(datas["topic1"])
    client.on_message = on_message  # Define the function to handle incoming messages
"""
#=========================================================================================================#

                #-------------------- If directly excute, make that --------------------#

#=========================================================================================================#

if __name__ == '__main__':
    import time
    global datas

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
    print("")
    print("=> Commande ?")

    # Initialize variables
    datas = {"Commande": 0, "topic1" : str(input("Entrez un nom de topic (sub) : "))}

    """
    # ===== Subscribe to MQTT broker ===== #
    # Start the background thread for MQTT communication
    client.loop_start()

    # Check for new messages on topic
    client.subscribe(datas["topic1"])
    client.on_message = on_message()  # Define the function to handle incoming messages
    # ===== ===== #
    """

    # Subscribe to MQTT broker
    #subscribe(datas)

    # Wait for incoming messages and update variables
    while True:
        print("Commande:", datas["Commande"])
        datas["Commande"] = 0
        time.sleep(1)
