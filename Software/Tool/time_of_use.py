import RPi.GPIO as gpio
import time
import signal
from datetime import datetime, timedelta


# GPIOs
tool_trig_pin = 22  # GPIO22
tool_on_led_pin = 23  # GPIO23

# "Time of use" timer variables
prev_val = 0
start_time = 0
accumulator = timedelta()
enable = True


def tool_trig_handler(pin):
    global prev_val
    global start_time
    global enable, accumulator
    tool_trig_pin_val = gpio.input(tool_trig_pin)
    time.sleep(0.1) # debouncing
    
    if (tool_trig_pin_val == gpio.input(tool_trig_pin)) & (prev_val != tool_trig_pin_val) & (enable):
        
        if tool_trig_pin_val:
            start_time = datetime.now()
            prev_val = 1
            gpio.output(tool_on_led_pin, True)
            print(f"start time {start_time}")
            
        elif ~tool_trig_pin_val:
            prev_val = 0
            gpio.output(tool_on_led_pin, False)
            retval = datetime.now() - start_time
            start_time = 0
            accumulator = accumulator + retval
            print(f"retval {retval}")
    

def tool_enable(enable_new_val):
    global enable, prev_val, start_time, accumulator
    
    enable = enable_new_val
    prev_val = 0
    
    if (not(enable)) and (type(start_time) != int):
        gpio.output(tool_on_led_pin, False)
        retval = datetime.now() - start_time
        start_time = 0
        accumulator = accumulator + retval
        print(f"retval {retval}") # for testing
        
    elif enable and (gpio.input(tool_trig_pin)):
        start_time = datetime.now()
        prev_val = 1
        gpio.output(tool_on_led_pin, True)
        print(f"start time {start_time}") # for testing
        
        
# GPIO initialization
# These are defined here becasue the callback tool_trig_handeler must be
# defined before running this section of code. Location marked with "# Here"
gpio.setmode(gpio.BCM) 
gpio.setup(tool_trig_pin, gpio.IN)
gpio.add_event_detect(tool_trig_pin, gpio.BOTH, callback=tool_trig_handler)  # Here

gpio.setup(tool_on_led_pin, gpio.OUT)
gpio.output(tool_on_led_pin, False)
    

if __name__=="__main__":
    try:
        while True:
            pass
    except:
        gpio.cleanup()
