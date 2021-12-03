# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:03:33 2021

@author: clive
"""
import csv
import os
import glob
import shutil

def csv_concat(path, filename_output):
    interesting_files = glob.glob(path + "*.csv")  
    header_saved = False
    
    with open(filename_output,'w') as fout:
        for filename in interesting_files:
            with open(filename) as fin:
                header = next(fin)
                if not header_saved:
                    fout.write(header)
                    header_saved = True
                for line in fin:
                    fout.write(line)
    if os.path.isfile(path + filename_output):
        os.remove(path + filename_output)                
    shutil.move(filename_output, path)
    
    
    
def dict_to_csv(package, csv_file):
    try:
        # Checks if csv files already exists. If not, the first row of the csv 
        # will be a header
        if os.path.isfile(csv_file):
            file_exists = True
        else:
            file_exists = False
            
        with open(csv_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(package.keys()))
            
            if not file_exists:
                writer.writeheader()
                
            writer.writerow(package)
            
            csvfile.close()
            
    except IOError:
        print("I/O error")
            
        

def wifi_param_extract(filename_in):
    with open(filename_in, mode='r') as infile:
        reader = csv.reader(infile)
        with open('temp_params.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]:rows[1] for rows in reader}
    os.remove('temp_params.csv')
    return mydict


def enable_timer_extract(filename_in):
    with open(filename_in, mode='r') as infile:
        reader = csv.reader(infile)
        with open('temp.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            timer_val = [rows[0] for rows in reader]
        os.remove('temp.csv')
        return int(timer_val)
        