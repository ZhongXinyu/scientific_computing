import numpy as np
import math
import matplotlib.pyplot as plt

k0=1
sigmak=k0/10
deltak=sigmak/10
c=1
d=0
m0=30
x_axis=np.linspace(-100,500,1000)
for d in [0,0.1,-0.1,0.2,-0.2]:
    plt.clf()
    for t in [0,100,200,300]:
        psi=[]
        for x in x_axis:
            psi_x=0
            for m in range (-m0,m0+1):
                km=k0+m*deltak
                omega=c*km+d*(km**3)
                psi_x+=math.exp(-(km-k0)**2/(2*sigmak**2))*math.cos(km*x-omega*t)
            psi.append(psi_x)
        plt.plot(x_axis,psi,label=f't={t}')
    plt.xlabel("\u03C8")
    plt.ylabel("x")
    plt.title(f'Disturbance against x,d={d}')
    plt.legend()
    plt.savefig(f'Disturbance against x,d={d}.png')
