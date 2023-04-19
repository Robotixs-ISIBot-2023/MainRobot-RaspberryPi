import os
import ydlidar
import time
import math
import RPi.GPIO as GPIO
import sys



# Parametrage pin d'intéruption pour le moteur
GPIO.setmode(GPIO.BCM)
Pin_Stop = 17

GPIO.setup(Pin_Stop, GPIO.OUT)
GPIO.output(Pin_Stop,0)  """Level LOW"""


# Parametrage Taille du Robot et Distance de securité
Taille_Robot = 25
Distance_Securite = 100  """a peu prés 30 cm"""


while True :

    # Sequance d'initialisation du Lidar
    ydlidar.os_init();
    laser = ydlidar.CYdLidar();
    ports = ydlidar.lidarPortList();
    port = "/dev/ttyUSB0";
    for key, value in ports.items():
        port = value;
    laser = ydlidar.CYdLidar();
    laser.setlidaropt(ydlidar.LidarPropSerialPort, port);
    laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 128000);
    laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TRIANGLE);
    laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL);
    laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0);
    laser.setlidaropt(ydlidar.LidarPropSampleRate, 20);
    laser.setlidaropt(ydlidar.LidarPropSingleChannel, False);
    
    ret = laser.initialize();
    if ret:
        ret = laser.turnOn();

        # Recupération des données du scan du Lidar
        scan = ydlidar.LaserScan();
        while ret and ydlidar.os_isOk():
            r = laser.doProcessSimple(scan);
            if r:
                for p in scan.points:

                    # Convertion des valeurs en degre et en mm
                    curr_angle = int(math.degrees(p.angle)+180)
                    dist = (p.range)*254 """1 ich = 25.4 mm"""

                    # Mise a l'état haut de la pin d'interuption du Teensy
                    if dist <= Distance_Securite and dist != 0:
                        GPIO.output(Pin_Stop,1) """Level High"""

                        #Faire des truc en fonction de ou est l'obstacle Ou pas
                        if curr_angle < 225 and curr_angle > 136 :
                            #print("il y a un obstacle derriere")
                            #print(curr_angle, " : ", dist)
                        
                        elif curr_angle < 135 and curr_angle > 46 :   
                            #print("il y a un obstacle à droite")
                            #print(curr_angle, " : ", dist)
                        
                        elif curr_angle < 315 and curr_angle > 226 :
                            #print("il y a un obstacle à gauche")
                            #print(curr_angle, " : ", dist)
                        
                        else :
                            #print("il y a un obstacle devant")
                            #print(curr_angle, " : ", dist)

                    # Remise à l'état Bas de la pin relier a la pin d'intruption pour que le robot puissent redémarre
                    GPIO.output(Pin_Stop,0)
            else :
                print("Failed to get Lidar Data")
            #time.sleep(1);

        # Arret et déconnéction du Lidar
        laser.turnOff();
    laser.disconnecting();


