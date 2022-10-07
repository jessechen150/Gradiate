from PIL import Image



class Colormap:
    """
    Colormap between two or more colors.
    """
    
    def __init__(self, color1, color2, domain, family='linear', mode='RGB', resolution=99):
        """
        Creates a color map between `color1` and `color2`,
        which maps to `domain` (list or tuple of length 2,
        where the domain[0] <= domain[1]).

        `family` specifies the type of color map.
        `mode` specifies the color space.
        `resolution` + 1 is the number of colors in the map.
        """

        self.color1 = color1
        self.color2 = color2
        self.domain = domain
        self.family = family
        self.mode = mode
        self.resolution = resolution

        if family not in ('linear'):
            raise ValueError('Unsupported colormap family')
        if mode not in ('RGB'):
            raise ValueError('Unsupported color space')
        if not isinstance(resolution, int) or resolution < 0:
            raise ValueError('Resolution must be a positive integer')

        if family == 'linear':
            self.map = self.linearMap()

    def linearMap(self):
        """
        Returns the linear interpolation from `color1`
        to `color2` in RGB space with `resolution` + 1 
        number of colors.
        """

        xStep = (self.color2[0] - self.color1[0]) / self.resolution
        yStep = (self.color2[1] - self.color1[1]) / self.resolution
        zStep = (self.color2[2] - self.color1[2]) / self.resolution

        currentColor = list(self.color1)
        colorMap = []
        for i in range(self.resolution):
            colorMap.append(tuple(map(int, currentColor)))
            currentColor[0] += xStep
            currentColor[1] += yStep
            currentColor[2] += zStep
        colorMap.append(self.color2)

        return colorMap

    def show(self):
        """
        Displays the colorMap in a 
        len(colorMap) by 50 rectangle.
         """

        canvas = Image.new(self.mode, (len(self.map), 50))
        for i in range(len(self.map)):
            for j in range(50):
                canvas.putpixel((i,j), self.map[i])
        canvas.show()

    def combineWith(self, colormap):
        """
        Directly append `colormap` to this
        instance's colormap.
        """
        if self.mode != colormap.mode:
            raise ValueError("Unsupported combination with two different color spaces")
        self.map += colormap.map
        self.resolution += colormap.resolution
    
    def domainToColor(self, n):
        """
        Returns the associated color from the color map
        given `n`, a number within the domain.
        """

        if n > self.domain[1] or n < self.domain[0]:
            raise ValueError('number is outside the domain')
        
        normalizedPosition = (n - self.domain[0]) / (self.domain[1] - self.domain[0])
        index = int((len(self.map) - 1) * normalizedPosition)
        return self.map[index]
