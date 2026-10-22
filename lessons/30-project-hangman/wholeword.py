# Hangman, practice 3: guess the whole word at once
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


# 3. Ask for one new letter, or the whole word
def get_guess(guessed, word):
    while True:
        guess = input("Guess a letter or the word: ").strip().lower()
        if guess == word:
            return guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please type one letter, or the whole word.")
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
        guess = get_guess(guessed, word)
        if guess == word:
            print(f"{' '.join(word)}   Lives: {lives}")
            print("You win!")
            break
        guessed.add(guess)
        if guess not in word:
            lives -= 1
            print("Not in the word.")
    if lives == 0:
        print("Out of lives! The word was", word)


if __name__ == "__main__":
    main()
