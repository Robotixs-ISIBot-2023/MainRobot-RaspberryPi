from Move.sendDataToTeensy import *
import time

"""
goForward(275)
time.sleep(1.5)
goForward(250)
time.sleep(1.6)
turnLeft(90)
time.sleep(1.5)
goForward(300)
"""
# Changement juste prendre palet (Plus de stop pour séquence)
goForward(600)
time.sleep(2)
turnLeft(90) # FOR BLUE
time.sleep(1.5)
goForward(500)
time.sleep(1.7)
turnRight(90) # FOR BLUE
time.sleep(1.5)
goForward(1200)
time.sleep(3.5)
turnRight(90) # FOR BLUE
time.sleep(1.5)
goForward(600)
time.sleep(2)
goBackward(600)

time.sleep(2)
turnRight(180) # FOR test
