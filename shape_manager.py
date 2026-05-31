import json
from log import create_log
from circle import Circle
from rectangle import Rectangle
from square import Square


logger = create_log("shape.log")

JSON_FILE = "shapes.json"


def shape_to_json(shape):
    return json.dumps(shape.to_dict())


def json_to_shape(json_str):
    data = json.loads(json_str)

    shape_type = data.get("type")
    shape_id = data.get("id")

    if shape_type == "circle":
        return Circle(shape_id, data["radius"])
    elif shape_type == "rectangle":
        return Rectangle(shape_id, data["width"], data["height"])
    elif shape_type == "square":
        return Square(shape_id, data["side"])
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")


def json_to_shapes_list(json_str):
    shapes_data = json.loads(json_str)
    return [json_to_shape(json.dumps(item)) for item in shapes_data]


class Shape_manager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()
        logger.info("ShapeManager initialized")

    def _find_index(self, shape_id):
        for i, shape in enumerate(self.shapes):
            if shape.id == shape_id:
                return i
        return -1

    def create_id(self):
        if not self.shapes:
            return 1
        return max(shape.id for shape in self.shapes) + 1

    def create_shape(self, shape):
        existing = self._find_index(shape.id)
        if existing != -1:
            logger.warning(f"Shape with id {shape.id} already exists, overwriting")
            self.shapes[existing] = shape
        else:
            self.shapes.append(shape)
        self.save_to_json()
        logger.info(f"Created shape {shape.shape_type} with id {shape.id}")

    def get_all_shapes(self):
        logger.info(f"Retrieved {len(self.shapes)} shapes")
        return list(self.shapes)

    def get_shape(self, shape_id):
        index = self._find_index(shape_id)
        if index == -1:
            return None
        return self.shapes[index]

    def update_shape(self, shape_id, new_data):
        index = self._find_index(shape_id)
        if index == -1:
            logger.warning(f"Shape with id {shape_id} not found for update")
            return False
        self.shapes[index] = new_data
        self.save_to_json()
        logger.info(f"Updated shape with id {shape_id}")
        return True

    def delete_shape(self, shape_id):
        index = self._find_index(shape_id)
        if index == -1:
            logger.warning(f"Shape with id {shape_id} not found for delete")
            return False
        del self.shapes[index]
        self.save_to_json()
        logger.info(f"Deleted shape with id {shape_id}")
        return True
