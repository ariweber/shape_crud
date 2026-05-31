from shape import Shape


class Square(Shape):
    def __init__(self, shape_id, side):
        super().__init__(shape_id, "square")
        self.side = side

    def get_area(self):
        return self.side * self.side
