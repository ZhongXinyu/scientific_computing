from re import L
import numpy as np
n=int(input ("Please enter an integer that is larger than 2: "))

prime_list=[]
###--Method 2--###
####==========####
for i in range (2,n):
    j=2
    prime=1
    for j in prime_list:
        if i % j == 0:
            prime=0
            break
    if prime:
        prime_list.append(i)

print (f'There are {len(prime_list)} prime numbers that is smaller than{n}, they are:',prime_list)

