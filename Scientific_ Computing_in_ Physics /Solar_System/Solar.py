import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

#creates the coordinate system and items for the solar system
class SolarSystem():
    def __init__(self):
        self.size = 1000
        self.planets = []
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig,auto_add_to_figure=False)#, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.dT = 1
        
    def add_planet(self, planet):
        self.planets.append(planet)
        
    def update_planets(self):
        self.ax.clear() ###Remove the previous drawing
        for planet in self.planets:
            planet.move()
            planet.draw()
            
    def fix_axes(self):
        self.ax.set_xlim((-self.size/2, self.size/2))
        self.ax.set_ylim((-self.size/2, self.size/2))
        self.ax.set_zlim((-self.size/2, self.size/2))
        
    def gravity_planets(self):
        for i, first in enumerate(self.planets):
            for second in self.planets[i+1:]:
                first.gravity(second)
                
class Planet():
    def __init__(self, SolarSys, mass, position=(0,0,0), velocity=(0,0,0)):
        self.SolarSys = SolarSys
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.SolarSys.add_planet(self)
        self.color = "black"
        
    def move(self): # updates its position and velocity
        self.position = (
            self.position[0]+self.velocity[0]*SolarSys.dT,
            self.position[1]+self.velocity[1]*SolarSys.dT,
            self.position[2]+self.velocity[2]*SolarSys.dT,
        )
        
    def draw(self): ###Plot Position
        self.SolarSys.ax.plot(*self.position, marker="o", markersize=10, color=self.color)
        
    def gravity(self, other): ###evaluate the force
        distance = np.subtract(other.position, self.position)
        distanceMag = np.linalg.norm(distance)
        distanceUnit = np.divide(distance,distanceMag)
        forceMag = self.mass*other.mass/(distanceMag**2)
        force = np.multiply(distanceUnit, forceMag)
        switch = 1
        for body in self, other:
            acceleration = np.divide(force, body.mass)
            acceleration = np.multiply(force, SolarSys.dT*switch)
            body.velocity = np.add(body.velocity, acceleration)
            switch *= -1
            
class Sun(Planet): ###Sun Class is herited from the Planet class
    def __init__(self, SolarSys, mass=1000, position=(0,0,0), velocity=(0,0,0)):
        super(Sun, self).__init__(SolarSys, mass, position, velocity)
        self.color = "yellow"
        
    def move(self):
        self.position = self.position
        
SolarSys = SolarSystem()

#Defining planets
planet1 = Planet(SolarSys, mass=100, position=(-50,-200,0), velocity=(-4,-5,0))
planet2 = Planet(SolarSys, mass=100, position=(50,-200,0), velocity=(-4,5,0))
planet3 = Planet(SolarSys, mass=200, position=(0,500,0), velocity=(4,0,0))
#sun = Sun(SolarSys)

def animate(i):
    print("The frame is:",i)
    SolarSys.gravity_planets()
    SolarSys.update_planets()
    SolarSys.fix_axes()




anim = animation.FuncAnimation(SolarSys.fig, animate, frames=100, interval=1)

writervieo = animation.FFMpegWriter(fps=120)

plt.show()