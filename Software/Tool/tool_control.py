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

# Temp/Humidity sense Init
name_tempHum = "Temp/Humidity"
sensor = Adafruit_DHT.DHT11

# GPIOs
temp_data_pin = 14  # GPIO14 (pin 8) on pi

def enable_timerOut_handler(signum, frame):
    enable = not(enable)
    tou.tool_enable(enable)
    

enable = True
signal.signal(signal.SIGALM, enable_timerOut_handler)
signal.alarm(10)
try:
    while True:
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
