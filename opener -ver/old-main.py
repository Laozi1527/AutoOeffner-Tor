import Rpi.GPIO as GPIO
import signal
import sys
import datetime
import threading
from time import sleep
from rpi_rf import RFDevice

rfdevice = None

def exithandler(signal, frame):
    rfdevice.cleanup()
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, exithandler)

rfdevice = RFDevice(27)
rfdevice.enable_rx()
timestamp = None

def scan():
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        #logging.info(str(rfdevice.rx_code) +
        #             " [pulselength " + str(rfdevice.rx_pulselength) +
        #             ", protocol " + str(rfdevice.rx_proto) + "]")
        return {"rx_code":rfdevice.rx_code ,"pulselength":rfdevice.rx_pulselength,"rx_proto":rfdevice.rx_proto}

relay_pin = 16
finish_time = None

GPIO.setup(relay_pin, GPIO.OUT, initial=GPIO.LOW)

def open_Door():
    global finish_time
    finish_time = datetime.datetime.now() + datetime.timedelta(seconds=30)
    if x.is_alive == False:
        GPIO.output(relay_pin, GPIO.HIGH)
        x.run()

def hold_open():
        while datetime.datetime.now <= finish_time:
            sleep(1)
        GPIO.output(relay_pin, GPIO.LOW)

x = threading.Thread(target=hold_open)


needed_values = {"rx_code":231312,"pulselength":"plus_minus_middle value---(int)","rx_proto":1}

while True:
    if scan() == needed_values:
        open_Door()

    sleep(0.01)