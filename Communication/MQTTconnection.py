# -*- coding: utf-8 -*-
"""
ISIBot - Connection MQTT

Created on Mar 29 2023
Last modification on Mar 29 2023

Authors :
@AntoDB - Antonin De Breuck (BC informatique)
"""

#=========================================================================================================#

                        #-------------------- Modules imported --------------------#

#=========================================================================================================#

import paho.mqtt.client as mqtt

#=========================================================================================================#

            #-------------------- Mofiable/Changeable variables | Options --------------------#

#=========================================================================================================#

#================================================== Parameters ==================================================#

# MQTT broker address
broker_address = "192.168.0.150" # Jetson IP (because the MQTT broker is in the Jetson) FORCED BY WIFI : D-Link DIR-605L (wifi AntoDB take on place)
#broker_address = "192.168.0.102" # Jetson wifi IP (because the MQTT broker is in the Jetson)
#broker_address = "192.168.0.228" # RbP 4 IP
#broker_address = str(input("Entrez l'IP de la Jetson : "))

# Create a client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address)
