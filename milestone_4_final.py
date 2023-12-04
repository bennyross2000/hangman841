import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Step 3: Initialize attributes
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word.lower()))  # Count of unique letters in the word
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Correcting word_guessed containing guessed letter
            for i in range(len(self.word)):
                if self.word[i].lower() == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Wrong guess! {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                break
        self.check_guess(guess)
        self.list_of_guesses.append(guess)

# Example usage:
hangman_game = Hangman(["mango", "watermelon", "guava", "plum", "pear"])
print(f"Chosen word: {hangman_game.word}")
print(f"Word Guessed: {hangman_game.word_guessed}")
print(f"Number of Lives: {hangman_game.num_lives}")
print(f"Number of Unique Letters: {hangman_game.num_letters}")
print(f"List of Guesses: {hangman_game.list_of_guesses}")

hangman_game.ask_for_input()
print(f"Updated Word Guessed: {hangman_game.word_guessed}")
print(f"Number of Lives remaining: {hangman_game.num_lives}")
print(f"List of Guesses: {hangman_game.list_of_guesses}")
