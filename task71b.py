# Write a function called "calculate_area" that takes the length and width of a rectangle as arguments and returns its area.
# Write another function called "calculate_perimeter" that takes the same inputs and returns the perimeter of the rectangle.
# Then, write a third function called "rectangle_info" that calls the first two functions and prints both the area and perimeter of the rectangle.

# Test the function using:
# rectangle_info(4, 5)

def calculate_area(length,width):
    return length*width

def calculate_perimeter(length,width):
    return 2 *(length+width)

def rectangle_info(length, width):
    area = calculate_area(length,width)
    perimeter = calculate_perimeter(length,width)
    print(f'Area: {area}')
    print(f'Perimeter: {perimeter}')

rectangle_info(4,5)
