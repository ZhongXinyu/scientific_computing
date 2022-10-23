from numpy.linalg import inv
import numpy as np
import math
import matplotlib.pyplot as plt
rho=0.2
m=0.005
lambdaa=0.1
Z1=rho*lambdaa/(2*math.pi)
Z2=Z1
Z3=Z2
k2=2*math.pi/lambdaa
##Ax=y，x=invA*y
r_amplitude=[]
r_phase=[]
t_amplitude=[]
t_phase=[]
a_amplitude=[]
b_amplitude=[]
c_amplitude=[]
x_value=np.linspace(0,0.2,10000)
for l in x_value:
    a = np.array([
        [-1,1,1,0], 
        [1+1j*m/Z1,Z1/Z2,-Z1/Z2,0],
        [0,pow(math.e,-1j*k2*l),pow(math.e,1j*k2*l),-1],
        [0,pow(math.e,-1j*k2*l),-pow(math.e,1j*k2*l),-Z2/Z3-1j*m/Z3]
        ])
    y = np.array([1,1-1j*m/Z1,0,0])
    #print (a)
    ainv = inv(a)
    #print (ainv)
    x=np.matmul(ainv,y)
    r=x[0]
    a=x[1]
    b=x[2]
    t=x[3]
    if abs(r) < 10**(-3):
        print (l)
    r_amplitude.append(abs(r))
    t_amplitude.append(abs(t))
    a_amplitude.append(abs(a))
    b_amplitude.append(abs(b))
plt.xlabel("t")
plt.ylabel("r")
plt.title(
    f'Plot of r,\u03C4 against l,'+
    f'(k\u2082={round(k2,2)},'+
    f'Z\u2081='+
    f'Z\u2082='+
    f'Z\u2083={round(Z3,6)})'
    )
y=[
    r_amplitude,
    a_amplitude,
    b_amplitude,
    t_amplitude
    ]
legend=["r","a","b","tau"]
for i,y_value in enumerate(y):
    plt.plot(x_value,y_value,label=legend[i])
plt.legend()
plt.savefig('Q16 Part (b).png')