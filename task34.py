#Define a variable called "temperature" and get its value from user input.
#Check if the temperature is greater than or equal to 100, display "Boiling".
#If the temperature is between 32 and 99 (inclusive), display "Liquid".
#If the temperature is less than 32, display "Freezing".

temperature = int(input("Enter the temperature: "))

if temperature >= 100:
    print("Boiling")
elif temperature >= 32:
    print("Liquid")
else:
    print("Freezing")