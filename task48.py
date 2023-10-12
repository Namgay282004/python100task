# Write a program that asks the user to guess a secret number (e.g., 42).
# The secret is a random number between 1 to 100 inclusive
# Keep asking for guesses until the user guesses the correct number.
# Provide feedback such as "Too high" or "Too low" after each guess.
# NOTE: USE WHILE LOOP

# Import the random module
import random

# Generate a secret number between 1 and 100
secret_number = random.randint(1, 100)

# Use a while loop to keep asking for guesses until the user guesses the correct number
while True:
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