import pandas as pd
import math 
import matplotlib.pyplot as plt
import numpy as np
data = {
    "Temp/C":[0,20,40,60,80,100],
    "P/kPa":[4.3,12,28.4,59.3,110.9,192.5]
}

df=pd.DataFrame(data=data)

df["Temp/Kelvin"]=df["Temp/C"]+273.15
df["1/T"]=1/df["Temp/Kelvin"]

df["P/Pa"]=df["P/kPa"]*1000
df["ln(P)"]=df["P/kPa"].apply(lambda x: np.log(x))

'''
plt.plot(df["1/T"],df["ln(P)"],marker="o")
plt.show()
'''
gradient,intercept = np.polyfit(df["1/T"], df["ln(P)"],1)

print (df)

print ("gradient =",gradient,"intercept =", intercept)

print ("Latent Heat", gradient*-8.31)

print ("Boiling Point", 1/((np.log(100)-intercept)/gradient)-273.15,"C")