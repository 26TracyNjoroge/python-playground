"""Number Guessing Game"""

import random

secret_number = random.randint(1, 15)
attempts = 0
max_attempts = 5

print("This is a number guessing game. You have to guess a number between 1 and 15!")

while True:
    guess = int(input("Guess a number between 1 and 15: "))
    attempts += 1

    if  guess == secret_number:
        print(f"You have guessed correctly in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

    if attempts == max_attempts and guess != secret_number:
        print(f"Game over! The correct number is {secret_number}.")






    