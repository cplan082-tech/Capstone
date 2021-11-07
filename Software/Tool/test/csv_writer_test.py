# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:05:01 2021

@author: clive
"""
import csv
import os

csv_file = "test.csv"


def dict_to_csv(package):
    try:
        if not os.path.isfile(csv_file):
            file_exists = True
        else:
            file_exists = False
            
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(package.keys()))
            
            if not file_exists:
                writer.writeheader()
                
            writer.writerow(package)
            
            csvfile.close()
            
    except IOError:
        print("I/O error")
        
        
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

dict_to_csv(package)

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

dict_to_csv(package)




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