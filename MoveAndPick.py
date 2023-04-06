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

from Move.sendDataToTeensy import *
from Communication.subscribe import *
from Communication.publish import publish
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

goForward(275)
# First sequence for cake here
goForward(200)
# Sequence for cake here

# IF BLUE
turnLeft(90)

# IF GREEN
turnRight(90)

goForward(300)

# Relay with camera on Jetson

"""
    MQTT communication
"""
# Initialize variables
datas = {"Commande": 0, "topic1" : "main_move"}

# ===== Subscribe to MQTT broker ===== #
# Start the background thread for MQTT communication
client.loop_start()

# Check for new messages on topic
client.subscribe(datas["topic1"])
client.on_message = on_message  # Define the function to handle incoming messages
# ===== ===== #

# Wait for incoming messages and update variables
while True:
    print("Commande:", datas["Commande"])
    datas["Commande"] = 0
    time.sleep(1)
