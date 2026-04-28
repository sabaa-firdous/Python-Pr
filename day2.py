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