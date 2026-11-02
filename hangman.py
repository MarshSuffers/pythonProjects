import random

word_bank = ["test", "testing", "hangman"]

word = random.choice(word_bank)

characters = list(word)

previous_guesses = []

current_guess = input("Guess a letter:")

for i in characters:
    for i in previous_guesses:
        if i == current_guess:
            print("You've already tried that letter")
        else:
            previous_guesses.append(current_guess)
