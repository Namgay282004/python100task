#Do the same task as task 46 but USE FOR LOOP to achieve the same task.

user_number = int(input("Please enter a number: "))

# Initialize the factorial
factorial = 1

# Use a for loop to calculate the factorial
for i in range(1, user_number + 1):
    factorial *= i

# Display the factorial
print("The factorial is: ", factorial)