import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

oldGreenButtonPush = False
oldBlueButtonPush = False

if __name__ == '__main__':
    while True: # Run forever
        if GPIO.input(16) == GPIO.HIGH:
            if not(oldGreenButtonPush):
                print("GREEN Button was pushed!")
                oldGreenButtonPush = True
        else:
            if oldGreenButtonPush:
                print("GREEN Button was NOT pushed!")
                oldGreenButtonPush = False
        
        if GPIO.input(18) == GPIO.HIGH:
            if not(oldBlueButtonPush):
                print("BLUE Button was pushed!")
                oldBlueButtonPush = True
        else:
            if oldBlueButtonPush:
                print("BLUE Button was NOT pushed!")
                oldBlueButtonPush = False
