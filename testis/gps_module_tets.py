from time import sleep
import serial
import RPi.GPIO as GPIO
import signal
import sys

def exithandler(signal, frame):
    GPS_sensor.close()
    GPIO.cleanup()
    print("Cleaned up!")
    sys.exit(0)

signal.signal(signal.SIGINT, exithandler)

GPS_sensor = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS) # Serial Addresse anpassen!
sleep(1)

def get_GPS():
    if GPS_sensor.in_waiting > 0:
        new_data = GPS_sensor.readline()
        if new_data[0:6] == "$GPRMC":
            new_data1 = []
            new_data1.append(new_data)
            if new_data1[1] == "A":
                lat = new_data1[4],new_data1[5]
                lon = new_data1[6],new_data1[7]
            return lat, lon

print("Test different applications!\nGPS receiving and decoding:  1\nTransmitting opening signal:  2")
if input() == 1:
    while True:
        print(get_GPS())
else:
    pass