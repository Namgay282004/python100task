# Get user input of a number and store that value in a variable called “user_input” 
# Write a function called "is_even" that takes an integer as an argument and returns True if it's even, False otherwise.
# Call the function and display the output for is_even(6)

# Get user input
user_input = int(input("Enter a number: "))

# Define the is_even function
def is_even(number):
    return number % 2 == 0

# Call the function and display the output
print(is_even(6))  # This will print: True

