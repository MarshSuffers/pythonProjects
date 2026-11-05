import random

#Setting Global Variables

character_list = []

guess_list = []

word_bank = ["test", "testing", "hangman"]

word = random.choice(word_bank)

lives_left = 6

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
def is_guess_new():
    pass

def is_guess_correct():
    pass

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

