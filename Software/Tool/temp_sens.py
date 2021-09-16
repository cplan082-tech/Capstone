#!/usr/bin/env python3

import sys
import argparse
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

# GPIO14 (pin 8) on pi
data_pin = 14

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fahrenheit", help="output temperature in Fahrenheit", action="store_true")

    return parser.parse_args()

def celsius_to_fahrenheit(degrees_celsius):
        return (degrees_celsius * 9/5) + 32

def main():
    args = parse_args()

    while True:
        try:
            # Gather the humidity and temperature
            # data from the sensor; GPIO Pin 4
            humidity, temperature = Adafruit_DHT.read_retry(sensor, data_pin)

        except RuntimeError as e:
            # GPIO access may require sudo permissions
            # Other RuntimeError exceptions may occur, but
            # are common.  Just try again.
            print(f"RuntimeError: {e}")
            print("GPIO Access may need sudo permissions.")

            time.sleep(2.0)
            continue

        if args.fahrenheit:
            print("Temp: {0:0.1f}*F, Humidity: {1:0.1f}%".format(celsius_to_fahrenheit(temperature), humidity))
        else:
            print("Temp:{0:0.1f}*C, Humidity: {1:0.1f}%".format(temperature, humidity))

        time.sleep(2.0)

if __name__ == "__main__":
    main()