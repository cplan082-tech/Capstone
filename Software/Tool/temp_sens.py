#!/usr/bin/env python3

import sys
import argparse
import time
import Adafruit_DHT
from datetime import datetime

sensor_name = "Temp/Humidity"
sensor = Adafruit_DHT.DHT11

# GPIO14 (pin 8) on pi
data_pin = 14


def main():
    prev = datetime.now().time()
    while True:
        try:
            # Gather the humidity and temperature
            # data from the sensor; GPIO Pin 14
            humidity, temperature = Adafruit_DHT.read_retry(sensor, data_pin)
            stamp = datetime.now()

        except RuntimeError as e:
            # GPIO access may require sudo permissions
            # Other RuntimeError exceptions may occur, but
            # are common.  Just try again.
            print(f"RuntimeError: {e}")
            print("GPIO Access may need sudo permissions.")

            time.sleep(2.0)
            continue

        package = (sensor_name, temperature, humidity, stamp)
       
        #print("Temp:{0:0.1f}*C, Humidity: {1:0.1f}%".format(temperature, humidity))
        
        print(package[3].time().hour)
        #print(package[3].time() - prev)
        prev = package[3].time()

        time.sleep(2.0)

if __name__ == "__main__":
    main()