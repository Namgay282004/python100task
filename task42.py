# Define a variable called "user_name" and get the name from user
# Check if there is a vowel in “user_name”; vowels: ‘a, e, i, o, u”
# If yes display True, else display False
# NOTE: USE WHILE LOOP

user_name = input("Please enter your name: ")
vowels = 'aeiou'

# Convert the user_name to lowercase
user_name = user_name.lower()

# Initialize the counter
i = 0
while i < len(user_name):
    if user_name[i] in vowels:
        print(True)
        break
    i += 1
else:
    print(False)

