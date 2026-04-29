# The Challenge: Sudoku Board ValidatorGoal: Determine if a $9 \times 9$ Sudoku board is valid.Rules:Each row, column, and $3 \times 3$ sub-box must contain the digits $1-9$ without repetition.Note: The board can be partially filled (empty cells are represented by ".").What it tests:Nested loops and grid traversal.Mapping and tracking values (using Dictionaries or Sets).Modular arithmetic (to identify the $3 \times 3$ sub-boxes).

#Code practice
import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 20.")

attempts = 5

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("Game Over! The number was", secret_number)