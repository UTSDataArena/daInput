from cyclops import *

from daInput.geometry.CursorGeometryBuilder import CursorGeometryBuilder


class SphereCursorGeometryBuilder(CursorGeometryBuilder):

    DEFAULT_RADIUS = 0.1
    DEFAULT_SUBDIVISIONS = 1
    DEFAULT_EFFECT = 'colored -d red'

    def __init__(self):
        super(SphereCursorGeometryBuilder, self).__init__()

        self.radius = SphereCursorGeometryBuilder.DEFAULT_RADIUS
        self.subdivisions = SphereCursorGeometryBuilder.DEFAULT_SUBDIVISIONS

        self.effect = SphereCursorGeometryBuilder.DEFAULT_EFFECT

    def set_radius(self, radius):
        self.radius = radius
        return self

    def set_subdivisions(self, subdivisions):
        self.subdivisions = subdivisions
        return self

    def set_effect(self, effect):
        self.effect = effect
        return self

    def build(self):
        geo = SphereShape.create(self.radius, self.subdivisions)
        geo.setPosition(self.position[0], self.position[1], self.position[2])
        geo.setEffect(self.effect)

        return geo
