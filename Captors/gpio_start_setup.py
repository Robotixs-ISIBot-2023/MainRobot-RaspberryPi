# -*- coding: utf-8 -*-
"""
ISIBot - Code for the start switch on the Main Robot

Created on Apr 19 2023
Last modification on Apr 19 2023

Authors : 
@Sabrine - Sabrine Belhaouar (M2 électronique)
"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

Pin_switch = 27

GPIO.setup(Pin_switch, GPIO.IN)

old_button_state = 1

if __name__ == '__main__':
    Pin_led = 4
    GPIO.setup(Pin_led, GPIO.OUT)
    GPIO.output(Pin_led, 0)

    while True :
        buttonState = GPIO.input(Pin_switch)
        
        """ Pour utiliser le switch de depart en no"""
        
        if buttonState == 0 and old_button_state == 1:  
            GPIO.output(Pin_led,1)  #HIGH
            print("on")
            old_button_state = buttonState
            
GPIO.cleanup()
