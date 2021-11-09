# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:57:47 2021

@author: clive
"""
import os
import sys
sys.path.append(os.path.realpath('../functional_scripts'))
import csv_manipulation as csvm

path_memory = "/home/pi/Hub/Memory/HubMemory/"
csv_file = "Tool_Memory_acumulator.csv"
csv_file_input = "Tool_Memory.csv"

# We just want to create a flag csv, we don't care what's in it
# FOR TESTING
csvm.dict_to_csv({'place': 'holder'}, os.path.realpath('../wifi_comms/Memory/') # TODO: remove thisjs

while True:
    
    # Checks if any new data has been recieved
    if os.path.isfile(csv_file_input):
        csvm.csv_concat(path_memory, csv_file) # updates accumulator
        os.remove(path_memory + csv_file_input) # Deletes old data
        
     