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

toleranceThreshold = 19 #threshold for the face recognition

file = 'cord.csv'



def move(direction = ['SS']):
    with serial.Serial('COM4', 9800, timeout=1) as ser: #create serial connection 
        time.sleep(0.5)
        ser.write(direction.encode()) # send movement command


def getDirection(row):
    
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
    #Y threshhold * 1.5 because the Y coordinate span is smaller than the X coordinate span
    if int(row[1]) > (center_y - int(toleranceThreshold * 1.5)) and int(row[1]) < (center_y + int(toleranceThreshold * 1.5)):
        
        # Cordinates are in the X Center Cordinate Threshold
        if int(row[0]) > center_x - toleranceThreshold and int(row[0]) < center_x + toleranceThreshold:
            return "SS"
        # Stop Y Move Left
        elif int(row[0]) < center_x:
            return "LS"
        # Stop Y Move Right
        else:
            return 'RS'
            
    if int(row[1]) < (center_y - int(toleranceThreshold * 1.5)):
        direction= 'U'
    
    elif int(row[1]) > (center_y + int(toleranceThreshold * 1.5)):
        direction = 'D'
    
    # Cordinates are in the X Center Cordinate Threshold
    if int(row[0]) > center_x - toleranceThreshold or int(row[0]) < center_x + toleranceThreshold:
        return direction + "S"  # Stop X Movement and move on Y axis
    elif int(row[0]) > center_x + toleranceThreshold:
       return direction + 'R' # Move right and up or Down
    else :
        return direction + 'L' # Move Left and up or down
    

#Main, handles the logic
while True:
    with open(ROOT_DIR + "/" + file, newline='') as csvfile: # Open the CSC with reading permission
        reader = csv.reader(csvfile, delimiter=';')   # Create the Reader instance
        for row in reader: 
            direction = getDirection(row) # get direction from the file
            break
        csvfile.close(); 
        move(direction) # call move function with the direction command
    time.sleep(1)
        

       
    