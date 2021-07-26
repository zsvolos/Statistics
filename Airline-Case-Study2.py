import pandas as pd
import numpy as np
file ='FlightDelay.csv'
df = pd.read_csv(file)
df.head()

#Excersize 1  
m = 4
p = 0.5

def mest(a,b):
    est = (a+m*p)/(b+m)
    return est

pdelay = 5/8
pnodelay = 3/8 
pseadelay = mest(3,5)
pseanodelay = mest(1,3)
patldelay = mest(1,5)
patlnodelay = mest(2,3)
pswdelay = mest(2,5)
pswnodelay = mest(1,3)
pd = pdelay * pseadelay * patldelay * pswdelay
pnd = pnodelay * pseanodelay * patlnodelay * pswnodelay
arg = [pd,pnd]
def ans():
    if max(arg)== pd:
        print("delayed")
    if max(arg) == pnd:
        print("not delayed")
    return
ans()

df["Delayed"] = np.where( df["Departure Delay"] + df["Arrival Delay"] >= 15, "Y", "N")
df["Total Delay"] = df["Departure Delay"] + df["Arrival Delay"]
df





#(1)
m = 3
#probability of delay and no delay given routes
delayedflights = df.loc[(df.Delayed == "Y") & (df.Carrier == "AA") & (df.Origin + df.Destination == "JFKLAS")].Delayed.count()
flighttotal = df.loc[(df.Carrier == "AA") & (df.Origin + df.Destination == "JFKLAS")].Delayed.count() 

probability_of_delay = delayedflights/flighttotal
probability_of_delay = probability_of_delay.item()
probability_of_nodelay = 1-probability_of_delay


print("the probability of delay on this airline and route is " + str(probability_of_delay))
print("the probability of no delay on this airline and route is " + str(probability_of_nodelay))

#(pOrigin given delay )
p = 1/df.Origin.nunique()
delaytotal = df.loc[df["Delayed"] == "Y"].Delayed.count()
delayOrigin = df.loc[(df["Delayed"] == "Y") & (df["Origin"] == "JFK") ].Delayed.count()


pOriginDelay = mest(delayOrigin,delaytotal)

#(pOrigin given no delay )
nodelaytotal = df.loc[df["Delayed"] == "N"].Delayed.count()
nodelayOrigin = df.loc[(df["Delayed"] == "N") & (df["Origin"] == "JFK") ].Delayed.count()

pOriginNodelay = mest(nodelayOrigin,nodelaytotal)

#(pDestination given delay )
p = 1/df.Destination.nunique()
delayDestination = df.loc[(df["Delayed"] == "Y") & (df["Destination"] == "LAS") ].Delayed.count()

pDestinationDelay = mest(delayDestination,delaytotal) 

#(pDestination given nodelay )
nodelayDestination = df.loc[(df["Delayed"] == "N") & (df["Destination"] == "LAS") ].Delayed.count()

pDestinationNodelay = mest(nodelayDestination,nodelaytotal)

#(pAirline given delay) 
p = 1/df.Carrier.nunique()
delayAirline = df.loc[(df["Delayed"] == "Y") & (df["Carrier"] == "AA")].Delayed.count()

pAirlineDelay = mest(delayAirline,delaytotal)

#(pAirline given nodelay) 
nodelayAirline = df.loc[(df["Delayed"] == "N") & (df["Carrier"] == "AA")].Delayed.count()

pAirlineNodelay = mest(nodelayAirline,nodelaytotal)
datatotal = (df.loc[(df.Delayed == "Y") ].Delayed.count()) + (df.loc[(df.Delayed == "N") ].Delayed.count())
probability_of_delay = (df.loc[(df.Delayed == "Y") ].Delayed.count())/datatotal
probability_of_nodelay = (df.loc[(df.Delayed == "N") ].Delayed.count())/datatotal
classifierDelayed = probability_of_delay*pOriginDelay*pDestinationDelay*pAirlineDelay
classifierNoDelay = probability_of_nodelay*pOriginNodelay*pDestinationNodelay*pAirlineNodelay
def classification():
    if classifierDelayed > classifierNoDelay:
        print( "JFK-LAS on AA is classified as Delayed")
    else:
        print( "JFK-LAS on AA is classified as Not Delayed")
    return
classification()




m = 3
#probability of delay and no delay given routes
delayedflights = df.loc[(df.Delayed == "Y") & (df.Carrier == "B6") & (df.Origin + df.Destination == "JFKLAS")].Delayed.count()
flighttotal = df.loc[(df.Carrier == "B6") & (df.Origin + df.Destination == "JFKLAS")].Delayed.count() 

