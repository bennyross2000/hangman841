import random

def check_guess(guess, secret_word):
    guess = guess.lower()
    if guess in secret_word.lower():
        print(f"Good guess! '{guess}' is in the word.")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False

def ask_for_input():
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
        return guess
    else:
        print("Oops! That is not a valid input. Please, enter a single alphabetical character.")
        return None

word_list = ["Mango", "Watermelon", "Guava", "Plum", "Pear"]

while True:
    guess = ask_for_input()

    if guess is not None:
        secret_word = random.choice(word_list)
        if check_guess(guess, secret_word):
            break
