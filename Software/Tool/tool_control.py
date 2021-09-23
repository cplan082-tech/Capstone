import RPi.GPIO as gpio
import time_of_use
import time
import board
import busio
# import pandas as pd
import adafruit_adxl34x
import Adafruit_DHT
from datetime import datetime
# from pandas import DataFrame
import csv

# Accelerometer Init
name_accel = "Accelerometer"
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer_obj = adafruit_adxl34x.ADXL345(i2c)

# Temp/Humidity sense Init
name_tempHum = "Temp/Humidity"
sensor = Adafruit_DHT.DHT11

# GPIO14 (pin 8) on pi
data_pin_temp = 14


try:
    while True:
        time.sleep(0.5)
        accel = accelerometer_obj.acceleration
        humidity, temperature = Adafruit_DHT.read_retry(sensor, data_pin_temp)
        stamp = datetime.now()
        package = {'temp': temperature,
                   'humid': humidity,
                   'accel x': accel[0],
                   'accel y': accel[1],
                   'accel z': accel[2],
                   'timestamp': stamp}
#         df = DataFrame(data=package)
#         print(df)
#         print(f"acceleration: {accel}")
#         print(f"Temp: {temperature}")
#         print(f"Hum: {humidity}")
        
        
        
except:
    print("exiting")
    gpio.cleanup()
