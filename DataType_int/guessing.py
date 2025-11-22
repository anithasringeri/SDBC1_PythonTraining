#Numeric Data Types
# exe5: Guessing game
#Objective: Use while with integers for a simple guessing game.
#Outcome: Prints “Correct!” when the guess matches.

secret = 0
guess = 0
while guess != secret:
    guess+=1
    print("Guessing: ",guess)
else:
    print("Correct! the sceret number is :", secret)
