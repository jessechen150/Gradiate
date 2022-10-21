from gradients import SurfaceGradient
from color import Colormap
import math

res = 99
domain = [0, 200]

m1 = Colormap(
    color1=(0, 0, 0), 
    color2=(46, 22, 92), 
    domain=domain, 
    resolution=res)

m2 = Colormap(
    color1=(46, 22, 92),
    color2=(184, 98, 33),
    domain=domain, 
    resolution=res)

m3 = Colormap(
    color1=(184, 98, 33),
    color2=(255, 231, 125),
    domain=domain, 
    resolution=res)

m4 = Colormap(
    color1=(255, 231, 125),
    color2=(255, 250, 227),
    domain=domain, 
    resolution=res)


m1.combineWith(m2)
m1.combineWith(m3)
m1.combineWith(m4)

 
# def surface(x, y):
#     return 100*math.pow(math.e, -0.1 * (((2*x)/100-(((y-200)/100)**3))**2))

def blob(x, y):
    x = (x-100)/100
    y = (y-100)/100
    return 100*math.pow(math.e, -x**2 - y**2)

g = SurfaceGradient(800, 500, m1, blob)
g.show()
g.save("gradient.png")