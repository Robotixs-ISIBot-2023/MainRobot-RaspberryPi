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
broker_address = "172.30.16.20"

# Create a client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address)
