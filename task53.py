#Do the same task as task 52 but USE FOR LOOP to achieve the same task.

num = int(input('enter any number: '))

# Start a for loop from 1 to 21
for i in range(1, 21):
    # Calculate the product of num and i
    product = num * i
    # Print the product
    print(f"{num} x {i} = {product}")