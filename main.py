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


def show_all_shapes(manager):
    shapes = manager.get_all_shapes()
    if not shapes:
        print("\nNo shapes found.")
        return
    print(f"\n--- All Shapes ({len(shapes)}) ---")
    for shape in shapes:
        print(f"  {shape}")


def update_shape_menu(manager):
    show_all_shapes(manager)
    if not manager.shapes:
        return

    shape_id = read_int("\nEnter shape ID to update: ")

    print("New shape type:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    choice = input("Choose shape type: ")

    if choice == "1":
        radius = read_positive_float("Enter new radius: ")
        new_shape = Circle(shape_id, radius)
    elif choice == "2":
        width = read_positive_float("Enter new width: ")
        height = read_positive_float("Enter new height: ")
        new_shape = Rectangle(shape_id, width, height)
    elif choice == "3":
        side = read_positive_float("Enter new side: ")
        new_shape = Square(shape_id, side)
    else:
        print("Invalid choice.")
        return

    if manager.update_shape(shape_id, new_shape):
        print(f"Updated to: {new_shape}")
    else:
        print("Shape not found.")


def delete_shape_menu(manager):
    show_all_shapes(manager)
    if not manager.shapes:
        return

    shape_id = read_int("\nEnter shape ID to delete: ")
    if manager.delete_shape(shape_id):
        print("Shape deleted.")
    else:
        print("Shape not found.")
