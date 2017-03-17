from cyclops import *
from euclid import *
from omega import *


from daInput.cursor.controller.ControllerCursor import ControllerCursor


class SpaceNavControllerCursor(ControllerCursor):

    MOTION_MULTIPLIER = 0.05   # scaling factor
    DAMPENING_FACTOR = 0.005   # dampen jitter caused by poor device calibration

    def __init__(self, id, user_id, geometry):
        super(SpaceNavControllerCursor, self).__init__(id, user_id, geometry)

        self.button1Pressed = False
        self.button2Pressed = False

        self.pitch_locked = True
        self.roll_locked = True
        self.yaw_locked = True

    def on_move(self, event):

        if event.getExtraDataItems() >= 3:

            dx = event.getExtraDataFloat(0) * SpaceNavControllerCursor.MOTION_MULTIPLIER
            dy = event.getExtraDataFloat(1) * SpaceNavControllerCursor.MOTION_MULTIPLIER
            dz = event.getExtraDataFloat(2) * SpaceNavControllerCursor.MOTION_MULTIPLIER

            if abs(dx) >= SpaceNavControllerCursor.DAMPENING_FACTOR or abs(dy) >= SpaceNavControllerCursor.DAMPENING_FACTOR or abs(dz) >= SpaceNavControllerCursor.DAMPENING_FACTOR:
                self.translate(dx, -dy, dz)  # invert the y-axis

            pitch = event.getExtraDataFloat(3)
            roll = event.getExtraDataFloat(4)
            yaw = event.getExtraDataFloat(5)

            if not self.pitch_locked and abs(pitch) >= SpaceNavControllerCursor.DAMPENING_FACTOR:
                self.pitch(pitch)

            if not self.roll_locked and abs(roll) >= SpaceNavControllerCursor.DAMPENING_FACTOR:
                self.roll(roll)

            if not self.yaw_locked and abs(yaw) >= SpaceNavControllerCursor.DAMPENING_FACTOR:
                self.yaw(yaw)

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
