from PIL import Image
import math

class SurfaceGradient:
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

        if width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            raise ValueError('Non-positive integer used for width or height')
        
        self.surface = surface
        self.canvas = Image.new('RGB', (self.width, self.height))

        self.drawGradient()
    
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



def sineSurface(x, y):
    return 127 * (math.cos(math.sqrt((x-200)**2 + (y-200)**2) / 10) + 1)

if __name__ == '__main__':
    g = SurfaceGradient(500, 500, sineSurface)
    g.show()