from time import sleep
import serial
import RPi.GPIO as GPIO
import signal
import sys

def exithandler(signal, frame):
    GPS_sensor.close()
    Rf.close()
    GPIO.cleanup()
    print("Cleaned up!")
    sys.exit(0)

signal.signal(signal.SIGINT, exithandler)

Rf = serial.Serial('/dev/ttyAMA0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS) # Serial Addresse anpassen!
sleep(1)
GPS_sensor = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS) # Serial Addresse anpassen!
sleep(1)

def send_message():
    Rf.write("code")

def convert_to_decimal(coord, direction):
    coord = float(coord)
    degrees = int(coord // 100)
    minutes = coord % 100
    decimal_degrees = degrees + (minutes / 60)
    if direction in ['S', 'W']:
        decimal_degrees *= -1
    return decimal_degrees

def get_GPS_cords(Data):
    if Data.startswith(b"$GPRMC"):
        parts = Data.split(b",")
        if parts[2] == b"A":
            lattitude = parts[3].decode('utf-8')
            latitude_direction = parts[4].decode('utf-8')
            longitude = parts[5].decode('utf-8')
            longitude_direction = parts[6].decode('utf-8')
            return (convert_to_decimal(lattitude, latitude_direction)),(convert_to_decimal(longitude, longitude_direction))
    return None, None

while True:
    if GPS_sensor.in_waiting > 0:
        lattitude, longitude = get_GPS_cords(GPS_sensor.readline())
    print("Lattitude:",lattitude,"\nLongitude:",longitude)
    sleep(0.1)



