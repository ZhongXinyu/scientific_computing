class light:
    description = "light as two properties, e.g. location of origin and direction"

    def __init__(self,origin,direction,k,c):
        self.origin=origin
        self.direction=direction
    
    def printBasicInfo(self):
        print (f'The light has origin{self.origin}, and direction{self.direction}')


import numpy as np
import matplotlib.pyplot as plt

ref_n1=1.5
ref_n2=1

def find_point_of_contact(k1,c1,k2,c2):
    """
    |1 -k1| |y| = |c1|
    |1 -k2| |x| = |c2|
    """
    matrix_x=np.array([[1,-k1],[1,-k2]])
    matrix_y=np.array([c1,c2])
    [y,x]= np.dot(np.linalg.inv(matrix_x),matrix_y)
    ###x,y=(c1-c2)/(k2-k1),(k2*c1-k1*c2)/(k2-k1)
    return (x,y)

plane_k=0
plane_c=0

critical_angle=np.arcsin(ref_n2/ref_n1)

incident_origin,incident_angle = [-5,5],np.pi/4
incident_k=-(np.pi/2-incident_angle)
incident_c=incident_origin[1]-incident_origin[0]*incident_k
refraction_origion=reflection_origin=find_point_of_contact(incident_k,incident_c,plane_k,plane_c)
reflection_k=-1*incident_k
reflection_c=reflection_origin[1]-reflection_origin[0]*reflection_k
refraction_k=1*incident_k*np.sin(ref_n2/ref_n1)


lower_limit=-10
upper_limit=10

linspace=np.linspace(-10,10,1000)
'''

incident=np.linspace(lower_limit,reflection_origin[0],int(1000*(reflection_origin[0]-lower_limit)/(upper_limit-lower_limit)))*incident_k+incident_c
reflection =(
    np.linspace(lower_limit,upper_limit,int(1000*(upper_limit-reflection_origin[0])/(upper_limit-lower_limit)))*reflection_k+reflection_c
    +np.linspace(reflection_origin[0],upper_limit,int(1000*(upper_limit-reflection_origin[0])/(upper_limit-lower_limit)))*reflection_k+reflection_c


'''
plane=np.linspace(lower_limit,upper_limit,1000)*plane_k+plane_c
refraction=linspace
incident=linspace*incident_k+incident_c
reflection=linspace*reflection_k+reflection_c

plt.plot(plane)
plt.plot(incident)
plt.plot(reflection)
#plt.plot(refraction)
plt.show()