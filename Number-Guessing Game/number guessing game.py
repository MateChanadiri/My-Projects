import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("enter your guess: "))
    attempts += 1

    if guess < number:
        print("your guess is too low")
    elif guess > number:
        print("your guess is too high")
    else:
        print(f"nice! You guessed it in {attempts} attempts")
        break
else:
    print(f"you used all {max_attempts} attempts, The number was {number}")
    