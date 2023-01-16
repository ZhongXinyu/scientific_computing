import pandas as pd
import math 
import matplotlib.pyplot as plt
import numpy as np
data = {
    "Temp/C":[0,6,12,18,24,30],
    "Rate":[5.5,10.9,23.5,48,98,206]
}
df=pd.DataFrame(data=data)
#################################### DEFINE CONSTANT ###############################
k_b=1.380649*10**(-23) #Boltzmann Constant

#################################### EDIT YOUR DATA HERE ###########################
'''
Examples:
df["Temp/Kelvin"]=df["Temp/C"]+273.15
df["1/T"]=1/df["Temp/Kelvin"]
df["P/Pa"]=df["P/kPa"]*1000
df["ln(P)"]=df["P/kPa"].apply(lambda x: np.log(x))
'''
df["Temp/Kelvin"]=df["Temp/C"]+273.15
df["1/T"]=1/df["Temp/Kelvin"]
df["ln(Rate)"]=df["Rate"].apply(lambda x: np.log(x))
print (df)
#################################### PLOT THE POINTS ##############################
df["X"] = df["1/T"]
df["Y"] = df["ln(Rate)"]
plt.plot(df["X"],df["Y"],marker="o")
gradient,intercept = np.polyfit(df["X"], df["Y"],1)
print ("gradient =",gradient,"intercept =",intercept)
################################### FURTHER EDITION ###############################
#print ("Latent Heat", gradient*-8.31)
#print ("Boiling Point", 1/((np.log(100)-intercept)/gradient)-273.15,"C")
print (gradient*k_b)


plt.show()