from turtle import Turtle, Screen
import turtle
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.speed(0)
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r, g, b)

timmy.goto(-620, 520)
timmy.dot(20, random_color())
print(turtle.screensize())
def fill_row():
    for _ in range(32):
        timmy.forward(38)
        timmy.dot(20, random_color())
def turn_right():
    timmy.right(90)
    timmy.forward(40)
    timmy.dot(20, random_color())
    timmy.right(90)
def turn_left():
    timmy.left(90)
    timmy.forward(40)
    timmy.dot(20, random_color())
    timmy.left(90)

for _ in range(13):
    fill_row()
    turn_right()
    fill_row()
    turn_left()

screen = Screen()
screen.exitonclick()