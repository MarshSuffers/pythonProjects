import random

#Setting Global Variables

character_list = []

guess_list = []

word_bank = ["test", "testing", "hangman"]

unacceptable_guesses = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "~", "!", "@", "#", "$" "%", "^", "&", "*", "(", ")" "-", "_", "=", "+", ":", ";" "'", ",", "<", ".", ">", "?"]

word = random.choice(word_bank)

wrong_moves = 0

correct = False

turn = 0

#Creating Classes

class Character:
    def __init__(self, display, char):
        self.display = display
        self.char = char

    def __str__(self) -> str:
        return f"{self.char} display = {self.display}."

#Filling Character List

for i in list(word):
    dis = False
    ch = i
    character = Character(dis, ch)
    character_list.append(character)

#Creating Functions
def is_guess_acceptable():
    for i in unacceptable_guesses:
        if i == guess:
            return False
    for i in guess_list:
        if i == guess:
            return False
    if len(guess) >= 2:
        return False
    guess_list.append(guess)


def is_guess_correct():
    mybool = False
    for i in character_list:
        if guess == i.char:
            i.display = True
            print(i)
            mybool = True
    if mybool == True:
        return True
        

def display_word():
    for i in character_list:
        if i.display == True :
            print(i.char, end="")
        elif i.display == False:
            print("_", end="")

def game_over():
    count = 0
    for i in character_list:
        if i.display == True:
            count = count + 1
    if count == len(word):
        print("You win!")
        print(f"You won in {turn} turns!")
        print(f"You guessed these letters: {guess_list} ")
        return True
    if wrong_moves >= 6:
        print("You lose!")
        print(f"{word} was the word!")
        return True

#Starting Game
print("HANGMAN")
print("")

while game_over() != True:
    display_word()
    guess = input(" Guess a letter: ")
    guess = guess.lower()
    if is_guess_acceptable() != False and is_guess_correct() == True:
        print("Your letter is in the word!")
    elif is_guess_acceptable() == False:
        print("Guess a *single letter* that you *have not guessed before*")
    elif is_guess_correct() != True:
        print("Your letter is not in the word")
        wrong_moves = wrong_moves + 1
    else: print("Guess a *single letter* that you *have not guessed before*")
    turn = turn + 1
    print(f"You've made {wrong_moves} wrong moves. If you make 6, you lose!")
    print(f"Turn: {turn}")
    print(f"Guessed characters: {guess_list}")
    print(len(guess))


