from euclid import *
from omega import *
from omegaToolkit import *

from daInput.cursor.Cursor import Cursor


class NormalisedCoordinatesCursor(Cursor):
    """
    Represents a cursor with motion restricted to a range between 0 and 1 within each dimension.
    """

    MIN_RANGE_VALUE = 0
    MAX_RANGE_VALUE = 1

    @staticmethod
    def is_normalised(coordinate):
        return NormalisedCoordinatesCursor.MIN_RANGE_VALUE <= coordinate <= NormalisedCoordinatesCursor.MAX_RANGE_VALUE

    def __init__(self, id):
        super(NormalisedCoordinatesCursor, self).__init__(id)

        self.coordinates = Vector3(NormalisedCoordinatesCursor.MAX_RANGE_VALUE * 0.5, NormalisedCoordinatesCursor.MAX_RANGE_VALUE * 0.5, NormalisedCoordinatesCursor.MAX_RANGE_VALUE * 0.5)

    def get_coordinates(self):
        """
        Return the normalised coordinates which represent the current position of
        the cursor within a "uv" space that defines the total display area.
        """
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
