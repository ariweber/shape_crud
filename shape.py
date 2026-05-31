from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape_id, shape_type):
        self.id = shape_id
        self.shape_type = shape_type

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    def __str__(self):
        return f"{self.shape_type} (id={self.id}, area={self.get_area():.2f}, perimeter={self.get_perimeter():.2f})"
