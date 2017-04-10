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

    If we imagine a seam running top to bottom through the data arena display
    directly behind the user, and were to unwrap the sides of the cylindrical
    arena display to form a flat rectangle in front of the user, then the normalised
    coordinates would be laid out as follows:

       - x axis runs left to right, ranging in value from 0 to 1
       - y axis runs bottom to top, ranging in value from 0 to 1
    """

    def __init__(self):
        super(MocapMapping, self).__init__()

    def map_x(self, x, z):
        raise NotImplementedError

    def map_y(self, y, z):
        raise NotImplementedError
