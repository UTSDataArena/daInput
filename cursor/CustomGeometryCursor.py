import math

from omega import *
from euclid import *

from daInput.cursor.NormalisedCoordinatesCursor import NormalisedCoordinatesCursor


class CustomGeometryCursor(NormalisedCoordinatesCursor):

    def __init__(self, id, user_id, geometry, ui_context):
        super(CustomGeometryCursor, self).__init__(id)

        self.user_id = user_id
        self.geometry = geometry

        self.ui_context = ui_context

        self.cursor_plane_height = abs(2.0 * self.geometry.getPosition().z * math.tan(math.radians(self.ui_context.fov * 0.5)))
        self.cursor_plane_width = self.cursor_plane_height * self.ui_context.aspect

    def get_user_id(self):
        return self.user_id

    def translate(self, dx, dy):

        translation = Vector3(0, 0, 0)
        coordinates = Vector2(self.coordinates.x, self.coordinates.y)

        if NormalisedCoordinatesCursor.is_normalised(self.coordinates.x + dx):
            coordinates.x = coordinates.x + dx
            translation.x = dx * self.cursor_plane_width

        if NormalisedCoordinatesCursor.is_normalised(self.coordinates.y + dy):
            coordinates.y = coordinates.y + dy
            translation.y = dy * self.cursor_plane_height

        self.set_coordinates(coordinates)
        self.geometry.translate(translation, Space.World)

    def on_move(self, event):
        raise NotImplementedError

    def on_button_up(self, event):
        pass    # TODO: do something to indicate click up

    def on_button_down(self, event):
        pass    # TODO: do something to indicate click down
