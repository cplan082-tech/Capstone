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

print("Automatic Transponder Script Running \n")
time.sleep(2)

#Nick or Clive testing? 1 = Nick, 0 = Clive
Nick_Clive=1

#Nick use only : Are you testing in full setup mode (i.e. Pi hub, zero transponder, zero tool) ? 1 = Yes
Full_test_mode=0

#Are you testing on your computer or your Pi? 1 for computer, 0 for Pi
MAC=0

#What is your pi password?
password ='clive'
password_hub='clive'

#What are the Pi IPs?
IP_Tool="10.0.0.112"
IP_Transponder="10.0.0.67"
IP_MAC="10.0.0.159"

#The name of your devices?
tool="pi"
transponder="pi"
hub="pi"

#Clive name of your devices?
tool_clive="pi"
transponder_clive="pi"
hub_clive="pi"

#What minium signal power do you want? less than -60dBm is very weak
Signal_Power= '-70'

#What is the name of the tool memory file that we pass to the transponder?
Memory_name="Tool_Memory.csv"
Timer_name="Update_Timer.csv"

#Clive tool memory file name and Directory
Clive_tool_memory="Tool_Memory.csv"
Clive_tool_folder="/home/Tool/Documents/tooldump/"

#Set these path parameters for testing purposes:
# dest_filename = Memory_name
# dest_path = os.path.realpath("../wifi_comms/Memory/")
# src_path = "/home/pi/Hub/Memory/HubMemory"

ToolFile = "/home/pi/Documents/tooldump/"+ Memory_name
ToolPath = "/home/pi/Documents/tooldump"
TransponderPath = "/home/pi/Hub/Memory/HubMemory"
MACPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory/HubMemory"
MACFlagPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory"
MACTimerPath ="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/Hub/Memory"
HubTimerPath ="/home/pi/Hub/Memory"
HubFlagPath = "/home/pi/Hub/Memory"

#Clive file names:
src_filename = "/home/Tool/Documents/tooldump/"+ Memory_name
src_path = "/home/Tool/Documents/tooldump"
dest_path = os.path.realpath("../wifi_comms/Memory/")



#if MAC flag is set to 1, then the path corresponds to the MAC path, if 0, then the Pi path
if MAC ==1:
    path_nick = MACPath
    FlagPath = MACFlagPath
    
else:
    path_nick = TransponderPath
    FlagPath = os.path.realpath("../wifi_comms/Memory/")

    #These GPIOs check the Py switch if it is activated or now, disabling it.
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.IN) # Switch pin (transponder)
##    GPIO.setup(4, GPIO.OUT)
##    GPIO.output(4, GPIO.HIGH)
    GPIO.setup(16,GPIO.OUT)
    

if Full_test_mode==1:
    MACFlagPath=HubFlagPath
    MACTimerPath=HubTimerPath



#If Clive is testing the script, sets all his parameters
if Nick_Clive==0:

    def wifi_param_extract(filename_in):
        with open(filename_in, mode='r') as infile:
            reader = csv.reader(infile)
            with open('temp_params.csv', mode='w') as outfile:
                writer = csv.writer(outfile)
                mydict = {rows[0]:rows[1] for rows in reader}
        os.remove('temp_params.csv')
        return mydict

    # Extraction of initialization parameters
    wifi_params = wifi_param_extract(path.realpath('../../../wifi_params.csv'))
    
    IP_src = wifi_params["IP_src"] #"10.0.0.198"
    IP_dest = wifi_params["IP_dest"]#"10.0.0.112"

    Memory_name=Clive_tool_memory
    IP_Tool=IP_src
    IP_Transponder=IP_dest
    password = wifi_params["Password"]
    ToolPath=src_path
    TransponderPath=dest_path
    path_nick= dest_path
    FlagPath= dest_path
    tool=tool_clive
    transponder=transponder_clive
    hub=hub_clive
    ToolFile = ""+Clive_tool_folder+""+ Memory_name+""
    IP_MAC="10.0.0.159"
    MACPath=HubTimerPath
    MACTimerPath=HubTimerPath
    password_hub=password
    



#This function checks if the timmer has set a flag file called flag.csv, then pushes it to the tool memory, then deletes it.
def flag():
    print("Flag verification function running")

    time.sleep (2)
    file = pathlib.Path(FlagPath +"/flag.csv") #Checks if the flag file exists
    if file.exists ():
        print("Flag file found")
        output = pexpect.run("scp " + FlagPath +"/flag.csv " + tool +"@"+ IP_Tool +":"+ ToolPath, events={'(?i)password':""+ password +"\n"})
        print("\n %s" %output.decode("utf-8"))
        time.sleep(1)
        # os.remove(FlagPath + "/flag.csv")
        print("Flag file deleted\n")
    else:
        print("No flag file found\n")

    time.sleep(1)


