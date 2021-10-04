import RPi.GPIO as gpio
import time_of_use as tou
import time
import board
import busio
import adafruit_adxl34x
import Adafruit_DHT
from datetime import datetime
import signal
import csv

# Accelerometer Init
name_accel = "Accelerometer"
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer_obj = adafruit_adxl34x.ADXL345(i2c)
accelerometer_obj.enable_freefall_detection(threshold=10, time=25)
accelerometer_obj.enable_motion_detection(threshold=18)
accelerometer_obj.enable_tap_detection(tap_count=1, threshold=20, duration=50, latency=20, window=255)


# Temp/Humidity sense Init
name_tempHum = "Temp/Humidity"
sensor = Adafruit_DHT.DHT11

# GPIOs
temp_data_pin = 14  # GPIO14 (pin 8) on pi

enable = True
interup_flag = False
timer_time = 10

def enable_timerOut_handler(signum, frame):
    global enable, interup_flag
    print('hit')
    enable = not(enable)
    interup_flag = True
    tou.tool_enable(enable)
    

signal.signal(signal.SIGALRM, enable_timerOut_handler)
signal.alarm(timer_time)
try:
    while True:
        # For testing (if statment)
        if interup_flag == True:
            interup_flag = False
            signal.alarm(timer_time)
            
        accel = accelerometer_obj.acceleration
        accel_freefall = accelerometer_obj.events["freefall"]
        accel_colision = accelerometer_obj.events['tap']
        accel_motion = accelerometer_obj.events['motion']
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, temp_data_pin)
        
        stamp = datetime.now()
        
        package = {'temp': temperature,
                   'humid': humidity,
                   'accel x': accel[0],
                   'accel y': accel[1],
                   'accel z': accel[2],
                   'freefall': accel_freefall,
                   'colision': accel_colision,
                   'Motion': accelerometer_obj.events['motion'],
                   'timestamp': stamp}
        print(package)  # For testing
        
        
        
except:
    print("exiting")
    gpio.cleanup()
    
gpio.cleanup()
