# Import pexpect module

import pexpect
import os
import time
import glob
#import pandas

count=0
#List the amount of data dump files by login through ssh

output = pexpect.run("ssh pi@192.168.0.29 'ls /home/pi/Documents/hubdump' ", events={'(?i)password':'nick\n'})
string=str(output)
substring = "data"
count = string.count(substring)
print("The count of data files in the tool is:", count)


#This function scp's into the tool and grabs all the tool data dumps and brings it to the hub
def Retreive(count):

    files = count
    files =int(files)
    i=1
    print("We have found this many data dumps:", files)

    while i <= files :

        output = pexpect.run("scp pi@192.168.0.29:/home/pi/Documents/tooldump/data{}.csv /home/pi/Documents/hubdump".format(i), events={'(?i)password':'nick\n'})
        print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))

        time.sleep(1)

        output = pexpect.run("scp pi@192.168.0.29:/home/pi/Documents/tooldump/Test /home/pi/Documents/hubdump", events={'(?i)password':'nick\n'})
        print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))

        i=i+1
    return

Retreive(count)

##def concatenate(indir="/Users/christelledube/Desktop/PythonScripts/hub_to_tool", outfile="/Users/christelledube/Desktop/PythonScripts/hub_to_tool/AWS"):
##      os.chdir(indir)
##      fileList=glob.glob("*.csv")
##      dfList=[]
##      for filename in fileList:
##                  print(filename)
##                  df=pandas.read_csv(filename,header=None)
##                  dfList.append(df)
##      concatDf=pandas.concat(dfList,axis=0)
##