#This function scp's into the tool and grabs all the tool data dumps and brings it to the hub deleting all other copies
#in the tool, and replaces the one in the transponder
def Retreive():

    print ("Retreiving tool data...")

    #Blink the on board LED green quickly to simulate data transfer
    for j in range(20):
        os.system('echo 1 | sudo dd status=none of=/sys/class/leds/led0/brightness') # led on
        time.sleep(0.1)
        os.system('echo 0 | sudo dd status=none of=/sys/class/leds/led0/brightness') # led off
        time.sleep(0.1)



    output = pexpect.run("scp " + tool +"@"+ IP_Tool +":"+ ToolFile + " "+ path_nick, events={'(?i)password':""+ password +"\n"})
    print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
    time.sleep(1)
    print("Tool memory file retreived")

    i=20
    while i>0:
        GPIO.output(16, 1)
        time.sleep(0.2)
        GPIO.output(16, 0)
        time.sleep(0.2)
        i=i-1
    
    #########Delete the tool memory, comment out to deactivate:
    pexpect.run("ssh pi@"+ IP_Tool +" 'rm "+ ToolPath + "/Tool_Memory.csv '", events={'(?i)password':""+ password +"\n"})


#List the amount of data dump files by login through ssh
def ConnectionTest(i):

    if i >1:
        print("Script continues to loop indefinetely while away from the Hub")
        time.sleep(3)
    

    print("\nRunning ConnectionTest()\n")
    time.sleep(1)

    if MAC==0:
    
        #Verifys if the switch is closed which replicates no wireless or WIFI coms. Note that GPIO 22 is BCM, not board for Pi 3 B
        if GPIO.input(15)==0:
            print("Wireless connections terminated... Switch is closed. Looping...")
            time.sleep(2)
            return
        else:
            print("Wireless conections enabled")
 
    output = pexpect.run("ssh " + tool +"@" + IP_Tool +" 'ls "+ ToolPath +" '", events={'(?i)password':""+ password +"\n"})
    #print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))
    #os.system("nick")
    print("\nConnection established\n")
    time.sleep(1)


    SignalStrength()
##
##    flag()
##
    Timer()
    flag()
    # Retreive()
    
#     Send()

    

#Check Wifi Connection Strength in dBm
def SignalStrength():
    print("Verifying signal strength")

    time.sleep(2)
    if MAC ==1:
        Wifi = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I"], shell=True, stderr=subprocess.DEVNULL)
        sentence=str(Wifi)
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
        firstnumber = ( "% d" + "dBm.") % s[0]
        print("The Wifi signal power is: " + str(firstnumber))
        time.sleep(3)
       

        #Check if Wifi signal is strong enough
        if s[0] < float(Signal_Power):
            print("Wifi signal is to weak, cannot transfer data")
            time.sleep(3)
            quit()
    else:
        Wifi=[]
        Wifi = subprocess.check_output(["iwconfig"], shell=True, stderr=subprocess.DEVNULL)
        sentence=str(Wifi)
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
        firstnumber = ( "% d" + "dBm.") % s[11]
        print("The Wifi signal power is: " + str(firstnumber))
        time.sleep(3)

#Send the tool data to the MAC
def Send():
    print("Sending the retreived data too the Hub")
    time.sleep(2)
    output_file ="Tool_Memory_acumulator.csv"
    if os.path.exists(dest_path + output_file):
        output = pexpect.run("scp " + dest_path + output_file +" " + hub +"@"+ IP_MAC +":"+ MACPath, events={'(?i)password':""+ password_hub +"\n"})
        os.remove(dest_path + output_file)
        print("\n %s" %output.decode("utf-8"))
        print("Files sent succesfully")
    else:
        print('Nothing to send')
        
    time.sleep(1)

#Grab timer csv file and bring it to the transponder, then delete the file
def Timer():
    print("Grabing timer csv file from the Hub")
    output = pexpect.run("scp " + hub + "@"+ IP_MAC +":"+ HubTimerPath +"/" + Timer_name + " "+ path_nick, events={'(?i)password':""+ password_hub +"\n"})
    print("\n %s" %output.decode("utf-8"))
    time.sleep(1)
    print("Deleting the timer csv file from the Hub")
    output = pexpect.run("ssh " + hub +"@"+ IP_MAC + " 'rm " + HubTimerPath +"/" + Timer_name + "'", events={'(?i)password':""+ password_hub +"\n"})
    time.sleep(1)
    
i=0
while True:
    i=i+1
    ConnectionTest(i)
    
