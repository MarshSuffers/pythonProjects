import random

#declare variables
guess_list = []

turn = 0

difficulty = 0

number = random.randint(1, 100)

#declare functions
def too_high():
    if number < guess_int:
        print("Too high!")

def too_low():
    if number > guess_int:
        print("Too low!")

def win():
    if number == guess_int:
        print("You win!")
        print(f"You took {turn} turns, and guessed these - {guess_list} - guesses!")
        quit()

def guess_number():
    try:
        int(guess)
        return True
    except ValueError:
        return False

def guess_illegal():
    if guess_int > 100 or guess_int < 1:
        return True

#program
print("Welcome to 'Guess the Number!' You have to guess the number I'm thinking of before you run out of time.")

diff = input("Easy or Hard mode?")
diff = diff.lower()

if diff == "easy":
    difficulty = 10
    print("You chose easy, so you get 10 turns!")
elif diff == "hard":
    difficulty = 5
    print("You chose hard, so you get 5 turns!")
else:
    print("Pick 'Easy', or 'Hard'!")

while turn < difficulty:
    guess = input("Guess a number between 1 and 100:")
    if guess_number() == True:
        guess_int = int(guess)
        if guess_illegal() != True:
            too_high()
            too_low()
            win()
            turn = turn + 1
            guess_list.append(guess)
        else:
            print("Pick a legal number!")
    else:
        print("Type an integer!")

print("You lose!")
print(f"The number was {number}, and you guessed {guess_list}.")
