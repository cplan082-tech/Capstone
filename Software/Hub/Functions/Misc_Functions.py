import csv
from datetime import datetime
import pandas as pd
import datetime as datetime2 # I was getting errors without this?

# csvFilePath = r'Memory/Hub_Memory.csv'
csvFilePath = "/home/pi/Hub/Memory/Tool_Memory_acumulator.csv"
headers = ['Transponder_ID','Tool_ID','temp','humid','x','y','z','freefall','collision','Motion','Time_of_use','date','time']

def is_tool_missing(timeThreshold = 3):

    csv = pd.read_csv(csvFilePath)
    df = pd.DataFrame(csv)

    lastTime = df["time"][df.index[-1]]
    lastDate = df["date"][df.index[-1]]
    toolId = str(df["Tool_ID"][df.index[-1]])

    #with open(csvFilePath, 'r') as file:
    #    data = file.readlines()
    #lastRow = data[-1]

    #lastTime = lastRow[-5:]
    #lastDate = lastRow[-17:-7]
    #toolId = lastRow[0:6]

    DateNow = datetime.today().strftime('%Y-%m-%d')
    TimeNow = datetime.today().strftime('%H:%M')

    # These are used for testing!!!
    #lastDate = '2021-11-19'
    #TimeNow = "13:00"

    print("\nThe last known date is: " + lastDate)
    print("The last known time is: " + lastTime)

    print("\nThe current date is: " + DateNow)
    print("The current time is: " + TimeNow + "\n")



    if datetime.strptime(lastDate, '%Y-%m-%d') < datetime.strptime(DateNow, '%Y-%m-%d'):
        print('Possible Stolen tool! Last known date is before today!')
        return True, lastDate, lastTime, toolId, DateNow, TimeNow
    elif datetime.strptime(lastDate, '%Y-%m-%d') > datetime.strptime(DateNow, '%Y-%m-%d'):
        print('Error, recorded date is later than current date... Corrupt data')
        return 'Data Corrupted', lastDate, lastTime, toolId, DateNow, TimeNow
    elif DateNow == lastDate:
        print('Last known date is today... Checking timestamp')
        diff = datetime.strptime(TimeNow, '%H:%M') - datetime.strptime(lastTime,'%H:%M')
        if diff.days < 0:
            print('Error, same date is recorded, but data collection timestamp is later than current time... Corrupt data')
            return 'Data Corrupted', lastDate, lastTime, toolId, DateNow, TimeNow
        elif diff.seconds >= timeThreshold*3600:
            print('Time discrepancy is greater than 3 hours (' + str((diff.seconds)/60) +' minutes), report suspicious behaviour')
            return True, lastDate, lastTime, toolId, DateNow, TimeNow
        else:
            print("We received tool information before the 3 hour threshold (" + str((diff.seconds)/60) + " minutes)")
            return False, lastDate, lastTime, toolId, DateNow, TimeNow


def make_delta(entry):
    m, s = entry.split(':')
    return datetime2.timedelta(minutes=int(m), seconds=float(s))

def findTimeSum(path):
    df2 = pd.read_csv(path)
    df = pd.DataFrame(df2)  # initalizes the data
#     indx = df.loc[df[]]
    time_of_use = df["Time_of_use"].apply(lambda entry: make_delta(entry))  # takes each number in the column "Time_of_use" and converts it to a base 10 number, which is then added to a list
    result = sum(time_of_use, datetime2.timedelta())  # take everything in the list and add it
    print(result)
    result2 = round((result.seconds)/60, 2) # convert seconds to minutes
    print(result2)

    df["Time_of_use"] = result2
    df.to_csv(path, index=False)
    print("Done converting times and finding sum!")

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False