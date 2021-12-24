from turtle import Turtle, Screen
import heroes

print(heroes.gen())

timmy = Turtle()
timmy.shape('turtle')
timmy.color("coral")

# timmy.forward(400)
def move_dashed(distance):
    for _ in range(int(distance/20)):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

for _ in range(4):
    move_dashed(300)
    timmy.left(90)

screen = Screen()
screen.exitonclick()