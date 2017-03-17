import math

from omega import *
from euclid import *

from daInput.cursor.NormalisedCoordinatesCursor import NormalisedCoordinatesCursor


class CustomGeometryCursor(NormalisedCoordinatesCursor):

    def __init__(self, id, user_id, geometry):
        super(CustomGeometryCursor, self).__init__(id)

        self.user_id = user_id
        self.geometry = geometry

    def get_user_id(self):
        return self.user_id

    def translate(self, dx, dy, dz):

        translation = Vector3(0, 0, 0)
        coordinates = Vector3(self.coordinates.x, self.coordinates.y, self.coordinates.z)

        if NormalisedCoordinatesCursor.is_normalised(self.coordinates.x + dx):
            coordinates.x = coordinates.x + dx
            translation.x = dx

        if NormalisedCoordinatesCursor.is_normalised(self.coordinates.y + dy):
            coordinates.y = coordinates.y + dy
            translation.y = dy

        if NormalisedCoordinatesCursor.is_normalised(self.coordinates.z + dz):
            coordinates.z = coordinates.z + dz
            translation.z = dz

        self.set_coordinates(coordinates)
        self.geometry.translate(translation, Space.World)   # TODO: need to map normalised coordinates to visible screen region

    def pitch(self, angle):
        self.geometry.rotate(Vector3(1, 0, 0), math.radians(angle), Space.World)

    def roll(self, angle):
        self.geometry.rotate(Vector3(0, 0, 1), math.radians(angle), Space.World)

    def yaw(self, angle):
        self.geometry.rotate(Vector3(0, 1, 0), math.radians(angle), Space.World)

    def on_move(self, event):
        raise NotImplementedError

    def on_button_up(self, event):
        pass    # TODO: do something to indicate click up

    def on_button_down(self, event):
        pass    # TODO: do something to indicate click down
