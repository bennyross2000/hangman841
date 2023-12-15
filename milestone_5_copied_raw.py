import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word.lower()))  
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i in range(len(self.word)):
                if self.word[i].lower() == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Wrong guess! {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        print(f"Updated Word Guessed: {' '.join(self.word_guessed)}")
        
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

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while game.num_lives > 0 and '_' in game.word_guessed:
        game.ask_for_input()

    
    if '_' not in game.word_guessed:
        print("Congratulations. You won the game!")
    else:
        print(f"You lost! The word was: {game.word}")

hangman_game = Hangman(["mango", "watermelon", "guava", "plum", "pear"])
print(f"Chosen word: {hangman_game.word}")
print(f"Word Guessed: {hangman_game.word_guessed}")
print(f"Number of Lives: {hangman_game.num_lives}")
print(f"Number of Unique Letters: {hangman_game.num_letters}")
print(f"List of Guesses: {hangman_game.list_of_guesses}")

play_game(["mango", "watermelon", "guava", "plum", "pear"])        
