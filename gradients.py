from PIL import Image



class Gradient:
    """
    Abstract gradient class to be inherited.
    """

    def __init__(self, width, height, colormap):
        """
        Creates a blank canvas for subclasses
        to draw gradients on.
        """

        if width > 0 and height > 0:
            self.width = width
            self.height = height
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

    def __init__(self, width, height, colormap, surface):
        """
        Initializes the gradient image where
        `width` and `height` are the dimensions of
        the image and `surface` is a function that maps
        (x,y) to a value.
        """

        self.surface = surface
        super().__init__(width, height, colormap)
    
    def drawGradient(self):
        """
        Draws the gradient on the canvas using
        the given surface.
        """
        for x in range(self.width):
            for y in range(self.height):
                surfaceValue = int(self.surface(x, y))
                try:
                    color = self.map.domainToColor(surfaceValue)
                except ValueError:
                    # If value is out of the domain, use black
                    color = (0, 0, 0)
                self.canvas.putpixel((x,y), color)
