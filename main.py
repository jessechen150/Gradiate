from gradients import SurfaceGradient

def surface(x, y):
    return (x+y)/10

g = SurfaceGradient(800, 800, surface)
g.show()