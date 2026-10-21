# Number guessing game with 7 tries
import random

secret = random.randint(1, 100)
print("I'm thinking of a number from 1 to 100. You get 7 tries.")

tries = 0
while tries < 7:
    guess = int(input("Your guess: "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"You got it in {tries} tries!")
        break

if guess != secret:
    print("Out of tries! It was", secret)
