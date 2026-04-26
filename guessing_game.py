import random

while True:
    number = random.randint(1, 100)
    attempt = 0

    print("I'm thinking of a number between 1 and 100!")

    while True:
        guess = int(input("Your guess: "))
        attempt += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"You win! The number was {number}.")
            print(f"You made {attempt} attempt(s).")
            break

    print("Play again? (y/n)")
    if input().lower() != 'y':
        break
