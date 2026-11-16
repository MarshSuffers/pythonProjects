#define variables
operators = ["+", "-", "*", "/"]

result = ""

#define functions

def is_float():
    try:
        float(num1)
        float(num2)
    except ValueError:
        print("Put in a *number* for both inputs")
        quit()

def operation():
    if operator == "+":
        print(num1f + num2f) 
    if operator == "-":
        print(num1f - num2f)
    if operator == "*":
        print(num1f * num2f)
    if operator == "/":
        print(num1f / num2f)

    for i in operators:
        if operator == i:
            return True

#program
num1 = input("Put in a number: ")

print(operators)
operator = input("Select an operation: ")

num2 = input("Put in a second number: ")

is_float()
num1f = float(num1)
num2f = float(num2)

if operation() != True:
    print("Pick one of the four operators next time.")


