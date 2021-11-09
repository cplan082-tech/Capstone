# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:05:01 2021

@author: clive
"""
import csv
import os
import glob
import shutil
import sys
sys.path.append(os.path.realpath('..\\..\\functional_scripts'))

import csv_manipulation as csvm


# def dict_to_csv(package):
#     try:
#         if os.path.isfile(csv_file):
#             file_exists = True
#         else:
#             file_exists = False
            
#         with open(csv_file, 'a', newline='') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=list(package.keys()))
            
#             if not file_exists:
#                 writer.writeheader()
                
#             writer.writerow(package)
            
#             csvfile.close()
            
#     except IOError:
#         print("I/O error")
        
        
        
# file1 = open("")
        
        
csv_file = "foldertest/test1.csv"  
package = {'temp': 10,
            'humid': 10,
            'accel x': 10,
            'accel y': 10,
            'accel z': 10,
            'freefall': 10,
            'colision': 10,
            'Motion': 'accel_motion',
            'Time_of_use': 'time_of_use',
            'timestamp': 10}

csvm.dict_to_csv(package, csv_file)


csv_file = "foldertest/test2.csv"  
package = {'temp': 12,
            'humid': 20,
            'accel x': 40,
            'accel y': 10,
            'accel z': 10,
            'freefall': 30,
            'colision': 10,
            'Motion': 'bitch',
            'Time_of_use': 'time_of_use',
            'timestamp': 10}

csvm.dict_to_csv(package, csv_file)




        
# file1 = open("foldertest/test1.csv", "a")
# file2 = open("foldertest/test2.csv", "r")

# for line in file2:
#    file1.write(line)

# file1.close()
# file2.close()


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

path = 'foldertest/'
filename_output = 'output.csv'
csv_concat(path, filename_output)

filename_in = path + filename_output

def wifi_param_extract(filename_in):
    with open(filename_in, mode='r') as infile:
        reader = csv.reader(infile)
        with open('temp_params.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]:rows[1] for rows in reader}
    os.remove('temp_params.csv')
    return mydict

dic = wifi_param_extract(filename_in)
print(dic["temp"])



# sample_dict = [
# {'key1': 1, 'key2': 2, 'key3': 3},
# {'key1': 4, 'key2': 5, 'key3': 6},
# {'key1': 7, 'key2': 8, 'key3': 9},
# ]

# col_name=["key1","key2","key3"]
# with open("export.csv", 'w') as csvFile:
#         wr = csv.DictWriter(csvFile, fieldnames=col_name)
#         wr.writeheader()
#         for ele in sample_dict:
#             wr.writerow(ele)