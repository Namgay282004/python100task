#Do the same task as task 50 but USE FOR LOOP to achieve the same task.

# Get user inputs for num1 and num2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize sum to 0
sum = 0

# Start a for loop from num1 to num2
for i in range(num1, num2 + 1):
    # Add i to sum
    sum += i

# Print the final sum
print("The sum of all numbers between", num1, "and", num2, "is", sum)