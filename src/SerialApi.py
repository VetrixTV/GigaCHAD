from cmath import log
from ctypes.wintypes import BYTE
from socket import timeout
import time
import serial
import os
import csv


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

global initial_y = 0
global initial_x = 0

global center_y = 0
global center_x = 0

global initial_run = True

file = 'cord.csv'

def initialize(row):
    center_y = row[0]
    center_x = row[1]
    initial_run = False

def move(direction = ['S']):
    with serial.Serial('COM4', 9800, timeout=1) as ser:
        for com in direction:
            time.sleep(0.5)
            ser.write(bytes(b"".join(com)))


def getDirection(row):
    direction = []

    if row[1] < center_x + 10 and row[1] > center_x - 10:
        direction.append('XS')
    elif row[1] > center_x:
       direction.append('R')
    else row[1] < center_x:
        direction.append('L')

    row[0] < center_y + 10 and row[0] > center_y - 10:
        direction.append('YS')
    elif row[0] > center_y:
       direction.append('U')
    else row[0] < center_y:
        direction.append('D')
    return direction
    

# while True:
with open(ROOT_DIR + "/" + file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        if initial_run:
            initialize(row)
            time.sleep(10)
            break
    
        break

       
    