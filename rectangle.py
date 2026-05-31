from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_id, width, height):
        super().__init__(shape_id, "rectangle")
        self.width = width
        self.height = height
