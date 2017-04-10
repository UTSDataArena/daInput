from euclid import *
from omega import *
from omegaToolkit import *

from daInput.cursor.pointer.MousePointerCursor import MousePointerCursor


class UiContext(object):

    DEFAULT_CAMERA_FOV = 34.7

    def __init__(self, fov=DEFAULT_CAMERA_FOV):
        super(UiContext, self).__init__()

        self.fov = fov

        self.pointer = MousePointerCursor('mouse')
        self.cursors = []

        self.ui = UiModule.createAndInitialize()

    def get_cursor(self, event):
        for cursor in self.cursors:
            if cursor.get_user_id() == event.getUserId():
                return cursor

    def add_cursor(self, cursor):
        self.cursors.append(cursor)

    def on_event(self, event):
        for cursor in self.cursors:
            cursor.on_event(event)
