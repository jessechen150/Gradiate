from gradients import SurfaceGradient
from color import Colormap
import math

res = 999

m1 = Colormap(
    color1=(0, 0, 0), 
    color2=(46, 22, 92), 
    domain=[0,942], 
    resolution=res)

m2 = Colormap(
    color1=(46, 22, 92),
    color2=(184, 98, 33),
    domain=[0, 1], 
    resolution=res)

m3 = Colormap(
    color1=(184, 98, 33),
    color2=(255, 231, 125),
    domain=[0, 1], 
    resolution=res)

m4 = Colormap(
    color1=(255, 231, 125),
    color2=(255, 250, 227),
    domain=[0, 1], 
    resolution=res)

m1.combineWith(m2)
m1.combineWith(m3)
m1.combineWith(m4)

def surface(x, y):
    return math.sqrt(x**2 + y**2)

g = SurfaceGradient(800, 500, m1, surface)
g.show()