from PIL import Image



class Gradient:
    """
    Abstract gradient class to be inherited.
    """

    def __init__(self, width, height):
        """
        Creates a blank canvas for subclasses
        to draw gradients on.
        """

        if width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            raise ValueError('Non-positive integer used for width or height')
        
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

    def __init__(self, width, height, surface):
        """
        Initializes the gradient image where
        `width` and `height` are the dimensions of
        the image and `surface` is a function that maps
        (x,y) to a value.
        """

        self.surface = surface
        super().__init__(width, height)
    
    def drawGradient(self):
        """
        Draws the gradient on the canvas using
        the given surface.
        """
        for x in range(self.width):
            for y in range(self.height):
                surfaceValue = int(self.surface(x, y))
                grayValue = None
                if surfaceValue < 0:
                    grayValue = 0
                elif surfaceValue > 255:
                    grayValue = 255
                else:
                    grayValue = surfaceValue

                self.canvas.putpixel((x,y), (grayValue, grayValue, grayValue))
