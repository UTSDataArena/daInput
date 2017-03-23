import math

from daInput.cursor.mocap.MocapCursor import MocapCursor
from daInput.mapping.mocap.MocapMapping import MocapMapping


class DataArenaMocapMapping(MocapMapping):

    # The purpose of this mapping is to convert three dimensional values in the
    # motion capture coordinate system into a two dimensional normalised space.
    #
    # The motion capture tracking coordinate system is set up in the following way
    # from the perspective of a user standing in the centre of the data arena with
    # the entrance directly behind them:
    #
    #   - origin is below user's feet, with positive y axis pointing up from floor
    #   - x axis runs through origin right to left (positive x on user's left)
    #   - z axis runs through origin back to front (positive z in front of user)
    #
    # If we imagine a seam running top to bottom through the data arena display
    # directly behind the user, and were to unwrap the sides of the cylindrical
    # arena display to form a flat rectangle in front of the user, then the normalised
    # coordinates would be laid out as follows:
    #
    #   - x axis runs left to right, ranging in value from 0 to 1
    #   - y axis runs bottom to top, ranging in value from 0 to 1

    def __init__(self, min_y=1.0, max_y=1.5):
        super(DataArenaMocapMapping, self).__init__()

        self.min_y = min_y
        self.max_y = max_y

        self.x_reciprocal = 1 / 360.0
        self.y_reciprocal = 1 / 22.5

        self.clamped_y_reciprocal = 1 / (self.max_y - self.min_y)

    def map_x(self, x, z):

        # we calculate the polar angle of the tracker x-z coordinates and map this
        # angle into a normalised position around the circumference of the data arena
        # display

        angle = math.degrees(math.atan2(x, -z))
        angle = angle if angle > 0 else 360 + angle

        return angle * self.x_reciprocal

    def map_y(self, y, z):

        # we clamp the y position of the tracker coordinates to a normalised
        # vertical slice of the motion capture region within the data arena
        # before calculating a polar angle and mapping it into a normalised height
        # position on the data arena display

        if y <= self.min_y:
            return MocapCursor.MIN_RANGE_VALUE
        elif y >= self.max_y:
            return MocapCursor.MAX_RANGE_VALUE
        else:
            normalised_y = (y - self.min_y) * self.clamped_y_reciprocal
            angle = math.degrees(math.atan2(normalised_y, abs(z)))

            return angle * self.y_reciprocal


