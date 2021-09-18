import RPi.GPIO as gpio
import time

#GPIO setup
chan = 17
gpio.setmode(gpio.BCM)
gpio.setup(chan, gpio.IN)

def callback(chan):
    print("Movment Detected")
        
gpio.add_event_detect(chan, gpio.BOTH, bouncetime=300)
gpio.add_event_callback(chan, callback)

while True:
    time.sleep(1)