# -*- coding: utf-8 -*-
"""
ISIBot - Code for setup team colors buttons on the Main Robot

Created on Apr 18 2023
Last modification on Apr 18 2023

Authors : 
@AntoDB - Antonin De Breuck (BC informatique)
"""

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

Pin_Green_Btn = 16
Pin_Blue_Btn = 18

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(Pin_Green_Btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Pin_Blue_Btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

oldGreenButtonPush = False
oldBlueButtonPush = False

if __name__ == '__main__':
    while True: # Run forever
        if GPIO.input(Pin_Green_Btn) == GPIO.HIGH:
            if not(oldGreenButtonPush):
                print("GREEN Button was pushed!")
                oldGreenButtonPush = True
        else:
            if oldGreenButtonPush:
                print("GREEN Button was NOT pushed!")
                oldGreenButtonPush = False
        
        if GPIO.input(Pin_Blue_Btn) == GPIO.HIGH:
            if not(oldBlueButtonPush):
                print("BLUE Button was pushed!")
                oldBlueButtonPush = True
        else:
            if oldBlueButtonPush:
                print("BLUE Button was NOT pushed!")
                oldBlueButtonPush = False
