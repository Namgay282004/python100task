# Define a variable called "user_name" and get the name from user
# Count the number of vowels occuring in the name
# Display the amount of vowels in the output
# NOTE: USE WHILE LOOP

user_name = input("Please enter your name: ")
vowels = 'aeiou'

# Convert the user_name to lowercase
user_name = user_name.lower()

# Initialize the counter
i = 0
vowel_count = 0
while i < len(user_name):
    if user_name[i] in vowels:
        vowel_count += 1
    i += 1

# Display the amount of vowels
print(vowel_count)
