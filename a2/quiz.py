import random

#Define Variables
question_List = []

content_Dictionary = {"Golf balls have between 300mand 500 dimples.":True, "Scotland's national animal is a Unicorn": True, "Lightning never strikes twice": False, "The sun is not a star": False, "In the english language, no word rhymes with orange.": True, "There are five different types of blood.": False, "The metric system was invented in France.": True,"Light is faster than sound.": True ,"A spider has six legs.": False, "Uranus spins on its side.": True}

current_question = 0

wrong_answers = 0

global answer

global cq


#Create Classes
class Question:
    def __init__(self, content, bool):
        self.content = content
        self.bool = bool

    def __str__(self) -> str:
        return f"{self.content} T/F = {self.bool}"

#Fill question list
for key, value in content_Dictionary.items():
    question = Question(key, value)
    question_List.append(question)

#Define Functions
def display_question():
    global current_question
    if current_question == 0:
        print(cq)
        current_question = current_question + 1
        global answer
        answer = input("True or False?").lower()
    else:
        print(cq)
        print(f"                                        {score}/{current_question}")
        current_question = current_question + 1
        answer = input("True or False?").lower()
    correct()


def correct():
    if valid_answer() == True:
        if cq.bool == True:
            if answer == "true" or answer == "t":
                print("Correct!")
        elif cq.bool == False:
            if answer == "false" or answer == "f":
                print("Correct")
        else:
            print("Wrong!")
            global wrong_answers
            wrong_answers = wrong_answers + 1
    else:
        print("Input True, T, False, or F next time. You automatically fail this question.")
        wrong_answers = wrong_answers + 1

def valid_answer():
    if answer == "true" or answer == "t" or answer == "false" or answer == "f":
        return True
    else:
        return False


def end():
    if score == 0:
        print("You didn't get any right!")
        quit()

    print(f"You got a score of {score + 1}/{current_question}!")
    if score == 10:
        print("Perfect!")
    elif score > 5:
        print("Good Job!")
    else:
        print("Better luck next time!")

#Program
print("Welcome to my quiz!")
print("Each question is either true or false.")
print("Get the best score you can.")

random.shuffle(question_List)

for i in range(0,10):
    cq = question_List[current_question]
    score = current_question - wrong_answers
    display_question()

end()
