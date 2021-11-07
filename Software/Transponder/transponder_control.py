# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:57:47 2021

@author: clive
"""
import csv
import os

csv_file = "/home/pi/Hub/Memory/HubMemory/Tool_Memory.csv"
interesting_files = glob.glob("/home/pi/Hub/Memory/HubMemory/*.csv") 

while True:
    
    if os.path.isfile(csv_file):
        
        header_saved = False
        with open('/home/pi/Hub/Memory/HubMemory/output.csv','w') as fout:
            for filename in interesting_files:
                with open(filename) as fin:
                    header = next(fin)
                    if not header_saved:
                        fout.write(header)
                        header_saved = True
                    for line in fin:
                        fout.write(line)
        
        os.remove(csv_file)