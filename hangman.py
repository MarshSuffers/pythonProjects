import random

#Setting Global Variables

character_list = []

guess_list = []

word_bank = ["test", "testing", "hangman"]

unacceptable_guesses = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "~", "!", "@", "#", "$" "%", "^", "&", "*", "(", ")" "-", "_", "=", "+", ":", ";" "'", ",", "<", ".", ">", "?"]

word = random.choice(word_bank)

lives_left = 6

correct = false

turn = 0

#Creating Classes

class Character:
    def __init__(self, display, position, char):
        self.display = display
        self.position = position
        self.char = char

    def __str__(self) -> str:
        return f"{self.char} is in position {self.position}, and display is set to {self.display}."

#Filling Character List

for i in list(word):
    dis = False
    pos = list(word).index(i)
    ch = i
    character = Character(dis, pos, ch)
    character_list.append(character)

for i in character_list:
    print(i)

#Creating Functions
def is_guess_acceptable():
    if len(guess) > 1:
        print("Guess a *letter*")
    else:
        for i in unacceptable_guesses:
            if guess == i:
                print("Guess a *letter*")
                break
            else:
                for i in guess_list:
                    if guess == i:
                        print("You've already guessed that letter!")
                    else:
                        guess_list.append(guess)
                        return True


def is_guess_correct():
    correct = False
    global lives_left
    for i in character_list:
        if guess == i:
            i.display = True
            correct = True
        else:
            lives_left = lives_left - 1

def display_word():
    for i in character_list:
        if i.display == True :
            print(i.char)
        else:
            print("_", end=(""))

#Starting Game
print("HANGMAN")
print("")

display_word()

guess = input(" Guess a letter:")

#testing area
is_guess_acceptable()
