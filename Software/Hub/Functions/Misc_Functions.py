import csv
from datetime import datetime

csvFilePath = r'Memory/Hub_Memory.csv'
headers = ['Transponder_ID','Tool_ID','temp','humid','x','y','z','freefall','collision','Motion','Time_of_use','date','time']

def is_tool_missing(timeThreshold = 3):
    with open(csvFilePath, 'r') as file:
        data = file.readlines()
    lastRow = data[-1]

    lastTime = lastRow[-5:]
    lastDate = lastRow[-16:-6]
    toolId = lastRow[0:6]

    DateNow = datetime.today().strftime('%Y-%m-%d')
    TimeNow = datetime.today().strftime('%H:%M')

    # These are used for testing!!!
    #lastDate = '2021-11-12'
    #TimeNow = "23:00"

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


