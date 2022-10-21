from PIL import Image

class Gradient:
    """
    Abstract gradient class to be inherited.
    """

    def __init__(self, dimensions, colormap):
        """
        Creates a blank canvas for subclasses
        to draw gradients on.
        """

        if width > 0 and height > 0:
            self.width = dimensions[0]
            self.height = dimensions[1]
        else:
            raise ValueError('Non-positive integer used for width or height')
        
        self.map = colormap
        self.canvas = Image.new('RGB', (self.width, self.height))
        self.drawGradient()
    
    def drawGradient(self):
        """
        To be overwritten in subclasses.
        """
        pass
    
    def save(self, path):
        """
        Save canvas to path.
        """
        self.canvas.save(path)

    def show(self):
        """
        Display the canvas in the operating system's
        default image viewer.
        """
        self.canvas.show()



class SurfaceGradient(Gradient):
    """
    Gradient defined by a 3D surface.
    """

    def __init__(self, dimensions, colormap, surface):
        """
        Initializes the gradient image with
        dimensions `dimensions` and `surface` 
        is a function that maps (x,y) to a value.
        """

        self.surface = surface
        super().__init__(dimensions, colormap)
    
    def drawGradient(self):
        """
        Draws the gradient on the canvas using
        the given surface.
        """
        minSV = int(self.surface(0, 0))
        maxSV = int(self.surface(0, 0))

        for x in range(self.width):
            for y in range(self.height):
                surfaceValue = self.surface(x, y)
                minSV = min(minSV, surfaceValue)
                maxSV = max(maxSV, surfaceValue)
                
                try:
                    color = self.map.domainToColor(surfaceValue)
                except ValueError:
                    # If value is out of the domain, use magenta
                    color = (255, 0, 255)
                self.canvas.putpixel((x,y), color)
        
        print(f"Surface value range: [{minSV},{maxSV}]")

    
class CurveGradient(Gradient):
    """
    Gradient defined by a 2D curve.
    """

    def __init__(self, dimensions, colormap, curve):
        """
        Initializes the gradient image with
        dimensions `dimensions` and `curve` 
        is a function that maps (x,y) to a 1 if
        it is on the curve or 0 if it is not..
        """

        self.curve = curve
        super().__init__(dimensions, colormap)

    def drawGradient(self):
        """
        Draws the gradient on the canvas using
        the given surface.
        """
        pass