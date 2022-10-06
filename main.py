from gradients import SurfaceGradient
from color import Colormap

def surface(x, y):
    return (x+y)/10

# g = SurfaceGradient(800, 800, surface)
# g.show()

m = Colormap((255, 0, 0), (0, 0, 255), [1, 10])