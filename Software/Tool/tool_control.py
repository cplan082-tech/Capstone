import time_of_use
import accelerometer



try:
    while True:
        accel = accelerometer.acceleration
        print(f"acceleration: {accel}")
        
except:
    gpio.cleanup()
