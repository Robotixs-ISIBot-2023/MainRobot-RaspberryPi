import os
import time
import ydlidar
#from YDLidar-SDK.setup import *
import math
import RPi.GPIO as GPIO
import sys


# Parametrage pin d'intéruption pour le moteur
GPIO.setmode(GPIO.BOARD)
Pin_Stop = 11

GPIO.setup(Pin_Stop, GPIO.OUT)
GPIO.output(Pin_Stop,0)  #Level LOW


Taille_Robot = 25
Distance_Securite = 80  #a peu prés 30 cm


while True :
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
        scan = ydlidar.LaserScan();
        while ret and ydlidar.os_isOk():
            r = laser.doProcessSimple(scan);
            if r:
                for p in scan.points:
                    curr_angle = int(math.degrees(p.angle)+180)
                    dist = (p.range)*254 # 1 ich = 25.4 mm  *0.0254*10*1000 #Il renvoie le range en 1/10 de inches, *0.0254 => to dm, *10 to m, *1000 to mm
                    if dist <= Distance_Securite and dist != 0:
                        if curr_angle < 225 and curr_angle > 136 or curr_angle < 46 and curr_angle > 0 or curr_angle < 359 and curr_angle > 315 :
                            GPIO.output(Pin_Stop,1)

                    GPIO.output(Pin_Stop,0)
            else :
                print("Failed to get Lidar Data")
            #time.sleep(1);
        laser.turnOff();
    laser.disconnecting();


