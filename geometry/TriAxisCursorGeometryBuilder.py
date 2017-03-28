from cyclops import *
from euclid import *
from omega import *

from daInput.geometry.CursorGeometryBuilder import CursorGeometryBuilder


class TriAxisCursorGeometryBuilder(CursorGeometryBuilder):

    DEFAULT_LENGTH = 0.25
    DEFAULT_RADIUS1 = 0.01
    DEFAULT_RADIUS2 = 0.01
    DEFAULT_SUBDIVISIONS = 1
    DEFAULT_SIDES = 16
    DEFAULT_EFFECT = 'colored -d green'

    def __init__(self):
        super(CursorGeometryBuilder, self).__init__()

        self.length = TriAxisCursorGeometryBuilder.DEFAULT_LENGTH
        self.radius1 = TriAxisCursorGeometryBuilder.DEFAULT_RADIUS1
        self.radius2 = TriAxisCursorGeometryBuilder.DEFAULT_RADIUS2
        self.subdivisions = TriAxisCursorGeometryBuilder.DEFAULT_SUBDIVISIONS
        self.sides = TriAxisCursorGeometryBuilder.DEFAULT_SIDES
        self.effect = TriAxisCursorGeometryBuilder.DEFAULT_EFFECT

    def set_length(self, length):
        self.length = length
        return self

    def set_radius1(self, radius1):
        self.radius1 = radius1
        return self

    def set_radius2(self, radius2):
        self.radius2 = radius2
        return self

    def set_subdivisions(self, subdivisions):
        self.subdivisions = subdivisions
        return self

    def set_sides(self, sides):
        self.sides = sides
        return self

    def set_effect(self, effect):
        self.effect = effect
        return self

    def build(self):

        x = CylinderShape.create(self.length, self.radius1, self.radius2, self.subdivisions, self.sides)
        y = CylinderShape.create(self.length, self.radius1, self.radius2, self.subdivisions, self.sides)
        z = CylinderShape.create(self.length, self.radius1, self.radius2, self.subdivisions, self.sides)

        cursor = SceneNode.create('cursor')
        cursor.setPosition(self.position[0], self.position[1], self.position[2])

        cursor.addChild(x)
        cursor.addChild(y)
        cursor.addChild(z)

        half_length = self.length * 0.5

        x.setEffect(self.effect)
        x.translate(Vector3(-half_length, 0, 0), Space.Local)
        x.rotate(Vector3(0, 1, 0), math.radians(90), Space.Parent)

        y.setEffect(self.effect)
        y.translate(Vector3(0, -half_length, 0), Space.Local)
        y.rotate(Vector3(1, 0, 0), math.radians(-90), Space.Parent)

        z.setEffect(self.effect)
        z.translate(Vector3(0, 0, -half_length), Space.Local)

        return cursor
