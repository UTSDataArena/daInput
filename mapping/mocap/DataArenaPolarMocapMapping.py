import math

from daInput.mapping.mocap.MocapMapping import MocapMapping


class DataArenaPolarMocapMapping(MocapMapping):

    # Map motion in the data arena along x and z axes into polar coordinates which
    # are normalised and mapped to the surface of the data arena display.
    #
    # If we imagine a seam running top to bottom through the data arena display
    # directly behind the user, and were to unwrap the sides of the cylindrical
    # arena display to form a flat rectangle in front of the user, then the normalised
    # coordinates would be laid out as follows:
    #
    #   - x axis runs left to right, ranging in value from 0 to 1
    #   - y axis runs bottom to top, ranging in value from 0 to 1

    def __init__(self, min_y=1.0, max_y=1.7):
        super(DataArenaPolarMocapMapping, self).__init__()

        self.min_y = min_y
        self.max_y = max_y

        self.x_reciprocal = 1 / 360.0
        self.y_reciprocal = 1 / (self.max_y - self.min_y)

        # keep track of current set of mapped values for diagnostics purposes:

        self.x = 0.0
        self.y = 0.0
        self.angle = 0

    def map_x(self, x, z):

        # we calculate the polar angle of the tracker x-z coordinates and map this
        # angle into a normalised position around the circumference of the data arena
        # display

        angle = math.degrees(math.atan2(-x, -z))
        angle = 360 - angle if angle > 0 else -angle

        self.angle = angle
        self.x = angle * self.x_reciprocal

        return self.x

    def map_y(self, y):

        # we clamp the y position of the tracker coordinates to a normalised
        # vertical slice of the motion capture region within the data arena

        self.y = (y - self.min_y) * self.y_reciprocal

        return self.y

    def in_active_region(self, position):
        return self.min_y <= position.y <= self.max_y


