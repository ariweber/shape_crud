from shape_manager import Shape_manager
from circle import Circle
from rectangle import Rectangle
from square import Square
from helpers import read_positive_float, read_int


def create_shape_menu(manager):
    print("\nShape types:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    choice = input("Choose shape type: ")

    shape_id = manager.create_id()

    if choice == "1":
        radius = read_positive_float("Enter radius: ")
        shape = Circle(shape_id, radius)
    elif choice == "2":
        width = read_positive_float("Enter width: ")
        height = read_positive_float("Enter height: ")
        shape = Rectangle(shape_id, width, height)
    elif choice == "3":
        side = read_positive_float("Enter side: ")
        shape = Square(shape_id, side)
    else:
        print("Invalid choice.")
        return

    manager.create_shape(shape)
    print(f"Created: {shape}")
