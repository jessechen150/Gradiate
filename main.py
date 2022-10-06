from gradients import SurfaceGradient
from color import Colormap

def surface(x, y):
    return (x+y)/10

m = Colormap(
    color1=(255, 0, 0), 
    color2=(0, 0, 255), 
    domain=[0, 160], 
    resolution=99)
g = SurfaceGradient(800, 800, m, surface)
g.show()