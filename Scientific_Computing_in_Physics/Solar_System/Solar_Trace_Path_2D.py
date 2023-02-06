"""
From the base question, I added another property called:
    self.history
which is the path history of the planet.

Now we can trace the path traveled by each planet.

In this programme, I found a stable (relative) three-star system where 
two stars are orbiting around their centre of mass, which, together with the third star
is orbiting around the centre of mass of the entire solar system.

The path of each star is traced
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from mpl_toolkits.mplot3d import Axes3D

#creates the coordinate system and items for the solar system
class SolarSystem():
    def __init__(self):
        self.size = 1000
        self.planets = []
        self.fig = plt.figure()
        #self.ax = Axes3D(self.fig,auto_add_to_figure=False)#, auto_add_to_figure=False)
        self.ax = self.fig.add_subplot()
        self.fig.add_axes(self.ax)
        self.dT = 1
        
    def add_planet(self, planet):
        self.planets.append(planet)
        
    def update_planets(self):
        self.ax.clear() ###Remove the previous drawing
        for planet_no, planet in enumerate (self.planets):
            planet.move()
            planet.draw(planet.color,10,planet.history, planet_no)
            planet.history.append(planet.position)
            
    def fix_axes(self):
        self.ax.set_xlim((-self.size/2, self.size/2))
        self.ax.set_ylim((-self.size/2, self.size/2))
        #self.ax.set_zlim((-self.size/2, self.size/2))
        
    def gravity_planets(self):
        for i, first in enumerate(self.planets):
            for second in self.planets[i+1:]:
                first.gravity(second)
                
class Planet():
    def __init__(self, SolarSys, mass, position=(0,0), velocity=(0,0), color='black'):
        self.SolarSys = SolarSys
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.SolarSys.add_planet(self)
        self.color = color
        self.history=[] ###This is the path history of the planet
        
    def move(self): # updates its position and velocity
        self.position = (
            self.position[0]+self.velocity[0]*SolarSys.dT,
            self.position[1]+self.velocity[1]*SolarSys.dT,
            #self.position[2]+self.velocity[2]*SolarSys.dT,
        )
        
    def draw(self,color,markersize,history,planet_no): ###Plot Position Add 3 parameters
        self.SolarSys.ax.plot(*self.position, marker="o", markersize=markersize, color=color)
        for item in history: # Plot the path
            #print (item[0])
            self.SolarSys.ax.plot(item[0],item[1],marker="o",markersize=2,color=color)
        x, y = -450, 450 - planet_no *50
        self.SolarSys.ax.text(x,y,f"velocity{planet_no} = {self.velocity}" ,color=color)
        #return(self.position)

    def gravity(self, other): ###evaluate the force
        distance = np.subtract(other.position, self.position)
        distanceMag = np.linalg.norm(distance)
        distanceUnit = np.divide(distance,distanceMag)
        forceMag = self.mass*other.mass/(distanceMag**2)
        force = np.multiply(distanceUnit, forceMag)
        switch = 1
        for body in self, other:
            acceleration = np.divide(force, body.mass)
            acceleration = np.multiply(acceleration, SolarSys.dT*switch)
            body.velocity = np.add(body.velocity, acceleration)
            switch *= -1
            
class Sun(Planet): ###Sun Class is herited from the Planet class
    def __init__(self, SolarSys, mass=100000, position=(0,0), velocity=(0,0)):
        super(Sun, self).__init__(SolarSys, mass, position, velocity)
        self.color = "orange"
        
    def move(self):
        self.position = self.position
        
SolarSys = SolarSystem()

#Defining planets

mass=8500
planet1 = Planet(SolarSys, mass=mass, position=(0,3*100), velocity=(5,-1),color = "blue")
planet2 = Planet(SolarSys, mass=mass, position=(-np.sqrt(3)*100,0), velocity=(-5/2,+(5/2*np.sqrt(3))),color = "orange")
planet3 = Planet(SolarSys, mass=mass, position=(np.sqrt(3)*100,0), velocity=(-5/2,-(5/2*np.sqrt(3))),color = "green")

'''
planet2 = Planet(SolarSys, mass=10000, position=(50,-200), velocity=(4,5))
planet1 = Planet(SolarSys, mass=10000, position=(-50,-200), velocity=(-4,5),color = "red")

planet3 = Planet(SolarSys, mass=10000, position=(0,100), velocity=(-4,0))
#sun = Sun(SolarSys)
'''

def animate(i):
    #print("The frame is:",i)
    SolarSys.gravity_planets()
    SolarSys.update_planets()
    SolarSys.fix_axes()

anim = animation.FuncAnimation(SolarSys.fig, animate, frames = 300, interval=100)

#plt.show()

#anim.save("planet.gif",fps = 60,dpi= 200)
anim.save("planet.mp4",fps = 60,dpi= 200)
