def read_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if value <= 0:
            print("Value must be greater than 0.")
            continue
        return value


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
