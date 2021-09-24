# Import pexpect module

import pexpect
import os
import time
import multiprocessing
import subprocess
import re

#Are you testing on your computer or your Pi? 1 for Yes, 0 for No
MAC=1

#Set these path parameters for testing purposes:
ToolFile = "/home/pi/Documents/tooldump/Hub_Memory.csv"
ToolPath = "/home/pi/Hub/Memory/HubMemory"
MACPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory/HubMemory"

#if MAC flag is set to 1, then the path corresponds to the MAC path, if 0, then the Pi path
if MAC ==1:
    path = MACPath
else:
    path = ToolPath


count=0
#List the amount of data dump files by login through ssh

def ConnectionTest():
    
    print("Running ConnectionTest()")
    
    output = pexpect.run("ssh pi@192.168.0.55 'ls /home/pi/Documents/tooldump' ", events={'(?i)password':'nick\n'})
    string=str(output)
    substring = "data"
    count = string.count(substring)
##    print("The count of data files in the tool is:", count)
    print("Connection established")

    SignalStrength()
    Retreive()


#Check Wifi Connection Strength in dBm

def SignalStrength():    
    if MAC ==1:
        Wifi = subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I", shell=True)
        sentence=str(Wifi)
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
        firstnumber = ( "% d" + "dBm.") % s[0]
        print("The Wifi signal power is: " + str(firstnumber))
        time.sleep(1)


#Runs a subprocess to monitor a GOOD wifi connection, if not it reports it to the user. 
if __name__ == '__main__':
    p = multiprocessing.Process(target=ConnectionTest)
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(10)

    # If thread is still active
    if p.is_alive():
        print ("Connection Timed Out - No Wifi Connection Established")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        #p.kill()
        p.join()
        

#This function scp's into the tool and grabs all the tool data dumps and brings it to the hub
def Retreive():

##    files = count
##    files =int(files)
##    print("We have found this many data dumps:", files)
##    i=1
    
    print ("Running Retreive() function")

##    while i <= files :
##
##        output = pexpect.run("scp pi@192.168.0.29:/home/pi/Documents/tooldump/data{}.csv ".format(i) + path, events={'(?i)password':'nick\n'})
##        print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
##        time.sleep(0.1)
##
##        i=i+1

#This scp will grab the Hub_Memory.csv file from the pi, then bring it locally and replace any existing file (always most current version)
    output = pexpect.run("scp pi@192.168.0.29:/home/pi/Documents/tooldump/Hub_Memory.csv "+ path, events={'(?i)password':'nick\n'})
    print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
    time.sleep(1)



