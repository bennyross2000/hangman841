import random

word_list = ["Mango", "Watermelon", "Guava", "Plum", "Pear"]


while True:
    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        secret_word = random.choice(word_list)

        if guess.lower() in secret_word.lower():
            print(f"Good guess! '{guess}' is in the word.")
            break
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
    else:
        print("Oops! That is not a valid input. Please, enter a single alphabetical character.")