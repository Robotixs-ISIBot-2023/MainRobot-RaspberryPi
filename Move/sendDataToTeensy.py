import smbus
import struct
import os

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
print(" @NoWayCall                                                                   28/03/23") 
print("=======================================================================================") 
 
# Affichage des commandes possibles 
print("10000 = Avancer / 20000 = Reculer") 
print("30000 = Rotation Horaire / 40000 = Rotation Anti-Horaire") 
print("50000 = STOP / 60000 = EMERGENCYSTOP") 
print("---------------------------------------------------------------------------------------") 
print("Remarques: ") 
print("") 
print("STOP : Décélère les moteurs et attend que les moteurs soient arrêtés (fct. blocante).") 
print("") 
print("EMERGENCYSTOP : Arrête immédiatement les moteurs.") 
print("N'utilisez cette fonction qu'en cas d'urgence car, selon la vitesse du moteur,") 
print("elle entraînera probablement des pertes de pas.")  
print("Une séquence de 'Homing' est fortement recommandée après un arrêt d'urgence.") 
print("---------------------------------------------------------------------------------------") 
print("Pour commander il suffit d'envoyer une valeur + la valeur désirée en mm ou degrés.") 
print("Exemple: Avancer de 200mm => 10200. Tourner de 45° dans le sens horaire => 30045") 
print("=======================================================================================") 
print("") 
print("=> Commande ?")

# Adresse du périphérique I2C
DEVICE_ADDR = 0x0a

# Créer un objet I2C bus
bus = smbus.SMBus(1)

# Définir la structure de données
# data = (10500)

def sendToTeensy(cmd):
    try:
        global bus, DEVICE_ADDR
        data = struct.pack('>H', cmd)
        bus.write_i2c_block_data(DEVICE_ADDR, 0, list(data)) # Envoyer les bytes sur l'adresse du périphérique I2C
    except:
        print("[DEBUG] Failed to send data")

if __name__ == '__main__':
    while True: 
        Commande = int(input("Entrez un entier : "))
        #data = struct.pack('>H', Commande)
        # Envoyer les bytes sur l'adresse du périphérique I2C
        #bus.write_i2c_block_data(DEVICE_ADDR, 0, list(data)) 
        sendToTeensy(Commande)
