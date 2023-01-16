from numpy.linalg import inv
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
k2=2*math.pi
Z1=1
Z2=3
Z3=4
##Ax=y，x=invA*y
r_amplitude=[]
r_phase=[]
t_amplitude=[]
t_phase=[]
x_value=np.linspace(0,1,1000)
for l in x_value:
    a = np.array([
        [-1,1,1,0], 
        [1,Z1/Z2,-Z1/Z2,0],
        [0,pow(math.e,-1j*k2*l),pow(math.e,1j*k2*l),-1],
        [0,pow(math.e,-1j*k2*l),-pow(math.e,1j*k2*l),-Z2/Z3]
        ])
    y = np.array([1,1,0,0])
    #print (a)
    ainv = inv(a)
    #print (ainv)
    x=np.matmul(ainv,y)
    r=x[0]
    t=x[3]
    r_amplitude.append(abs(r))
    r_phase.append(cmath.phase(r))
    t_amplitude.append(abs(t))
    t_phase.append(cmath.phase(t))
plt.xlabel("t")
plt.ylabel("r")
plt.title(
    f'Plot of r,\u03C4 against l,'+
    '(k\u2082=2\u03C0,'+
    'Z\u2081=1,'+
    'Z\u2082=3,'+
    'Z\u2083=4)'
    )
y=[r_amplitude,r_phase,t_amplitude,t_phase]
legend=["r_amplitude","r_phase","\u03C4_amplitude","\u03C4_phase"]
for i,y_value in enumerate(y):
    plt.plot(x_value,y_value,label=legend[i])
plt.legend()
plt.show()
#print (r_amplitude)
#print (r_phase)

print (x)