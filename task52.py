# Get a number from the user
# Display the multiplication table of that number from 1 till 20
# NOTE: USE WHILE LOOP

num = int(input('enter any number: '))

# Initialize i to 1
i = 1

# Start a while loop from 1 to 20
while i <= 20:
    # Calculate the product of num and i
    product = num * i
    # Print the product
    print(f"{num} x {i} = {product}")
    # Increment i
    i += 1