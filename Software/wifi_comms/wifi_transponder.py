# Import modules

import pexpect
import os
from os import path
import pathlib
import time
import multiprocessing
import subprocess
import re
import csv

def wifi_param_extract(filename_in):
    with open(filename_in, mode='r') as infile:
        reader = csv.reader(infile)
        with open('temp_params.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]:rows[1] for rows in reader}
    os.remove('temp_params.csv')
    return mydict

print("OK")
time.sleep(1)

#Are you testing on your computer or your Pi? 1 for Yes, 0 for No
MAC=0

# Extraction of initialization parameters
wifi_params = wifi_param_extract(path.realpath('../../../wifi_params.csv'))
#What is your pi password?
Password = wifi_params["Password"]

#What are the Pi IPs?
IP_src = wifi_params["IP_src"] #"10.0.0.198"
IP_dest = wifi_params["IP_dest"]#"10.0.0.112"

#What minium signal power do you want? less than -60dBm is very weak
Signal_Power= '-70'

#What is the name of the tool memory file that we pass to the transponder?
Memory_name="Tool_Memory.csv"

#Set these path parameters for testing purposes:
# dest_filename = Memory_name
# dest_path = os.path.realpath("../wifi_comms/Memory/")
# src_path = "/home/pi/Hub/Memory/HubMemory"

src_filename = "/home/Tool/Documents/tooldump/"+ Memory_name
src_path = "/home/Tool/Documents/tooldump"
dest_path = os.path.realpath("../wifi_comms/Memory/")
MACPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory/HubMemory"
MACFlagPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory"


#if MAC flag is set to 1, then the path corresponds to the MAC path, if 0, then the Pi path
if MAC ==1:
    path = MACPath
    FlagPath = MACFlagPath
else:
    path = dest_path
    FlagPath = dest_path
    

#This function checks if the timmer has set a flag file called flag.csv, then pushes it to the tool memory, then deletes it.
def flag():
    print("flag function running")
    file = pathlib.Path(FlagPath +"/flag.csv") #Checks if the flag file exists
    if file.exists ():
        print("Flag file found")
        output = pexpect.run("scp " + FlagPath +"/flag.csv Tool@"+ IP_src +":"+ src_path, events={'(?i)password':""+ Password +"\n"})
        print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
        time.sleep(1)
        os.remove(FlagPath + "/flag.csv")
        print("Flag file deleted\n")
    else:
        print("No flag file found\n")

    time.sleep(1)

#This function scp's into the tool and grabs all the tool data dumps and brings it to the hub deleting all other copies
def Retreive():

    print ("Running Retreive() function")

    output = pexpect.run("scp pi@"+ IP_src +":"+ src_filename + " "+ path, events={'(?i)password':""+ Password +"\n"})
    print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
    time.sleep(1)
    print("Tool memory file retreived")


#List the amount of data dump files by login through ssh
def ConnectionTest():
    flag()
    print("\nRunning ConnectionTest()\n")
    
    output = pexpect.run("ssh pi@" + IP_src +" 'ls "+ src_path +" '", events={'(?i)password':""+ Password +"\n"})
    print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
    #os.system("nick")
    print("\nConnection established\n")
    time.sleep(1)

    SignalStrength()
    Retreive()


#Check Wifi Connection Strength in dBm
def SignalStrength():    
    if MAC ==1:
        Wifi = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I"], shell=True, stderr=subprocess.DEVNULL)
        sentence=str(Wifi)
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
        firstnumber = ( "% d" + "dBm.") % s[0]
        print("The Wifi signal power is: " + str(firstnumber))
        time.sleep(1)
       

        #Check if Wifi signal is strong enough
        if s[0] < float(Signal_Power):
            print("Wifi signal is to weak, cannot transfer data")
            time.sleep(1)
            quit()
    else:
        Wifi=[]
        Wifi = subprocess.check_output(["iwconfig"], shell=True, stderr=subprocess.DEVNULL)
        sentence=str(Wifi)
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
        firstnumber = ( "% d" + "dBm.") % s[12]
        print("The Wifi signal power is: " + str(firstnumber))
        time.sleep(1)

#Loop will run forever
while True:          
    ConnectionTest()
    
