#imports
import turtle
import random

#setup turtle and screen
Tim = turtle
screen = turtle.Screen()

Tim.hideturtle()
Tim.speed(0)

screen.setup(500, 500, -700, 100)

screen.colormode(255)

y_counter = -200

#Setup functions


def change_color():
    global R
    global G
    global B
    R = random.randint(0,255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

def draw_dots():
    for i in range(5):
        change_color()
        Tim.down()
        Tim.dot(50, R,G,B)
        Tim.up()
        Tim.fd(100)

def draw():
    for i in range(0, 5):
        global y_counter
        Tim.up()
        Tim.teleport(-200, y_counter)
        draw_dots()
        y_counter = y_counter + 100
    Tim.teleport(-200, -200)
    y_counter = -200

def draw_infinite():
    while True:
        draw()

#Program
screen.onkeyrelease(draw, "d")
screen.onkeyrelease(draw_infinite, "s")
screen.listen()

screen.exitonclick()
