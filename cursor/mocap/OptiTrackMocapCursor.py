from cyclops import *
from euclid import *
from omega import *


from daInput.cursor.mocap.MocapCursor import MocapCursor


class OptiTrackMocapCursor(MocapCursor):

    MOTION_MULTIPLIER = 4

    def __init__(self, id, user_id, geometry, mapping, ui_context):
        super(OptiTrackMocapCursor, self).__init__(id, user_id, geometry, ui_context, OptiTrackMocapCursor.MOTION_MULTIPLIER)

        self.is_active = False

        self.mapping = mapping
        self.origin = Vector3(0, 0, 0)

    def on_move(self, event):
        position = event.getPosition()

        if self.mapping.in_active_region(position):

            if not self.is_active:
                # we re-position the xz origin to wherever the user happens to be when the cursor enters the active region

                self.origin = Vector3(position.x, 0, position.z)
                self.set_coordinates(Vector3(OptiTrackMocapCursor.MAX_RANGE_VALUE * 0.5, self.coordinates.y, OptiTrackMocapCursor.MAX_RANGE_VALUE * 0.5))

                self.is_active = True

            x = self.mapping.map_x(position.x - self.origin.x)
            y = self.mapping.map_y(position.y)
            z = self.mapping.map_z(position.z - self.origin.z)

            self.move(x, y, z)

        else:
            self.is_active = False

    def on_button_up(self, event):
        super(OptiTrackMocapCursor, self).on_button_up(event)

        pass    # TODO: add custom optitrack marker specific button up logic here

    def on_button_down(self, event):
        super(OptiTrackMocapCursor, self).on_button_down(event)

        pass    # TODO: add custom optitrack marker specific button down logic here
