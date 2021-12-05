import os
import sys
sys.path.append(os.path.realpath('../functional_scripts'))

import RPi.GPIO as gpio
import time
import time_of_use as tou
import board
import busio
import adafruit_adxl34x
import Adafruit_DHT
from datetime import datetime, timedelta
import signal
import csv_manipulation as csvm

# Tool's memory file for sensor data
import shutil # need this too move "Tool_Memory.csv" to proper location
csv_file = "Tool_Memory.csv"
path_memory = "/home/pi/Documents/tooldump/"
path_flag_csv = "/home/pi/Documents/tooldump/flag.csv"


# Accelerometer Init
name_accel = "Accelerometer"
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer_obj = adafruit_adxl34x.ADXL345(i2c)
accelerometer_obj.enable_freefall_detection(threshold=10, 
                                            time=25)
accelerometer_obj.enable_motion_detection(threshold=18)
accelerometer_obj.enable_tap_detection(tap_count=1, 
                                       threshold=20, 
                                       duration=50, 
                                       latency=20, 
                                       window=255)


# Temp/Humidity sense Init
name_tempHum = "Temp/Humidity"
sensor = Adafruit_DHT.DHT11
tempHum_enable = True; 

# GPIOs
temp_data_pin = 27  # GPIO27 
led_enable = 24 # GPIO 24
led_disable = 25 # GPIO 25 

# initializing GPIO pins
gpio.setmode(gpio.BCM)
gpio.setup(led_enable, gpio.OUT)
gpio.setup(led_disable, gpio.OUT)
gpio.output(led_enable, True) # initialize enable led to off
gpio.output(led_disable, False) # initialize disable led as on


enable = False # Allows script to know if tool needs to be re-enabled once timer is refilled
interupt_flag = False
timer_time = 20 # Time the tool can opperate independantly of transponder
data_collect_time_delay = 1 # seconds


def enable_timerOut_handler(signum, frame):
    global interupt_flag
    interupt_flag = True    
    

signal.signal(signal.SIGALRM, enable_timerOut_handler)
signal.alarm(timer_time)
time_of_use = timedelta()

try:
    while True:
        # Checks to see if tool is allowed to be enabled
        if os.path.exists(path_flag_csv):
            signal.alarm(timer_time)
            os.remove(path_flag_csv)
            
            # enables the tool
            if enable == False:
                tou.tool_enable(True) # enable tool
                enable = True   
                gpio.output(led_enable, True)
                gpio.output(led_disable, False)
                
            # If timer is reset, then value of interupt flag should be reset to True
            if interupt_flag == True: 
                interupt_flag = False
        
        # Disables the tool
        if interupt_flag == True:
            interupt_flag = False
            tou.tool_enable(False) # disable tool
            gpio.output(led_enable, False)
            gpio.output(led_disable, True)
            enable = False
            
            
        time.sleep(data_collect_time_delay)
        
        # "Time of use" collection
        if tou.accumulator != timedelta(): # endures that accumulator is not empty before transfering data and reseting acc
            time_of_use = tou.accumulator
            tou.accumulator = timedelta()  # Resets accumulator
        
        # Accelerometer data collection
        accel = accelerometer_obj.acceleration
        accel_freefall = accelerometer_obj.events["freefall"]
        accel_colision = accelerometer_obj.events['tap']
        accel_motion = accelerometer_obj.events['motion']
        
        # Humidity/Temp data collection
        if tempHum_enable:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, temp_data_pin)
        
        # Timestamp
        stamp = datetime.now()
        # print("hit") # ttesting
        
        # Package to be sent to transponder
        if tempHum_enable:
            package = {'Transponder_ID':111111,
                       'Tool_ID':8846877,
                       'temp': temperature,
                        'humid': humidity,
                        'x': accel[0],
                        'y': accel[1],
                        'z': accel[2],
                        'freefall': accel_freefall,
                        'collision': accel_colision,
                        'Motion': accel_motion,
                        'Time_of_use': time_of_use,
                        'date': stamp.date(),
                        'time':stamp.time().strftime("%H:%M")}
            
        else:
            package = {'x': accel[0],
                       'y': accel[1],
                       'z': accel[2],
                       'freefall': accel_freefall,
                       'collision': accel_colision,
                       'Motion': accel_motion,
                       'Time_of_use': time_of_use,
                       'date': stamp.date(),
                       'time':stamp.time()}
                
        
        csvm.dict_to_csv(package, csv_file)
        
        # Resets time_of_use once recorded
        if time_of_use !=  timedelta():
            time_of_use =  timedelta()
        
        # checksa if "Tool_Memory.csv" already exists. If so, it concats
        # new data with banked data. else it moves new csv to memory locvation
        if not os.path.isfile(path_memory + csv_file):
            shutil.move(csv_file, path_memory)
        else:
            os.rename(csv_file, 'temp_tool.csv')
            shutil.move('temp_tool.csv', path_memory)
            csvm.csv_concat('/home/pi/Documents/tooldump', csv_file)
            os.remove(path_memory + 'temp_tool.csv')
        
        if tempHum_enable:
            print('temp :', package['temp'], "\n",
                  'humidity :', package['humid'], "\n",
                  'accel x :', package['x'], "\n",
                  'accel y :', package['y'], "\n",
                  'accel z :', package['z'], "\n",
                  "freefall :", package['freefall'], "\n",
                  "colision :", package['collision'], "\n",
                  "Motion :", package['Motion'], "\n",
                  "Time of use :", package['Time_of_use'], "\n",
                  "date :", package['date'], "\n",
                  "Time :", package['time'], "\n",
                  "==========================================")  # For testing

        else:
            print('accel x :', package['x'], "\n",
                  'accel y :', package['y'], "\n",
                  'accel z :', package['z'], "\n",
                  "freefall :", package['freefall'], "\n",
                  "colision :", package['colision'], "\n",
                  "Motion :", package['Motion'], "\n",
                  "Time of use :", package['Time_of_use'], "\n",
                  "date :", package['date'], "\n",
                  "Time :", package['time'], "\n",
                  "==========================================")        
        
        
except:
    print("exiting")
    gpio.cleanup()
    
gpio.cleanup()
