class MocapMapping(object):
    """
    Algorithm to map 3-dimensional motion capture marker positions into normalised
    2-dimensional coordinates (e.g., corresponding to positions on a display screen)

    The motion capture tracking coordinate system is set up in the following way
    from the perspective of a user standing in the centre of the data arena with
    the entrance directly behind them:

       - origin is below user's feet, with positive y axis pointing up from floor
       - x axis runs through origin right to left (positive x on user's left)
       - z axis runs through origin back to front (positive z in front of user)
    """

    def __init__(self):
        super(MocapMapping, self).__init__()

    def map_x(self, x, z):
        raise NotImplementedError

    def map_y(self, y, z):
        raise NotImplementedError
