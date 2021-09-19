import RPi.GPIO as gpio
import time
from datetime import datetime

tool_trig = 21
gpio.setmode(gpio.BCM)
gpio.setup(tool_trig, gpio.IN)


def start_tou(pin):
    start_time = datetime.now().time()

def stop_tou(pin):
    time_of_use = datetime.now().time() - start_time
    print (f"time of use = {time_of_use}")

gpio.add_event_detect(tool_trig, gpio.RISING, callback=start_tou)
gpio.add_event_detect(tool_trig, gpio.FALLING, callback=stop_tou)

try:
    while True:
        pass
except:
    gpio.cleanup()




