import math

from omega import *
from euclid import *

from daInput.cursor.NormalisedCoordinatesCursor import NormalisedCoordinatesCursor


class CustomGeometryCursor(NormalisedCoordinatesCursor):

    def __init__(self, id, user_id, geometry, ui_context, cursor_plane_width=8.0, cursor_plane_height=None, cursor_plane_depth=8.0):
        super(CustomGeometryCursor, self).__init__(id)

        self.user_id = user_id
        self.geometry = geometry

        self.ui_context = ui_context

        self.cursor_plane_height = cursor_plane_height if cursor_plane_height else abs(2.0 * self.geometry.getPosition().z * math.tan(math.radians(self.ui_context.fov * 0.5)))
        self.cursor_plane_width = cursor_plane_width
        self.cursor_plane_depth = cursor_plane_depth

    def get_user_id(self):
        return self.user_id

    def get_position(self):
        return self.geometry.getPosition()

    def get_direction(self, camera):
        direction = self.get_position() - camera.getHeadOffset()
        direction = camera.getOrientation() * direction
        direction.normalize()

        return direction

    def move(self, x, y, z):

        translation = Vector3(0, 0, 0)
        coordinates = Vector3(self.coordinates.x, self.coordinates.y, self.coordinates.z)

        delta = Vector3(x - self.coordinates.x, y - self.coordinates.y, z - self.coordinates.z)

        if NormalisedCoordinatesCursor.is_normalised(x):
            coordinates.x = x
            translation.x = delta.x * self.cursor_plane_width

        if NormalisedCoordinatesCursor.is_normalised(y):
            coordinates.y = y
            translation.y = delta.y * self.cursor_plane_height

        if NormalisedCoordinatesCursor.is_normalised(z):
            coordinates.z = z
            translation.z = delta.z * self.cursor_plane_depth

        self.set_coordinates(coordinates)
        self.geometry.translate(translation, Space.World)

    def on_move(self, event):
        raise NotImplementedError

    def on_button_up(self, event):
        pass    # TODO: do something to indicate click up

    def on_button_down(self, event):
        pass    # TODO: do something to indicate click down
