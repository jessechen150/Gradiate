class Colormap:
    """
    Static class for holding various
    methods relating to color maps.
    """

    @staticmethod
    def linearMap(color1, color2, colorSpace, resolution=100):
        """
        Returns a `resolution`-length list of
        a linear interpolation between `color1` and
        `color2` in color space `colorSpace`.

        Currently supported color spaces:
            * RGB in format (r, g, b)
        """

        if colorSpace == 'RGB':
            return Colormap.linearMapRGB(color1, color2, resolution)
        else:
            raise NotImplemented


    @staticmethod
    def linearMapRGB(color1, color2, resolution=100):
        """
        Returns the linear interpolation from `color1`
        to `color2` in RGB space.
        """
        
        pass
