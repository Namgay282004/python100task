#Do the same task as task 44 but USE FOR LOOP to achieve the same task.

user_name = input("Please enter your name: ")
vowels = 'aeiou'

# Convert the user_name to lowercase
user_name = user_name.lower()

# Initialize the counter
vowel_count = 0
for x in user_name:
    if x in vowels:
        vowel_count += 1

# Display the amount of vowels
print(vowel_count)