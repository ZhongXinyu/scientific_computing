# For local execution (does not require installing the library):
import sys; sys.path.append('../')

# OSMNX
import osmnx as ox
# Matplotlib-related
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

City="Cambridge"
#list: Address[City][#]
#0:Location
#1:Size
#2:Location Displayed
Address={
    "Cambridge":[(52.2053,0.1200),1500,"52°12′19″N 0°07′09″E"],
    "Nanjing":(32.0573690, 118.7606900),
    "南京":(32.0573690, 118.7606900),
    "Singapore":(0,0)
}

xmin, ymin, xmax, ymax = 301712.74114666076, 5786282.341528043, 304712.74114666076, 5789282.341528043
dx, dy = xmax-xmin, ymax-ymin
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.text(
    xmin+.5*dx, 
    ymin-0.08*dy,
    f'{City}',
    fontweight='bold',
    color = '#2F3737',
    horizontalalignment='center',
    fontproperties = fm.FontProperties(
        fname = 'Copenhagen.ttf'
    ),
    size = 100
)

ax.text(
    xmin+.5*dx, 
    ymin-0.1*dy,
    Address[City][2],
    fontweight='bold',
    color = '#2F3737',
    horizontalalignment='center',
    fontproperties = fm.FontProperties( 
        size = 20
    )
)
'''
rect = plt.Rectangle(
    # (lower-left corner), width, height
    (xmin, ymin), dx*0.8, dy*0.8, fill=False, lw=10, 
    zorder=0
)
'''

plt.savefig('Frame.png', dpi=200)
print (xmin,ymin,xmax,ymax)