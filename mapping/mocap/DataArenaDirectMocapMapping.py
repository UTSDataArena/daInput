from daInput.mapping.mocap.MocapMapping import MocapMapping


class DataArenaDirectMocapMapping(MocapMapping):

    def __init__(self, min_x=-4.0, max_x=4.0, min_y=1.0, max_y=1.7, max_z=4.0, min_z=-4.0):
        super(DataArenaDirectMocapMapping, self).__init__()

        self.min_y = min_y
        self.max_y = max_y

        self.min_x = min_x
        self.max_x = max_x

        self.min_z = min_z
        self.max_z = max_z

        self.y_reciprocal = 1 / (self.max_y - self.min_y)
        self.x_reciprocal = 1 / (self.max_x - self.min_x)
        self.z_reciprocal = 1 / (self.max_z - self.min_z)

    def map_x(self, x):

        # flip the x position of the tracker coordinates and convert to a
        # normalised value

        return (-x + self.max_x) * self.x_reciprocal

    def map_y(self, y):

        # we clamp the y position of the tracker coordinates to a normalised
        # vertical slice of the motion capture region within the data arena

        return (y - self.min_y) * self.y_reciprocal

    def map_z(self, z):

        # convert the z position of the tracker coordinates to a normalised
        # value

        return (-z + self.max_z) * self.z_reciprocal

    def in_active_region(self, position):
        return self.min_y <= position.y <= self.max_y
