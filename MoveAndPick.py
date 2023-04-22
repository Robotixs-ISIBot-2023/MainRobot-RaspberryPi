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

import RPi.GPIO as GPIO
GPIO.cleanup()

from Move.sendDataToTeensy import *
from Communication.publish import *
from Captors.buttonsSetup import *
from Captors.gpio_start_setup import *

import time
import file

#=========================================================================================================#

            #-------------------- Mofiable/Changeable variables | Options --------------------#

#=========================================================================================================#
            
#================================================== Parameters ==================================================#

points = 0

#================================================== Don't touch ==================================================#

flag_start_move = True
tryCatchPuck = 0
nbrCatchPuck = 0

"""
    MQTT communication
"""
# MQTT Topics
topics = {"main_start" : 0, "teamcolor" : "null", "main_send_cameradata" : 0, "main_move_straight" : 0, "main_move_turn" : 0, "main_isfull" : False, "main_isfull2" : False,  "main_goToBase" : False, "main_points" : points}
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

exec(open('/home/pi/module_lidar.py').read())

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
    
    if buttonState == 1 and old_button_state == 0 and topics["teamcolor"] != "null" :  
        print("GOOOOO !")
        publish("main_start", 1) # Send to MQTT the start
        old_button_state = buttonState

# When start :
while True:
    if flag_start_move:
        start = time.time() # Start calculating time
        publish("main_points", points)
        # CLOSE the servo motor at the back of the robot

        # ABANDON SEQUENCE JUST GO and slide with the pucks 😏
        goForward(600)
        time.sleep(4)

        # IF BLUE
        if  topics["teamcolor"] == "blue":
            print("Blue - Turn left")
            turnLeft(90)
        # IF GREEN
        if  topics["teamcolor"] == "green":
            print("Green - Turn right")
            turnRight(90)
        time.sleep(3)

        goForward(500)
        time.sleep(3)

        # IF BLUE
        if  topics["teamcolor"] == "blue":
            print("Blue - Turn right")
            turnRight(90)
        # IF GREEN
        if  topics["teamcolor"] == "green":
            print("Green - Turn left")
            turnLeft(90)
        time.sleep(4)

        goForward(1200)
        time.sleep(6) # A test avec 3 s

        # IF BLUE
        if  topics["teamcolor"] == "blue":
            print("Blue - Turn right")
            turnRight(90)
        # IF GREEN
        if  topics["teamcolor"] == "green":
            print("Green - Turn left")
            turnLeft(90)
        time.sleep(3)

        goForward(500)
        time.sleep(8) # Drop pucks

        # IF BLUE
        if  topics["teamcolor"] == "blue":
            print("Blue - Turn right back")
            turnRight(160) # turn 180° to drop puck backwards and put ball on top
        # IF GREEN
        if  topics["teamcolor"] == "green":
            print("Green - Turn left back")
            turnLeft(150)
        time.sleep(4)
        
        # OPEN the servo motor at the back of the robot
        points += 9
        publish("main_points", points)

        goForward(600) # Go back (Forward due to the turn 180° in the plate) to be seen by the camera
        # CLOSE the servo motor at the back of the robot
        #goBackward(600) # Go back to be seen by the camera
        time.sleep(4)

        # Relay with camera on Jetson
        flag_start_move = False
    else:

        # In automatic - Jetson
        publish("main_send_cameradata", 1) # Ask the Jetson to send data | CAUTION Wait until the robot stop moving
        time.sleep(3.5)
        
        degrees = int(float(topics["main_move_turn"]))
        distance = int(float(topics["main_move_straight"]))*10

        print("main_move_turn: " + str(degrees) + "°")
        print("main_move_straight: " + str(distance) + " mm")

        # If turn right
        if degrees > 0 :
            turnRight(degrees)
            # If nothing is found
            if degrees == 180 and distance == 0:
                tryCatchPuck += 1
            print("Tourne à droite")
            time.sleep(4)
        # If turn left
        elif degrees < 0 :
            turnLeft(- degrees)
            print("Tourne à gauche")
            time.sleep(4)

        # If go forward
        if distance > 0 :
            if distance != 6000:
                goForward(distance)
                print("Avance")
                time.sleep(4)
        # If go backward
        elif distance < 0 :
            goBackward(- distance)
            print("Recule")
            time.sleep(4)
        nbrCatchPuck += 1

        #print("GO TO BASE ??? " + str(topics["main_goToBase"]))
        #print(type(topics["main_goToBase"]))
        topics["main_goToBase"] = bool(topics["main_goToBase"])
        if topics["main_goToBase"] == True :
            points += 15
            publish("main_points", points)
            publish("main_finish", True) # Annimation with ESP32

            print("")
            print("")
            print("  FINISH")
            print("  Points : " + str(points))
            print("")
            print("")
            break
        
        print("Nbr palets : " + str(nbrCatchPuck))
        print("IS FULL ? " + str(nbrCatchPuck > 0 and nbrCatchPuck % 3 == 0))
        """
        if nbrCatchPuck > 0 and nbrCatchPuck % 3 == 0 : # If detect it's full
            publish("main_isfull", True)    # To go to the plate
        if topics["main_isfull"] == True and topics["main_isfull2"] == False :
            publish("main_isfull2", True)   # To stand up straight for the plate
        if topics["main_isfull"] == True and topics["main_isfull2"] == True :
            turnRight(180)   # turn 180° to drop puck backwards and put ball on top
            time.sleep(2)
            # OPEN the servo motor at the back of the robot
            # Put ball on top
            goForward(600) # Move forward to be catching by the Jetson with camera
            time.sleep(2)
            # CLOSE the servo motor at the back of the robot
            # RESET VARIABLES
            publish("main_isfull", False)
            publish("main_isfull2", False)
            # ADD POINTS
            points += 3
            publish("main_points", points)
        """
        
        done = time.time()
        elapsed = done - start
        print("Time since start: " + str(elapsed) + " s")
        if elapsed >= 60 :
            tryCatchPuck = 20 # Same as not found pucks 20 times -> EMPTY MAIN ROBOT + GO BASE
        
        if elapsed >= 95 :
            tryCatchPuck = 20 # Same as not found pucks 20 times -> EMPTY MAIN ROBOT + GO BASE
            publish("main_points", points)
            publish("main_finish", True) # Annimation with ESP32

            print("")
            print("")
            print("  FINISH")
            print("  Points : " + str(points))
            print("")
            print("")
            break

        if tryCatchPuck >= 20 and topics["main_goToBase"] == False:
            print("Not found pucks 20 times so go to plate and go back to base")
            publish("main_goToBase", True)   # To go to the base
            """
            if topics["main_isfull"] == False :
                publish("main_isfull", True)    # To go to the plate
            else:
                if topics["main_isfull2"] == False :
                    publish("main_isfull2", True)   # To stand up straight for the plate
                else:
                    goBackward(600) # Back off the plate and avoid hitting all the cakes between the plate and the base
                    time.sleep(2)

                    publish("main_isfull", False)
                    publish("main_isfull2", False)
                    publish("main_goToBase", True)   # To go to the base
            """

        # RESET VARIABLES
        print("RESET VARIABLES & WAIT")
        publish("main_send_cameradata", 0)
        publish("main_move_straight", 0)
        publish("main_move_turn", 0)

        #time.sleep(2)
