# Get three user input of three numbers and store that value in an array called “user_inputs”
# Google “array methods in python” to see how to add values to an array 
# Write a function called "is_even" that takes in the user_inputs array as an argument and returns True if all of the numbers are even, False otherwise.

# Get user input
user_inputs = [int(input("Enter a number: ")) for i in range(3)]

# Define the is_even function
def is_even(numbers):
    return all(number % 2 == 0 for number in numbers)

# Call the function and display the output
print(is_even(user_inputs))