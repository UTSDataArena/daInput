from euclid import *
from omega import *
from omegaToolkit import *

from daInput.cursor.NormalisedCoordinatesCursor import NormalisedCoordinatesCursor


class CustomImageCursor(NormalisedCoordinatesCursor):

    @staticmethod
    def load_image(path):
        return loadImage(path) if path else None

    def __init__(self, id, user_id, cursor_up_image_path, cursor_down_image_path, ui_context):
        super(CustomImageCursor, self).__init__(id)

        self.ui_context = ui_context

        self.user_id = user_id

        self.cursor = Image.create(self.ui_context.container)
        self.cursor.setSize(Vector2(CustomImageCursor.DEFAULT_SIZE, CustomImageCursor.DEFAULT_SIZE))

        self.cursor_up_image = CustomImageCursor.load_image(cursor_up_image_path)
        self.cursor_down_image = CustomImageCursor.load_image(cursor_down_image_path)

        if self.cursor_up_image:
            self.cursor.setData(self.cursor_up_image)

    def get_user_id(self):
        return self.user_id

    def get_position(self):
        return self.cursor.getPosition()

    def set_position(self, position):
        dimensions = self.ui_context.container.getSize()
        coordinates = Vector2(position.x / dimensions[0], position.y / dimensions[1])

        if NormalisedCoordinatesCursor.is_normalised(coordinates):
            self.cursor.setPosition(position)

            super(CustomImageCursor, self).set_coordinates(coordinates)

    def set_coordinates(self, coordinates):
        if NormalisedCoordinatesCursor.is_normalised(coordinates):
            super(CustomImageCursor, self).set_coordinates(coordinates)

            dimensions = self.ui_context.container.getSize()
            self.cursor.setPosition(Vector2(dimensions[0] * self.coordinates.x, dimensions[1] * self.coordinates.y))

    def on_move(self, event):
        raise NotImplementedError

    def on_button_up(self, event):
        self.cursor.setData(self.cursor_up_image)

    def on_button_down(self, event):
        self.cursor.setData(self.cursor_down_image)
