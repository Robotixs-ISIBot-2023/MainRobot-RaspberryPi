import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Pin_led = 4
Pin_switch = 27

GPIO.setup(Pin_led, GPIO.OUT)
GPIO.setup(Pin_switch, GPIO.IN)

GPIO.output(Pin_led, 0)

old_button_state = 1

while True :
    

    buttonState = GPIO.input(Pin_switch)
    
    """ Pour utiliser le switch de depart en no"""
    
    if buttonState == 0 and old_button_state == 1:  
        GPIO.output(Pin_led,1)  #HIGH
        print("on")
        old_button_state = buttonState
        
GPIO.cleanup()
