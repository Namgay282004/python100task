#Do the same task as task 48 but USE FOR LOOP to achieve the same task.

# Import the random module
import random

# Generate a secret number between 1 and 100
secret_number = random.randint(1, 100)

# Use a for loop to keep asking for guesses until the user guesses the correct number
for i in range(100):  # Limit the number of attempts to 100
    # Ask the user for a guess
    user_guess = int(input("Guess a number between 1 and 100: "))
    
    # Provide feedback
    if user_guess < secret_number:
        print("Too low!")
    elif user_guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the secret number.")
        break  # Exit the loop if the guess is correct