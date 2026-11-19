#imports
import turtle
import random

#setup turtle and screen
Tim = turtle
screen = turtle.Screen()

Tim.hideturtle()
Tim.speed(0)

screen.setup(700, 700, -700, 100)

screen.colormode(255)

y_counter = -225

#Setup functions


def change_color():
    global R
    global G
    global B
    R = random.randint(0,255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

def draw_dots():
    for i in range(10):
        change_color()
        Tim.down()
        Tim.dot(20, R,G,B)
        Tim.up()
        Tim.fd(50)

def draw():
    for i in range(10):
        global y_counter
        Tim.up()
        Tim.teleport(-225, y_counter)
        draw_dots()
        y_counter = y_counter + 50
    Tim.teleport(-225, -225)
    y_counter = -225

def draw_infinite():
    while True:
        draw()

#Program
screen.onkeyrelease(draw, "d")
screen.onkeyrelease(draw_infinite, "s")
screen.listen()

screen.exitonclick()
