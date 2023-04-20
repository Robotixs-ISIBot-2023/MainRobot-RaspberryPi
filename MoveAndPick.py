# -*- coding: utf-8 -*-
"""
ISIBot - Main code for the Main Robot

Created on Mar 29 2023
Last modification on Apr 18 2023

Authors : 
@AntoDB - Antonin De Breuck (BC informatique)
"""

#=========================================================================================================#

                        #-------------------- Modules imported --------------------#

#=========================================================================================================#

from Move.sendDataToTeensy import *
from Communication.publish import *
from Captors.buttonsSetup import *
from Captors.gpio_start_setup import *

import time

#=========================================================================================================#

            #-------------------- Mofiable/Changeable variables | Options --------------------#

#=========================================================================================================#
            
#================================================== Parameters ==================================================#

# NOTHING HERE FOR THE MOMEMENT

#================================================== Don't touch ==================================================#

flag_start_move = True
tryCatchPuck = 0

"""
    MQTT communication
"""
# MQTT Topics
topics = {"main_start" : 0, "teamcolor" : "null", "main_send_cameradata" : 0, "main_move_straight" : 0, "main_move_turn" : 0}
"""
main_start : 0 par défaut, 1 pour lancer # Aussi avec button
teamcolor : null par défaut, blue or green pour choisir # Aussi avec button
main_send_cameradata : 0 par défaut ou pour stop, 1 pour envoyer des données de déplacement caméra
main_move_straight : INT donnée par la caméra pour avancer/reculer
main_move_turn : INT donnée par la caméra pour tourner
"""

#=========================================================================================================#

                        #-------------------- Homemade Function/Class --------------------#

#=========================================================================================================#

#================================================== MQTT communication ==================================================#

# Wait for incoming messages and update variables
def on_message(client, userdata, message):
    global topics
    print("Received message on topic {}: {}".format(message.topic, message.payload))
    for key in topics:
        if message.topic == key:
            msg = message.payload.decode()
            if msg.isdigit():
                topics[key] = int(msg)
            else:
                topics[key] = msg

#=========================================================================================================#

                            #-------------------- Executed code --------------------#

#=========================================================================================================#

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

"""
    MQTT communication
"""
# Start the background thread for MQTT communication
client.loop_start()

# ===== Subscribe to MQTT broker ===== #
# Subscribe for new messages on topics
for key in topics:
    #print(key)
    client.subscribe(key)
client.on_message = on_message


"""
    MAIN CODE
"""

# Wait the start & the team color
while topics["main_start"] == 0 or topics["teamcolor"] == "null":
    # Do nothing & wait the button teamcolor push & start
    if GPIO.input(Pin_Green_Btn) == GPIO.HIGH:
        if not(oldGreenButtonPush):
            print("GREEN Button was pushed!")
            publish("teamcolor", "green") # Send to MQTT for rasp on main robot & jetson
            oldGreenButtonPush = True
    else:
        if oldGreenButtonPush:
            print("GREEN Button was NOT pushed!")
            oldGreenButtonPush = False
    
    if GPIO.input(Pin_Blue_Btn) == GPIO.HIGH:
        if not(oldBlueButtonPush):
            print("BLUE Button was pushed!")
            publish("teamcolor", "blue") # Send to MQTT for rasp on main robot & jetson
            oldBlueButtonPush = True
    else:
        if oldBlueButtonPush:
            print("BLUE Button was NOT pushed!")
            oldBlueButtonPush = False

    buttonState = GPIO.input(Pin_switch)

    """ Pour utiliser le switch de depart en no"""
    
    if buttonState == 1 and old_button_state == 0:  
        print("GOOOOO !")
        publish("main_start", 1) # Send to MQTT the start
        old_button_state = buttonState

# When start :
while True:
    if flag_start_move:
        GPIO.cleanup()

        # ABANDON SEQUENCE JUST GO and slide with the pucks 😏
        goForward(600)
        time.sleep(2)

        # IF BLUE
        if  topics["teamcolor"] == "blue":
            print("Blue - Turn left")
            turnLeft(95)
        # IF GREEN
        if  topics["teamcolor"] == "green":
            print("Green - Turn right")
            turnRight(82)
        time.sleep(1.5)

        goForward(500)
        time.sleep(1.7)

        # IF BLUE
        if  topics["teamcolor"] == "blue":
            print("Blue - Turn right")
            turnRight(82)
        # IF GREEN
        if  topics["teamcolor"] == "green":
            print("Green - Turn left")
            turnLeft(95)
        time.sleep(1.5)

        goForward(1200)
        time.sleep(3.5)

        # IF BLUE
        if  topics["teamcolor"] == "blue":
            print("Blue - Turn right")
            turnRight(90)
        # IF GREEN
        if  topics["teamcolor"] == "green":
            print("Green - Turn left")
            turnLeft(90)
        time.sleep(1.5)

        goForward(600)
        time.sleep(2) # Drop pucks
        goBackward(600) # Go back to be seen by the camera
        time.sleep(2)

        # Relay with camera on Jetson
        flag_start_move = False
    else:
        if topics["main_goToBase"] == False :
            break

        # In automatic - Jetson
        publish("main_send_cameradata", 1) # Ask the Jetson to send data | CAUTION Wait until the robot stop moving

        print("main_move_straight: ", float(topics["main_move_straight"]))
        print("main_move_turn: ", float(topics["main_move_turn"]))

        # If turn right
        if float(topics["main_move_turn"]) > 0 :
            if float(topics["main_move_turn"]) > 90 :
                turnRight(90)
                time.sleep(2)
                turnRight(float(topics["main_move_turn"])-90)
                # If nothing is found
                if int(topics["main_move_turn"]) == 180 and int(topics["main_move_straight"]) == 0:
                    tryCatchPuck += 1
            else:
                turnRight(float(topics["main_move_turn"]))
            print("Tourne à droite")
            time.sleep(4)
        # If turn left
        elif float(topics["main_move_turn"]) < 0 :
            if float(topics["main_move_turn"]) < -90 :
                turnLeft(90)
                time.sleep(2)
                turnRight(-float(topics["main_move_turn"])-90)
            else:
                turnLeft(- float(topics["main_move_turn"]))
            print("Tourne à gauche")
            time.sleep(4)

        # If go forward
        if float(topics["main_move_straight"]) > 0 :
            goForward(float(topics["main_move_straight"])*10)
            print("Avance")
            time.sleep(4)
        # If go backward
        elif float(topics["main_move_straight"]) < 0 :
            goBackward(float(topics["main_move_straight"])*10)
            print("Recule")
            time.sleep(4)

        # RESET VARIABLES
        print("RESET VARIABLES & WAIT")
        publish("main_send_cameradata", 0)
        publish("main_move_straight", 0)
        publish("main_move_turn", 0)

        if tryCatchPuck >= 20:
            print("Not found pucks 20 times so go to plate and bo back to base")
            if topics["main_isfull"] == False :
                publish("main_isfull", True)    # To go to the plate
            else:
                if topics["main_isfull2"] == False :
                    publish("main_isfull2", True)   # To stand up straight for the plate
                else:
                    publish("main_isfull", False)
                    publish("main_isfull2", False)
                    publish("main_goToBase", True)   # To go to the base

        time.sleep(10)

