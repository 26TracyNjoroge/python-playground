"""Number Gueassing Game"""

import random

secret_number = random.randint(1, 15)
attempts = 0

print("This is a number guessing game. You have to guess a number between 1 and 15!")

while True:
    guess = int(input("Guess a number between 1 and 15: "))
    # attempts += 1

    if  guess == secret_number:
        print("You have guessed correctly!")
        break
    elif    guess < 8:
        print("Too low!")
    elif guess >= 8:
        print("Too high!")



    