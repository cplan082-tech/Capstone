import RPi.GPIO as gpio
import time
from datetime import datetime

tool_trig_pin = 21
prev_val = 0
start_time = 0
    
def event_handler(pin):
    global prev_val
    global start_time
    tool_trig_pin_val = gpio.input(tool_trig_pin)
    time.sleep(0.1) # debouncing
    
    if (tool_trig_pin_val == gpio.input(tool_trig_pin)) & (prev_val != tool_trig_pin_val):
        print('hit')
        if tool_trig_pin_val:
            start_time = datetime.now()
            prev_val = 1
            print(f"start time {start_time}")
        elif ~tool_trig_pin_val:
            prev_val = 0
            retval = datetime.now() - start_time
            print(f"retval {retval}")
    else:  # else is only for testing
        print(f"tool_trig_pin_val: {tool_trig_pin_val}")
        print(f"gpio.input(tool_trig_pin): {gpio.input(tool_trig_pin)}")
        print(f"prev_val: {prev_val}")
        print(f"tool_trig_pin_val: {tool_trig_pin_val}")
        
gpio.setmode(gpio.BCM)
gpio.setup(tool_trig_pin, gpio.IN)
gpio.add_event_detect(tool_trig_pin, gpio.BOTH, callback=event_handler)

if __name__=="__main__":
    try:
        while True:
            pass
    except:
        gpio.cleanup()






