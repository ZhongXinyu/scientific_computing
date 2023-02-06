# Import the required modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dU_dx(U, x):
    # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
    return [U[1],-np.sin(U[0])]
for theta_0 in [0.01,0.03,0.1,1.0,2.0,3.0]:
    U0 = [theta_0, 0]
    xs = np.linspace(0, 100, 1000)
    Us = odeint(dU_dx, U0, xs)/theta_0
    ys = Us[:,0]
    plt.clf()
    plt.xlabel("t")
    plt.ylabel("\u03B8/\u03B8\u2080")
    plt.title(f'Motion of Pendulum,\u03B8\u2080={theta_0}')
    plt.plot(xs,ys)
    plt.savefig(f'Motion of Pendulum,\u03B8\u2080={theta_0}.png',transparent=True)