probability_of_delay = delayedflights/flighttotal
probability_of_delay = probability_of_delay.item()
probability_of_nodelay = 1-probability_of_delay


print("the probability of delay on this airline and route is " + str(probability_of_delay))
print("the probability of no delay on this airline and route is " + str(probability_of_nodelay))

#(pOrigin given delay )
p = 1/df.Origin.nunique()
delaytotal = df.loc[df["Delayed"] == "Y"].Delayed.count()
delayOrigin = df.loc[(df["Delayed"] == "Y") & (df["Origin"] == "JFK") ].Delayed.count()


pOriginDelay = mest(delayOrigin,delaytotal)

#(pOrigin given no delay )
nodelaytotal = df.loc[df["Delayed"] == "N"].Delayed.count()
nodelayOrigin = df.loc[(df["Delayed"] == "N") & (df["Origin"] == "JFK") ].Delayed.count()

pOriginNodelay = mest(nodelayOrigin,nodelaytotal)

#(pDestination given delay )
p = 1/df.Destination.nunique()
delayDestination = df.loc[(df["Delayed"] == "Y") & (df["Destination"] == "LAS") ].Delayed.count()

pDestinationDelay = mest(delayDestination,delaytotal) 

#(pDestination given nodelay )
nodelayDestination = df.loc[(df["Delayed"] == "N") & (df["Destination"] == "LAS") ].Delayed.count()

pDestinationNodelay = mest(nodelayDestination,nodelaytotal)

#(pAirline given delay) 
p = 1/df.Carrier.nunique()
delayAirline = df.loc[(df["Delayed"] == "Y") & (df["Carrier"] == "B6")].Delayed.count()

pAirlineDelay = mest(delayAirline,delaytotal)

#(pAirline given nodelay) 
nodelayAirline = df.loc[(df["Delayed"] == "N") & (df["Carrier"] == "B6")].Delayed.count()

pAirlineNodelay = mest(nodelayAirline,nodelaytotal)
datatotal = (df.loc[(df.Delayed == "Y") ].Delayed.count()) + (df.loc[(df.Delayed == "N") ].Delayed.count())
probability_of_delay = (df.loc[(df.Delayed == "Y") ].Delayed.count())/datatotal
probability_of_nodelay = (df.loc[(df.Delayed == "N") ].Delayed.count())/datatotal
classifierDelayed = probability_of_delay*pOriginDelay*pDestinationDelay*pAirlineDelay
classifierNoDelay = probability_of_nodelay*pOriginNodelay*pDestinationNodelay*pAirlineNodelay
def classification():
    if classifierDelayed > classifierNoDelay:
        print( "JFK-LAS on B6 is classified as Delayed")
    else:
        print( "JFK-LAS on B6 is classified as Not Delayed")
    return
classification()




m = 3
#probability of delay and no delay given routes
delayedflights = df.loc[(df.Delayed == "Y") & (df.Carrier == "VX") & (df.Origin + df.Destination == "SFOORD")].Delayed.count()
flighttotal = df.loc[(df.Carrier == "VX") & (df.Origin + df.Destination == "SFOORD")].Delayed.count() 

probability_of_delay = delayedflights/flighttotal
probability_of_delay = probability_of_delay.item()
probability_of_nodelay = 1-probability_of_delay


print("the probability of delay on this airline and route is " + str(probability_of_delay))
print("the probability of no delay on this airline and route is " + str(probability_of_nodelay))

#(pOrigin given delay )
p = 1/df.Origin.nunique()
delaytotal = df.loc[df["Delayed"] == "Y"].Delayed.count()
delayOrigin = df.loc[(df["Delayed"] == "Y") & (df["Origin"] == "SFO") ].Delayed.count()


pOriginDelay = mest(delayOrigin,delaytotal)

#(pOrigin given no delay )
nodelaytotal = df.loc[df["Delayed"] == "N"].Delayed.count()
nodelayOrigin = df.loc[(df["Delayed"] == "N") & (df["Origin"] == "SFO") ].Delayed.count()

pOriginNodelay = mest(nodelayOrigin,nodelaytotal)

#(pDestination given delay )
p = 1/df.Destination.nunique()
delayDestination = df.loc[(df["Delayed"] == "Y") & (df["Destination"] == "ORD") ].Delayed.count()

pDestinationDelay = mest(delayDestination,delaytotal) 

#(pDestination given nodelay )
nodelayDestination = df.loc[(df["Delayed"] == "N") & (df["Destination"] == "ORD") ].Delayed.count()

