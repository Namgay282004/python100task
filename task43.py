#Do the same task as task 42 but USE FOR LOOP to achieve the same task

user_name = input("Please enter your name: ")
vowels = 'aeiou'

# Convert the user_name to lowercase
user_name = user_name.lower()

# Use a for loop to check each character
for char in user_name:
    if char in vowels:
        print(True)
        break
else:
    print(False)