from cyclops import *
from euclid import *
from omega import *


from daInput.cursor.controller.ControllerCursor import ControllerCursor


class SpaceNavControllerCursor(ControllerCursor):

    MOTION_MULTIPLIER = 0.005   # scaling factor
    DAMPENING_FACTOR = 0.0005   # dampen jitter caused by poor device calibration

    def __init__(self, id, user_id, geometry, ui_context):
        super(SpaceNavControllerCursor, self).__init__(id, user_id, geometry, ui_context)

        self.button1Pressed = False
        self.button2Pressed = False

    def on_move(self, event):

        # The spacenav VRPN driver emits 6 channels of motion data:
        #
        #   x, y, z, pitch, roll, yaw
        #
        # Values corresponding to motion in each of these channels is written to
        # the extra data structure included in each event generated by Omegalib.
        #
        # For simplicity, we currently make use of the x and y channels only.

        if event.getExtraDataItems() >= 2:

            dx = event.getExtraDataFloat(0) * SpaceNavControllerCursor.MOTION_MULTIPLIER
            dy = event.getExtraDataFloat(1) * SpaceNavControllerCursor.MOTION_MULTIPLIER
            dz = event.getExtraDataItems(2) * SpaceNavControllerCursor.MOTION_MULTIPLIER

            if abs(dx) >= SpaceNavControllerCursor.DAMPENING_FACTOR or abs(dy) >= SpaceNavControllerCursor.DAMPENING_FACTOR or abs(dz) >= SpaceNavControllerCursor.DAMPENING_FACTOR:
                self.move(self.coordinates.x + dx, self.coordinates.y + dy, self.coordinates.z + dz)

    def on_button_up(self, event):
        super(SpaceNavControllerCursor, self).on_button_up(event)

        if event.isButtonUp(EventFlags.Button1):
            self.button1Pressed = False
        elif event.isButtonUp(EventFlags.Button2):
            self.button2Pressed = False

    def on_button_down(self, event):
        super(SpaceNavControllerCursor, self).on_button_down(event)

        if event.isButtonDown(EventFlags.Button1):
            self.button1Pressed = True
        elif event.isButtonDown(EventFlags.Button2):
            self.button2Pressed = True
