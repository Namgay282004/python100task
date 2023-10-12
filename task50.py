#Get two numbers as user inputs from a user
# Store each of them in variable num1 and num2
# Calculate the sum of all numbers between num1 and num2
# Display the final sum as the output
# NOTE: USE WHILE LOOP

# Get user inputs for num1 and num2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize sum to 0
sum = 0

# Start a while loop from num1 to num2
while num1 <= num2:
    # Add num1 to sum
    sum += num1
    # Increment num1
    num1 += 1

# Print the final sum
print("The sum of all numbers between", num1, "and", num2, "is", sum)
