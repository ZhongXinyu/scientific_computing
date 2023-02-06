import matplotlib.pyplot as plt
import numpy as np

def simpson_integration(func,a,b,N):
    dx=(b-a)/N
    I=0
    for i in range (1,N):
        if i%2 == 1:
            I+=4*func(a+i*dx)
        else:
            I+=2*func(a+i*dx)
    I=(func(a)+I+func(b))*dx/3
    return I

def complex_simpson_integration(func, a, b, N):
    def real_func(x):
        return np.real(func(x))
    def imag_func(x):
        return np.imag(func(x))
    real_integral = simpson_integration(real_func, a, b, N)
    imag_integral = simpson_integration(imag_func, a, b, N)
    return (real_integral + 1j*imag_integral)

psi=(lambda x:np.sin(x))
i_values=np.linspace(-6,6,1000)
psi_k=[]
psi_x=[]
for i in i_values:
    psi_xi=psi(i)
    psi_ki=complex_simpson_integration((lambda x: psi(x)*np.exp(1j*i*x)),-100,100,1000)
    #print (psi_xi,psi_ki)
    psi_x.append(psi_xi)
    psi_k.append(abs(psi_ki))

###plt.subplot(i_values,psi_x)
###plt.subplot(i_values,psi_k)

fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(i_values,psi_x)
axes[1].plot(i_values,psi_k)

plt.show()