# Hangman, practice 2: easy (8 lives) or hard (4 lives)
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


# Ask how many lives the player gets
def get_lives():
    while True:
        level = input("Easy or hard? ").strip().lower()
        if level == "easy":
            return 8
        elif level == "hard":
            return 4
        print("Please type easy or hard.")


# 4. Play until you win or run out of lives
def main():
    word = pick_word()
    guessed = set()
    lives = get_lives()
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
