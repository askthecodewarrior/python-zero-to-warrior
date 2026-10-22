# Your turn: words of your own, and play again
# This is hangman.py from the video.
# TODO 1: add three words of your own to the list in pick_word(), in
#         lowercase, in quotes.
# TODO 2: change the bottom of the file so the game asks
#         "Play again? (y/n) " after each game, and starts a new game
#         when the player types y. A while True loop around main() does
#         it, with a break when the answer isn't y.
import random


# 1. Pick a secret word
def pick_word():
    words = ["python", "loop", "warrior", "dragon", "potion"]
    return random.choice(words)


# 2. Show the word with blanks
def show_word(word, guessed):
    shown = []
    for letter in word:
        if letter in guessed:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


# 3. Ask for one new letter
def get_guess(guessed):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please type one letter.")
        elif guess in guessed:
            print("You already guessed that.")
        else:
            return guess


# 4. Play until you win or run out of lives
def main():
    word = pick_word()
    guessed = set()
    lives = 6
    while lives > 0:
        shown = show_word(word, guessed)
        print(f"{shown}   Lives: {lives}")
        if "_" not in shown:
            print("You win!")
            break
        guess = get_guess(guessed)
        guessed.add(guess)
        if guess not in word:
            lives -= 1
            print("Not in the word.")
    if lives == 0:
        print("Out of lives! The word was", word)


if __name__ == "__main__":
    main()
