from euclid import *
from omega import *
from omegaToolkit import *

from daInput.cursor.Cursor import Cursor


class NormalisedCoordinatesCursor(Cursor):
    """
    Represents a cursor with motion restricted to a range between 0 and 1 in the X and Y dimensions.
    """

    MIN_RANGE_VALUE = 0
    MAX_RANGE_VALUE = 1

    @staticmethod
    def is_normalised(coordinates):

        x_normalised = NormalisedCoordinatesCursor.MIN_RANGE_VALUE <= coordinates.x <= NormalisedCoordinatesCursor.MAX_RANGE_VALUE
        y_normalised = NormalisedCoordinatesCursor.MIN_RANGE_VALUE <= coordinates.y <= NormalisedCoordinatesCursor.MAX_RANGE_VALUE

        return x_normalised and y_normalised

    def __init__(self, id):
        super(NormalisedCoordinatesCursor, self).__init__(id)

        self.coordinates = Vector2(NormalisedCoordinatesCursor.MIN_RANGE_VALUE, NormalisedCoordinatesCursor.MIN_RANGE_VALUE)

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
