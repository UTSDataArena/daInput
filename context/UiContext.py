from euclid import *
from omega import *
from omegaToolkit import *

from daInput.cursor.pointer.MousePointerCursor import MousePointerCursor


class UiContext(object):

    DEFAULT_CAMERA_FOV = 34.7

    @staticmethod
    def calculate_aspect():
        config = getDisplayConfig()
        size = getDisplayPixelSize()

        width = float(size[0]) / 2 if config.stereoMode == StereoMode.SideBySide else float(size[0])
        height = float(size[1]) / 2 if config.stereoMode == StereoMode.TopBottom else float(size[1])

        return width / height

    def __init__(self):
        super(UiContext, self).__init__()

        self.fov = UiContext.DEFAULT_CAMERA_FOV
        self.aspect = UiContext.calculate_aspect()

        self.pointer = MousePointerCursor('mouse')
        self.cursors = []

    def get_cursor(self, event):
        for cursor in self.cursors:
            if cursor.get_user_id() == event.getUserId():
                return cursor

    def add_cursor(self, cursor):
        self.cursors.append(cursor)

    def on_event(self, event):
        for cursor in self.cursors:
            cursor.on_event(event)
