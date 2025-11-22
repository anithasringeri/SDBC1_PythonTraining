# Create a number guessing game. 
# The program should pick a random number between 1 and 100 and the user has to guess it.
# The program should provide "Too high" or "Too low" hints. 
# Use a while loop that terminates when the user guesses correctly.

import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break  # Exit the loop when guessed correctly

