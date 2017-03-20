from cyclops import *
from euclid import *
from omega import *


from daInput.cursor.mocap.MocapCursor import MocapCursor


class OptiTrackMocapCursor(MocapCursor):

    def __init__(self, id, user_id, geometry, ui_context):
        super(OptiTrackMocapCursor, self).__init__(id, user_id, geometry, ui_context)

    def on_move(self, event):

        if event.getExtraDataItems() >= 2:

            # TODO: this implementation is a guess - confirm actual behaviour

            current = self.get_position()

            dx = event.getPosition().x - current.x
            dy = event.getPosition().y - current.y

            self.translate(dx, dy)  # TODO: do we need to invert the y-axis?

    def on_button_up(self, event):
        super(OptiTrackMocapCursor, self).on_button_up(event)

        pass    # TODO: add custom optitrack marker specific button up logic here

    def on_button_down(self, event):
        super(OptiTrackMocapCursor, self).on_button_down(event)

        pass    # TODO: add custom optitrack marker specific button down logic here
