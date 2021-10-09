# Import modules

import pexpect
import os
from os import path
import pathlib
import time
import multiprocessing
import subprocess
import re

print("Hub Wifi Script")
time.sleep(1)

#Are you testing on your computer or your Pi? 1 for Yes, 0 for No
MAC=1

#What is your pi password?
Password ='nick'

#What are the Pi IPs?
IP_Transponder="192.168.0.28"

#What minium signal power do you want? less than -60dBm is very weak
Signal_Power= '-70'

#What is the name of the tool memory file that we pass to the transponder?
Memory_name="Hub_Memory.csv"

#Set these path parameters for testing purposes:
TransponderFile = "/home/pi/Hub/Memory/HubMemory/"+ Memory_name
TransponderPath = "/home/pi/Hub/Memory/HubMemory"
MACPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory/HubMemory"  # This is your hub technically
#MACFlagPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory"


#if MAC flag is set to 1, then the path corresponds to the MAC path, if 0, then the Pi path
if MAC ==1:
    path = MACPath
    #FlagPath = MACFlagPath
else:
    path = MACPath
    #FlagPath = TransponderPath


    #This function checks if the timmer has set a flag file called flag.csv, then pushes it to the tool memory, then deletes it.
##    def flag():
##        print("flag function running")
##        file = pathlib.Path(FlagPath +"/flag.csv") #Checks if the flag file exists
##        if file.exists ():
##            print("Flag file found")
##            output = pexpect.run("scp " + FlagPath +"/flag.csv pi@"+ IP_Tool +":"+ ToolPath, events={'(?i)password':""+ Password +"\n"})
##            print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
##            time.sleep(1)
##            os.remove(FlagPath + "/flag.csv")
##            print("Flag file deleted\n")
##        else:
##            print("No flag file found\n")
##
##        time.sleep(1)



#This function scp's into the transpnder and grabs all the transponder data dumps and brings it to the hub deleting all other copies
def Retreive():

    print ("Running Retreive() function")

    output = pexpect.run("scp pi@"+ IP_Transponder +":"+ TransponderFile + " "+ path, events={'(?i)password':""+ Password +"\n"})
    print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
    time.sleep(1)
    print("Tool memory file retreived")


#List the amount of data dump files by login through ssh
def ConnectionTest():
    #flag()
    print("\nRunning ConnectionTest()")
    
    output = pexpect.run("ssh pi@" + IP_Transponder +" 'ls "+ TransponderPath +" '", events={'(?i)password':""+ Password +"\n"})
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
        

ConnectionTest()

