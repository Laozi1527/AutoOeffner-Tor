from time import sleep
import serial
import RPi.GPIO as GPIO
import threading
import datetime
import signal
import sys

def exithandler(signal, frame):
    Rf.close()
    GPIO.cleanup()
    print("Cleaned up!")
    sys.exit(0)

signal.signal(signal.SIGINT, exithandler)

RELAY_PIN = 16
GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.LOW) #Relay
Rf = serial.Serial('/dev/ttyAMA0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS) # Serial Addresse anpassen!
sleep(1)

def readIncoming():
    if Rf.in_waiting > 0:
        return Rf.readline()

def open_Door():
    global finish_time
    finish_time = datetime.datetime.now() + datetime.timedelta(seconds=30)
    if x.is_alive == False:
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        x.run()

def hold_open():
        while datetime.datetime.now <= finish_time:
            sleep(1)
        GPIO.output(RELAY_PIN, GPIO.LOW)

x = threading.Thread(target=hold_open)

try:
    while True:
        if readIncoming() == "code":
             open_Door()

        sleep(0.1)

except not KeyboardInterrupt:
     exithandler()
