import math

from cyclops import *
from euclid import *
from omega import *


from daInput.cursor.mocap.MocapCursor import MocapCursor


class OptiTrackMocapCursor(MocapCursor):

    #MOTION_MULTIPLIER = 0.5   # scaling factor

    def __init__(self, id, user_id, geometry, ui_context, mapping):
        super(OptiTrackMocapCursor, self).__init__(id, user_id, geometry, ui_context)

        #self.current = None
        self.mapping = mapping

    def on_move(self, event):
        position = event.getPosition()

        x = self.mapping.map_x(position.x, position.z)
        y = self.mapping.map_y(position.y, position.z)

        self.translate(x, y)

        #if self.current:
        #    dx = (self.current.x - event.getPosition().x) * OptiTrackMocapCursor.MOTION_MULTIPLIER
        #    dy = (self.current.y - event.getPosition().y) * OptiTrackMocapCursor.MOTION_MULTIPLIER

        #    self.translate(dx, -dy)  # invert the y-axis

        #self.current = Vector2(event.getPosition().x, event.getPosition().y)

    def on_button_up(self, event):
        super(OptiTrackMocapCursor, self).on_button_up(event)

        pass    # TODO: add custom optitrack marker specific button up logic here

    def on_button_down(self, event):
        super(OptiTrackMocapCursor, self).on_button_down(event)

        pass    # TODO: add custom optitrack marker specific button down logic here
