import RPi.GPIO as gpio
import time
from datetime import datetime

tool_trig = 21
prev_val = 0

gpio.setmode(gpio.BCM)
gpio.setup(tool_trig, gpio.IN)


# def start_tou(pin):
#     start_time = datetime.now().time()

# def stop_tou(pin):
#     time_of_use = datetime.now().time() - start_time
#     print (f"time of use = {time_of_use}")
    
def event_handler(pin):
    global prev_val
    tool_trig_val = gpio.input(tool_trig)
    print (f"prev: {prev_val}")
    print(f"trig: {tool_trig_val}")
    time.sleep(0.1)
    
    if (tool_trig_val == gpio.input(tool_trig)) & (prev_val != tool_trig_val):
        if tool_trig_val:
            start_time = datetime.now().time()
            prev_val = 1
            print(f"hit {gpio.input(tool_trig)}")
        elif ~tool_trig_val:
            prev_val == 0
            #print (f"prev changed to: {prev_val}")
            print(f"hit {gpio.input(tool_trig)}")
            #time_of_use = datetime.now().time() - start_time
            #print (f"time of use = {time_of_use}")
        

gpio.add_event_detect(tool_trig, gpio.BOTH, callback=event_handler)

# gpio.add_event_detect(tool_trig, gpio.RISING, callback=start_tou)
# gpio.add_event_detect(tool_trig, gpio.FALLING, callback=stop_tou)

try:
    while True:
        pass
except:
    gpio.cleanup()






