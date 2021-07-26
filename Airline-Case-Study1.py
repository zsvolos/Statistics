import pandas as pd
import numpy as np
file ='FlightTime.csv'
df = pd.read_csv(file)
df.head()

#flight time
df = df.dropna(how='any')
df = df[df['Flight Time'] >= 230]


#new count
index = df.index 
rowcount = len(index)
rowcount = str(rowcount)
print(rowcount + " is row count")

#target flight time
d = 1741.16
lori=-87.9 
ldes = -118.41

TFT = 0.117 * d +.517*(lori - ldes) + 20
TFTstr = str(TFT)
print( TFTstr + " is target flight time")

#typical flight time 

typicalft = TFT + df["Departure Delay"].mean() + df["Arrival Delay"].mean()
typicalftstr = str(typicalft)
print(typicalftstr + " is typical flight time")





#time added for each airline 
df = df.groupby(['Carrier']).mean()
flttime = df["Flight Time"] + df["Departure Delay"] + df["Arrival Delay"] - TFT
df["TimeAdded"] = flttime
df1 = df["TimeAdded"]
df1 = df1.reset_index()


import matplotlib as plt
x = df1.Carrier
y = df1.TimeAdded
plt.pyplot.bar(x,y)

df1