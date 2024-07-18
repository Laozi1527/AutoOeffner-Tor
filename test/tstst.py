from time import sleep
import serial
import RPi.GPIO as GPIO
import signal
import sys

def exithandler(signal, frame):
    GPS_sensor.close()
    GPIO.cleanup()
    logs.close()
    print("Cleaned up!")
    sys.exit(0)

signal.signal(signal.SIGINT, exithandler)

def get_GPS():
    if GPS_sensor.in_waiting > 0:
        new_data = GPS_sensor.readline()
        if new_data.startswith("$GPRMC"):
            print(new_data)


logs = open("logs.txt", mode="w")
GPS_sensor = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS) # Serial Addresse anpassen!
sleep(1)
while True:
    #if GPS_sensor.in_waiting > 0:
    #        logs.write(GPS_sensor.readline())
    get_GPS()
    sleep(0.1)
            


