'''
This is a programme to estimate the value of ln2 

Method:
Generate random points in the square region of 1<x<2, 1<y<2, count ratio of no. of points falls under the curve y=1/x
'''

import math
import random
import matplotlib.pyplot as plt

no_of_trials=30000
counter=0
results=[]
for i in range (1,no_of_trials+1):
    x=random.random()+1
    y=random.random()
    y_critical=1/x
    if y < y_critical:
        counter+=1
    results.append(counter/i)
print(f"Estimated Value of ln(2)is { '%.2f' % (counter/no_of_trials)}, with {no_of_trials} of points plotted")
print("Real Value of ln(2) is",math.log(2))
plt.ylim(0,1)
plt.xlim(-no_of_trials/100,no_of_trials)
plt.axhline(y=math.log(2), color='r', linestyle='--',label="True Value of ln(2)")
plt.plot(results,label="Estimated Value of ln(2)")
plt.legend()
plt.xlabel("No of trials")
plt.ylabel("Estimated value of ln(2)")
plt.show()

#Disclaimer: I completed this programme independently
