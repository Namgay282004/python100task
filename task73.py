# Write a function called "calculate_hypotenuse" that takes the lengths of two sides of a right triangle as arguments and returns the length of the hypotenuse.
# Write another function called "triangle_info" that takes the lengths of two sides and calls the "calculate_hypotenuse" function to calculate and print the length of the hypotenuse.
# Display the output

# Test the function using:
# triangle_info(4, 5)

import math
def calculate_hypotenuse(s1,s2):
    return math.sqrt(s1**2 + s2**2)
def triangle_info(s1,s2):
    hypotenuse  = calculate_hypotenuse(s1,s2)
    print(f'Hypotenuse: {hypotenuse}')

triangle_info(4,5)