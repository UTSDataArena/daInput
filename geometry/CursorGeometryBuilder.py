class CursorGeometryBuilder(object):

    def __init__(self):
        super(CursorGeometryBuilder, self).__init__()

        self.position = (0, 0, 0)

    def set_position(self, x, y, z):
        self.position = (x, y, z)
        return self

    def build(self):
        raise NotImplementedError
