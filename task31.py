#Define a variable called age and get it’s value from user input()
#Remember: the input() function returns a string, you need to convert it to an int
#Check if the age is above 18.
#If the age is above 18 (inclusive), display the output as: “You can drink”
#If the age is below 18, display the output as “Please grow older”

age = int(input("Your age: "))

if age > 18:
    print("You can drink")
else:
    print("Please grow older")