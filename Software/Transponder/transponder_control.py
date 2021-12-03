# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:57:47 2021

@author: clive
"""
import os
import sys
sys.path.append(os.path.realpath('../functional_scripts'))
import signal
import csv_manipulation as csvm

# path_memory = "/home/pi/Hub/Memory/HubMemory/"
path_enable_flag = os.path.realpath('../wifi_comms/Memory/flag.csv')
path_memory = path_enable_flag
filename_sensor_data_bank = "Tool_Memory_acumulator.csv"
filename_sensor_data_bank_input = "Tool_Memory.csv"
filename_enable_timer_input = "Update_Timer.csv"

# We just want to create a flag csv, we don't care what's in it
# FOR TESTING
# csvm.dict_to_csv({'place': 'holder'}, path_enable_flag) # TODO: remove thisjs
interupt_flag = False


def enable_timerOut_handler(signum, frame):
    global interupt_flag
    interupt_flag = True

signal.signal(signal.SIGALRM, enable_timerOut_handler)


while True:
    
    # Checks if any new data has been recieved
    if os.path.isfile(filename_sensor_data_bank_input):
        csvm.csv_concat(path_memory, filename_sensor_data_bank) # updates accumulator (data banks)
        os.remove(path_memory + filename_sensor_data_bank_input) # Deletes old data
    
    # Timer depleted. Disable tool
    if interupt_flag == True:
        interupt_flag = False
        os.remove(path_enable_flag)
    
    # Checks if new timer value recieved from hub

    if os.path.exists(path_memory + filename_enable_timer_input):
        enable_timer_val = csvm.enable_timer_extract(path_memory + filename_enable_timer_input)
        signal.alarm(enable_timer_val)
        os.remove(path_memory + filename_enable_timer_input)
        
        if not os.path.exists(path_enable_flag): # Ensures that flag.csv exists
            csvm.dict_to_csv({'place': 'holder'}, path_enable_flag)
        