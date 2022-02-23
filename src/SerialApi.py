from asyncore import read
from cmath import log
from ctypes.wintypes import BYTE
from socket import timeout
import time
import serial
import os
import csv


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


center_y = 160
center_x = 220

toleranceThreshold = 10

file = 'cord.csv'



def move(direction = ['SS']):
    with serial.Serial('COM4', 9800, timeout=1) as ser:
        time.sleep(0.5)
        ser.write(direction.encode())


def getDirection(row):
    direction = ""
    
    # UR Up Right
    # UL Up Left
    # DR Down Right
    # DL Down Left
    # US Up and no x movement
    # DS Down and no x movement
    # RS Right and no y movement
    # LS Left and no y movement
    # SS No movement

    # Cordinates are in the Y Center Cordinate Threshold
    if int(row[1]) > center_y - toleranceThreshold and int(row[1]) < center_y + toleranceThreshold:
        
        # Cordinates are in the X Center Cordinate Threshold
        if int(row[0]) > center_x - toleranceThreshold and int(row[0]) < center_x + toleranceThreshold:
            return "SS"
        # Stop Y Move Left
        elif int(row[0]) < center_x:
            return "LS"
        # Stop Y Move Right
        else:
            return 'RS'
            
    if int(row[1]) < center_y - toleranceThreshold:
        direction= 'U'
    
    elif int(row[1]) > center_y + toleranceThreshold:
        direction = 'D'
    
    # Cordinates are in the X Center Cordinate Threshold
    if int(row[0]) > center_x - toleranceThreshold or int(row[0]) < center_x + toleranceThreshold:
        return direction + "S"  # Stop X Movement and move on Y axis
    elif int(row[0]) > center_x + toleranceThreshold:
       return direction + 'R' # Move right and up or Down
    else :
        return direction + 'L' # Move Left and up or down
    

while True:
    with open(ROOT_DIR + "/" + file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')    
        for row in reader: 
            direction = getDirection(row)
            break
        csvfile.close();
        move(direction)
    time.sleep(1)
        

       
    