import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.integrate import quad

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

def complex_quadrature(func, a, b):
    def real_func(x):
        return scipy.real(func(x))
    def imag_func(x):
        return scipy.imag(func(x))
    real_integral = quad(real_func, a, b)
    imag_integral = quad(imag_func, a, b)
    return (real_integral[0] + 1j*imag_integral[0], real_integral[1:], imag_integral[1:])



lambda_0=500*(10**(-9))
k=(2*np.pi)/lambda_0
d=0.001
D_array=[10*10**(-3),100*10**(-3),326*10**(-3),640*10**(-3),4000*10**(-3)]
Y_array=np.linspace(-0.0015,0.0015,1000)
### delta_omega=d/sqrt(2/(lambda*D))
for D in D_array:
    delta_omega=d*np.sqrt(2/(lambda_0*D))
    print (delta_omega)
    Iarray=[]
    Y_array_mm=[]
    for Y in Y_array:
        I = complex_simpson_integration(lambda x: np.exp(1j*k*np.sqrt((Y-x)**2+D**2)),-d/2,d/2,1000)
        #print (I)
        Iarray.append((abs(I))**2)
    max_intensity=max(Iarray)
    Iarray_relative = [element/max_intensity for element in Iarray]
    Y_array_mm = [element * 1000 for element in Y_array]
    plt.plot(Y_array_mm,Iarray_relative,'r')
    plt.xlabel('Distance from centre, x/mm')
    plt.ylabel(r'Relative Intensity, $I/I_0$')
    plt.title(f'Fresnel Diffraction,D={D*10**3}mm')
    plt.savefig(f'Fresnel Diffraction,D={D*10**3}mm.png',transparent=True)
    plt.close()


