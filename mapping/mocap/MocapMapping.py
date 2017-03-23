class MocapMapping(object):
    """
    Algorithm to map 3-dimensional motion capture marker positions into normalised
    2-dimensional coordinates (e.g., corresponding to positions on a display screen)
    """

    def __init__(self):
        super(MocapMapping, self).__init__()

    def map_x(self, x, z):
        raise NotImplementedError

    def map_y(self, y, z):
        raise NotImplementedError
