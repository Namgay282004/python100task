# Get three user input of three numbers and store that value in an array called “user_inputs”
# Google “array methods in python” to see how to add values to an array 
# Write a function called "is_even" that takes in the user_inputs array as an argument and displays which numbers are even and which are odd.
# Example: 
# is_even([1,2,5]) will display the output as
# 1 is odd
# 2 is even
# 5 is odd 

# Get user input
user_inputs = [int(input("Enter a number: ")) for _ in range(3)]

# Define the is_even function
def is_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

# Call the function
is_even(user_inputs)
