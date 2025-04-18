# Gets user input for the shape type
def get_shape():
    return input("Enter shape (rectangle/square): ").lower()

# Gets dimensions for a rectangle
def get_rectangle_dimensions():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    return length, width

# Gets the dimension for a square
def get_square_dimension():
    side = float(input("Enter side length: "))
    return side

# Calculates the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Calculates the area of a square
def calculate_square_area(side):
    return side * side

# Main function that brings all the parts together
def main():
    shape = get_shape()

    if shape == "rectangle":
        length, width = get_rectangle_dimensions()
        area = calculate_rectangle_area(length, width)
        print("Area of rectangle:", area)
    elif shape == "square":
        side = get_square_dimension()
        area = calculate_square_area(side)
        print("Area of square:", area)
    else:
        print("Invalid shape.")

# Run the program
main()
