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
