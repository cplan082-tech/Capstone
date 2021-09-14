
import json
import csv
from csv import DictReader

###########################################################################

'''
Purpose: This function returns the fieldnames of the CSV file
'''
def csv_get_fieldnames(csvFilePath):
    # opening the csv file
    with open(csvFilePath) as csv_file:
        # creating an object of csv reader with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter = ',')
        # list to store the names of columns
        fieldnames = []
        # loop to iterate thorugh the rows of csv
        for row in csv_reader:
            # adding the first row
            fieldnames.append(row)
            # breaking the loop after the first iteration itself
            break
    fieldnames = fieldnames[0]      
    return fieldnames

###########################################################################

'''
Purpose: This function writes data to a specified csv file
'''

def write_to_csv_file(csvFilePath, myData, fieldnames):
    with open(csvFilePath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(myData)

###########################################################################

'''
Purpose: This function converts a csv file to json format
'''      

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

###########################################################################

