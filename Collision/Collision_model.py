import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools

class Canvas():
    def __init__(self):
        self.size = 20
        self.blocks = []
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()
        
    def add_block(self,block):
        self.blocks.append(block)
        
    def update_blocks(self):
        self.ax.clear()
        for i, block in enumerate(self.blocks):
            block.move()
            block.draw(markersize=block.radius)
            
    def fix_axes(self):
        self.ax.set_xlim((-self.size/2,self.size/2))
        self.ax.set_ylim((-1,1))
        
    def check_collision(self):
        combinations = list(itertools.combinations(range(len(self.blocks)),2))
        for pair in combinations:
            self.blocks[pair[0]].collide(self.blocks[pair[1]])
            
class Block():
    def __init__(self,canvas,mass,position=0,velocity=0):
        self.canvas = canvas
        self.mass = mass
        self.radius = 10*mass**0.33
        self.position = position
        self.velocity = velocity
        self.canvas.add_block(self)
        self.color = "black"
        
    def move(self):
        self.position = self.position + self.velocity
        
    def draw(self,markersize):
        canvas.ax.plot(self.position,0,"o",markersize=markersize)
        
    def collide(self,other):
        m1=self.mass
        m2=other.mass
        v1=self.velocity
        v2=other.velocity
        e=1
        if abs(self.position)+self.radius/31 > canvas.size/2:
            self.velocity *= -1
        if abs(other.position)+other.radius/31 > canvas.size/2:
            other.velocity *= -1
        if abs(self.position - other.position) < abs(self.radius + other.radius)/31:
            self.velocity = ((m1 - m2)*v1 + 2*m2*v2)/(m1 + m2) *e
            other.velocity = ((m2 - m1)*v2 + 2*m1*v1)/(m1 + m2) *e
        

canvas = Canvas()

block1 = Block(canvas,mass=5,position=-2,velocity=0.1)
block2 = Block(canvas,mass=1,position=2,velocity=-0.1)
block3 = Block(canvas,mass=2,position=4,velocity=-0.1)
block4 = Block(canvas,mass=10,position=-5,velocity=0.1)

def animate(i):
    print("The frame is:", i)
    canvas.update_blocks()
    canvas.check_collision()
    canvas.fix_axes()

anim = animation.FuncAnimation(canvas.fig, animate,frames=500, interval=100)
writer= animation.FFMpegWriter()
#anim.save("Collision.mp4",writer=writer)
plt.show()
