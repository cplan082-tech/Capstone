# Import modules

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
TransponderPath = "/home/pi/Hub/Memory/HubMemory"
MACPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory/HubMemory"

#if MAC flag is set to 1, then the path corresponds to the MAC path, if 0, then the Pi path
if MAC ==1:
    path = MACPath
else:
    path = TransponderPath


#Loop will run 1000 times
i=0
while i<1000:
    i=i+1
    #This function scp's into the tool and grabs all the tool data dumps and brings it to the hub deleting all other copies
    def Retreive():

        print ("Running Retreive() function")

        output = pexpect.run("scp pi@192.168.0.29:/home/pi/Documents/tooldump/Hub_Memory.csv "+ path, events={'(?i)password':'nick\n'})
        print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
        time.sleep(10)


    #List the amount of data dump files by login through ssh
    def ConnectionTest():
        print("Running ConnectionTest()")
        
        output = pexpect.run("ssh pi@192.168.0.29 'ls /home/pi/Documents/tooldump' ", events={'(?i)password':'nick\n'})
        print("Connection established")

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
            if s[0] <-50:
                print("Wifi signal is to weak, cannot transfer data")
                time.sleep(1)
                quit()
        else:
            Wifi=[]
            Wifi = subprocess.check_output(["iwconfig"], shell=True, stderr=subprocess.DEVNULL)
            sentence=str(Wifi)
            s = [float(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
            firstnumber = ( "% d" + "dBm.") % s[13]
            print("The Wifi signal power is: " + str(firstnumber))
            time.sleep(1)
                


    #Runs a subprocess to monitor a GOOD wifi connection, if not it reports it to the user. 
    if __name__ == '__main__':
        p = multiprocessing.Process(target=ConnectionTest)
        p.start()

        # Wait for 10 seconds or until process finishes
        p.join(15)

        # If thread is still active
        if p.is_alive():
            print ("Continuously checking for a Tool - no connection established...")

            # Terminate - may not work if process is stuck for good
            p.terminate()
            #p.kill()
            p.join()

    #Time delay of 10 seconds between each data retreival
    
        


