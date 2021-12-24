import turtle as t
import random

screen = t.Screen()
screen.setup(width = 500, height = 400)
color = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -100
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = t.Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    y_position += 30
    new_turtle.goto(-230, y_position)
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color:")
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on: 

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else: 
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()