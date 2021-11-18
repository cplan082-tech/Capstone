import pandas as pd
import datetime
df2=pd.read_csv('Hub_Memory.csv')

def make_delta(entry):
  m, s = entry.split(':')
  return datetime.timedelta(minutes = int(m), seconds = float(s))

df = pd.DataFrame(df2) #initalizes the data
time_of_use = df["Time_of_use"].apply(lambda entry: make_delta(entry)) #takes each number in the column "Time_of_use" and converts it to a base 10 number, which is then added to a list
result = sum(time_of_use, datetime.timedelta()) #take everything in the list and add it
print (result)
df["Time_of_use"] = result
df.to_csv("Hub_Memory.csv", index=False)

