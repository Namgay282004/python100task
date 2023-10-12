# Define a variable called "user_number" and get the number from user
# Calculate the factorial for the user_number given by the user
# Display the factorial at the end
# NOTE: USE WHILE LOOP

user_number = int(input("Please enter a number: "))

# Initialize the factorial
factorial = 1

# Use a while loop to calculate the factorial
i = 1
while i <= user_number:
    factorial *= i
    i += 1

# Display the factorial
print("The factorial is: ", factorial)