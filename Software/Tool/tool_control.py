import RPi.GPIO as gpio
import time_of_use
import time
import board
import busio
import adafruit_adxl34x
import Adafruit_DHT
from datetime import datetime

# Accelorometer Init
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer_obj = adafruit_adxl34x.ADXL345(i2c)

# Temp/Humidity sense Init
sensor_name = "Temp/Humidity"
sensor = Adafruit_DHT.DHT11

# GPIO14 (pin 8) on pi
data_pin = 14


try:
    while True:
        time.sleep(0.5)
        accel = accelerometer_obj.acceleration
        humidity, temperature = Adafruit_DHT.read_retry(sensor, data_pin)
        print(f"acceleration: {accel}")
        print(f"Temp: {temperature}")
        print(f"Hum: {humidity}")
        
        
        
except:
    gpio.cleanup()
