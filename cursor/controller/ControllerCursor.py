from omega import *
from omegaToolkit import *

from daInput.cursor.CustomGeometryCursor import CustomGeometryCursor


class ControllerCursor(CustomGeometryCursor):
    """
    Base class for all cursors of the controller type.
    """

    @staticmethod
    def is_interested(event):
        return event.getServiceType() == ServiceType.Controller

    def __init__(self, id, user_id, geometry):
        super(ControllerCursor, self).__init__(id, user_id, geometry)

    def on_event(self, event):

        if ControllerCursor.is_interested(event):

            if event.getType() == EventType.Up:
                self.on_button_up(event)
            elif event.getType() == EventType.Down:
                self.on_button_down(event)
            elif event.getType() == EventType.Update:
                self.on_move(event)
