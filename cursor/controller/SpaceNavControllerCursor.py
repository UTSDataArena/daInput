from cyclops import *
from euclid import *
from omega import *


from daInput.cursor.controller.ControllerCursor import ControllerCursor


class SpaceNavControllerCursor(ControllerCursor):

    MOTION_MULTIPLIER = 0.01   # scaling factor

    def __init__(self, id, user_id, cursor_up_image_path, cursor_down_image_path, ui_context):
        super(SpaceNavControllerCursor, self).__init__(id, user_id, cursor_up_image_path, cursor_down_image_path, ui_context)

        self.button1Pressed = False
        self.button2Pressed = False

    def on_move(self, event):

        # This cursor currently makes use of the x and y motion channels of the
        # spacenav VRPN input events only. These events actually contain values
        # for all 6 input channels of the device, which are as follows:
        #
        #   0 - x (left/right)
        #   1 - y (forward/back)
        #   2 - z (up/down)
        #   3 - pitch (tilt forward/back)
        #   4 - roll (tilt left/right)
        #   5 - yaw (twist left/right)
        #
        # The raw VRPN output is stored within the event extra data properties
        # by omegalib.

        if event.getExtraDataItems() >= 2:

            dx = event.getExtraDataFloat(0)
            dy = event.getExtraDataFloat(1)

            x = self.get_coordinates().x + (dx * SpaceNavControllerCursor.MOTION_MULTIPLIER)
            y = self.get_coordinates().y + (dy * SpaceNavControllerCursor.MOTION_MULTIPLIER)

            self.set_coordinates(Vector2(x, y))

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
