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
# name_accel = "Accelerometer"
# i2c = busio.I2C(board.SCL, board.SDA)
# accelerometer_obj = adafruit_adxl34x.ADXL345(i2c)

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
            
        
#         time.sleep(5) # for testing
#         enable = not(enable) # for testing
#         tou.tool_enable(enable)
#         accel = accelerometer_obj.acceleration
#         humidity, temperature = Adafruit_DHT.read_retry(sensor, temp_data_pin)
#         stamp = datetime.now()
#         package = {'temp': temperature,
#                    'humid': humidity,
#                    'accel x': accel[0],
#                    'accel y': accel[1],
#                    'accel z': accel[2],
#                    'timestamp': stamp}
        
        
        
except:
    print("exiting")
    gpio.cleanup()
    
gpio.cleanup()
