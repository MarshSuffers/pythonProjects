import random

word_bank = ["test", "testing", "hangman"]

word = random.choice(word_bank)

characters = list(word)

new_guess = True

previous_guesses = ["a","b"]

current_guess = input("Guess a letter:")

def isGuessNew():
    for i in previous_guesses:
        global new_guess
        if i == current_guess:
            print("You've already tried that letter.")
            new_guess = False
            break
        else:
            previous_guesses.append(current_guess)
            new_guess = True
    print(new_guess)
    print(previous_guesses)

isGuessNew()
