import serial
import socket

aD=serial.Serial('/dev/ttyACM0',9600)
while True:
    while(aD.inWaiting()==0):
        pass
    try:
        astring=str(aD.readline())
        astring=astring[2:]
        
        
