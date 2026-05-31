import json
from log import create_log
from circle import Circle
from rectangle import Rectangle
from square import Square


logger = create_log("shape.log")

JSON_FILE = "shapes.json"


def shape_to_json(shape):
    return json.dumps(shape.to_dict())
