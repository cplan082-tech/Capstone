import RPi.GPIO as gpio
import time_of_use
import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer_obj = adafruit_adxl34x.ADXL345(i2c)



try:
    while True:
        accel = accelerometer_obj.acceleration
        print(f"acceleration: {accel}")
        
except:
    gpio.cleanup()
