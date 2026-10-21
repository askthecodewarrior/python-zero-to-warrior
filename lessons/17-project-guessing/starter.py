# Your turn: say "1 try", not "1 tries"
# This is guess.py from the video. If you get it on the very first guess,
# it prints "You got it in 1 tries!". Change step 3:
# TODO 1: after the loop, use an if: when tries == 1, print "You got it in 1 try!"
# TODO 2: put the f-string print under an else, for every other count.
# To test it, add print(secret) right after the randint line for a moment, type that number
# as your first guess, then take the print back out.
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
print(f"You got it in {tries} tries!")