pDestinationNodelay = mest(nodelayDestination,nodelaytotal)

#(pAirline given delay) 
p = 1/df.Carrier.nunique()
delayAirline = df.loc[(df["Delayed"] == "Y") & (df["Carrier"] == "VX")].Delayed.count()

pAirlineDelay = mest(delayAirline,delaytotal)

#(pAirline given nodelay) 
nodelayAirline = df.loc[(df["Delayed"] == "N") & (df["Carrier"] == "VX")].Delayed.count()

pAirlineNodelay = mest(nodelayAirline,nodelaytotal)
datatotal = (df.loc[(df.Delayed == "Y") ].Delayed.count()) + (df.loc[(df.Delayed == "N") ].Delayed.count())
probability_of_delay = (df.loc[(df.Delayed == "Y") ].Delayed.count())/datatotal
probability_of_nodelay = (df.loc[(df.Delayed == "N") ].Delayed.count())/datatotal
classifierDelayed = probability_of_delay*pOriginDelay*pDestinationDelay*pAirlineDelay
classifierNoDelay = probability_of_nodelay*pOriginNodelay*pDestinationNodelay*pAirlineNodelay
def classification():
    if classifierDelayed > classifierNoDelay:
        print( "SFO-ORD on VX is classified as Delayed")
    else:
        print( "SFO-ORD on VX is classified as Not Delayed")
    return
classification()




m = 3
#probability of delay and no delay given routes
delayedflights = df.loc[(df.Delayed == "Y") & (df.Carrier == "WN") & (df.Origin + df.Destination == "SFOORD")].Delayed.count()
flighttotal = df.loc[(df.Carrier == "WN") & (df.Origin + df.Destination == "SFOORD")].Delayed.count() 

#flighttotal and delayedflights are 0 here. This is the source of the error but I left this in to show that it is zero. 
probability_of_delay = delayedflights/flighttotal
probability_of_delay = probability_of_delay.item()
probability_of_nodelay = 1-probability_of_delay


print("the probability of delay on this airline and route is unkown")
print("the probability of no delay on this airline and route is unknown")

#(pOrigin given delay )
p = 1/df.Origin.nunique()
delaytotal = df.loc[df["Delayed"] == "Y"].Delayed.count()
delayOrigin = df.loc[(df["Delayed"] == "Y") & (df["Origin"] == "SFO") ].Delayed.count()


pOriginDelay = mest(delayOrigin,delaytotal)

#(pOrigin given no delay )
nodelaytotal = df.loc[df["Delayed"] == "N"].Delayed.count()
nodelayOrigin = df.loc[(df["Delayed"] == "N") & (df["Origin"] == "SFO") ].Delayed.count()

pOriginNodelay = mest(nodelayOrigin,nodelaytotal)

#(pDestination given delay )
p = 1/df.Destination.nunique()
delayDestination = df.loc[(df["Delayed"] == "Y") & (df["Destination"] == "ORD") ].Delayed.count()

pDestinationDelay = mest(delayDestination,delaytotal) 

#(pDestination given nodelay )
nodelayDestination = df.loc[(df["Delayed"] == "N") & (df["Destination"] == "ORD") ].Delayed.count()

pDestinationNodelay = mest(nodelayDestination,nodelaytotal)

#(pAirline given delay) 
p = 1/df.Carrier.nunique()
delayAirline = df.loc[(df["Delayed"] == "Y") & (df["Carrier"] == "WN")].Delayed.count()

pAirlineDelay = mest(delayAirline,delaytotal)

#(pAirline given nodelay) 
nodelayAirline = df.loc[(df["Delayed"] == "N") & (df["Carrier"] == "WN")].Delayed.count()

pAirlineNodelay = mest(nodelayAirline,nodelaytotal)

datatotal = (df.loc[(df.Delayed == "Y") ].Delayed.count()) + (df.loc[(df.Delayed == "N") ].Delayed.count())
probability_of_delay = (df.loc[(df.Delayed == "Y") ].Delayed.count())/datatotal
probability_of_nodelay = (df.loc[(df.Delayed == "N") ].Delayed.count())/datatotal
classifierDelayed = probability_of_delay*pOriginDelay*pDestinationDelay*pAirlineDelay
classifierNoDelay = probability_of_nodelay*pOriginNodelay*pDestinationNodelay*pAirlineNodelay
def classification():
    if classifierDelayed > classifierNoDelay:
        print( "SFO-ORD on WN is classified as Delayed")
    else:
        print( "SFO-ORD on WN is classified as Not Delayed")
    return
classification()