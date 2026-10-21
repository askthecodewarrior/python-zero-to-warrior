# Number guessing game: "1 try", not "1 tries"
import random

# 1. Pick a secret number from 1 to 100
secret = random.randint(1, 100)
print("I'm thinking of a number from 1 to 100.")

# 2. Keep asking until the guess is right
tries = 0
while True:
    guess = int(input("Your guess: "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        break

# 3. Say how many tries it took
if tries == 1:
    print("You got it in 1 try!")
else:
    print(f"You got it in {tries} tries!")
