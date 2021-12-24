import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.pensize(15)
timmy.speed(0)
distance = 30
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return r, g, b

directions = [0, 90, 180, 270]

for x in range(200):
    timmy.pencolor(random_color())
    timmy.setheading(random.choice(directions))
    timmy.forward(distance)

screen = Screen()
screen.exitonclick()