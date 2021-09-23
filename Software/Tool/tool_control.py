import RPi.GPIO as gpio
import time_of_use
import accelerometer



try:
    while True:
        accel = accelerometer_obj.acceleration
        print(f"acceleration: {accel}")
        
except:
    gpio.cleanup()
