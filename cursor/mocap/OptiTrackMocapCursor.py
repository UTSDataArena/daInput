from cyclops import *
from euclid import *
from omega import *


from daInput.cursor.mocap.MocapCursor import MocapCursor


class OptiTrackMocapCursor(MocapCursor):

    def __init__(self, id, user_id, geometry, mapping, ui_context):
        super(OptiTrackMocapCursor, self).__init__(id, user_id, geometry, ui_context)

        self.mapping = mapping

    def on_move(self, event):
        position = event.getPosition()

        if self.mapping.in_active_region(position):

            x = self.mapping.map_x(position.x)
            y = self.mapping.map_y(position.y)
            z = self.mapping.map_z(position.z)

            self.move(x, y, z)

    def on_button_up(self, event):
        super(OptiTrackMocapCursor, self).on_button_up(event)

        pass    # TODO: add custom optitrack marker specific button up logic here

    def on_button_down(self, event):
        super(OptiTrackMocapCursor, self).on_button_down(event)

        pass    # TODO: add custom optitrack marker specific button down logic here
