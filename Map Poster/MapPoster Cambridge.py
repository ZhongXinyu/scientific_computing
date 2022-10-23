# For local execution (does not require installing the library):
import sys; sys.path.append('../')

# Prettymaps
from prettymaps import *
# Vsketch
import vsketch
# OSMNX
import osmnx as ox
# Matplotlib-related
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
# Shapely
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union
fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

City="Cambridge"
#list: Address[City][#]
#0:Location
#1:Size
#2:Location Displayed
Address={
    "Cambridge":[(52.2053,0.1180),2000,"52°12′19″N 0°07′09″E"],
    "Nanjing":[(32.0573690, 118.7606900),10000,"Home"],
    "南京":[(32.0573690, 118.7606900),10000,"Home"],
    "Singapore":[(1.3378141, 103.8192512),10000,"1.3521° N, 103.8198° E"]
}
layers = plot(
    # Address:
    #'Praça Ferreira do Amaral, Macau',
    Address[City][0],
    # Plot geometries in a circle of radius:
    radius = Address[City][1],
    # Matplotlib axis
    ax = ax,
    # Which OpenStreetMap layers to plot and their parameters:
    layers = {
            # Perimeter (in this case, a circle)
            'perimeter': {},
            # Streets and their widths
            'streets': {
                'width': {
                    'motorway': 4,
                    'trunk': 4,
                    'primary': 4,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'footway': 1,
                }
            },
            # Other layers:
            #   Specify a name (for example, 'building') and which OpenStreetMap tags to fetch
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
            'forest': {'tags': {'landuse': 'forest'}},
            'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
        },
        # drawing_kwargs:
        #   Reference a name previously defined in the 'layers' argument and specify matplotlib parameters to draw it
        drawing_kwargs = {
            'background': {'fc': '#ffffff', 'ec': '#dadbc1',  'zorder': -1},
            'perimeter': {'fc': '#ffffff', 'ec': '#dadbc1', 'lw': 0, 'zorder': 0},
            'green': {'fc': '#ffffff', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#ffffff', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#ffffff', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
            'parking': {'fc': '#ffffff', 'ec': '#ffffff', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#2F3737', 'ec': '#2F3737', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'building': {'palette': ['#bfbfbf', '#d4d4d4', '#eaeaea'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
        }
)
xmin, ymin, xmax, ymax = layers['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.text(
    xmin+.5*dx, 
    ymin-0.18*dy,
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
    ymin-0.2*dy,
    Address[City][2],
    fontweight='bold',
    color = '#2F3737',
    horizontalalignment='center',
    fontproperties = fm.FontProperties( 
        size = 20
    )
)


plt.savefig(f'{City}.png', dpi=500)
print (xmin,ymin,xmax,ymax)