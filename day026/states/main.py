import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
game_is_on = True
guessed_states = 0
data = pandas.read_csv("./50_states.csv")


def write_state(x, y, state):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(state, align="center", font=("Courrier", 12, "normal"))


guessed_states = []


while game_is_on:
    answer_state = (screen.textinput(title=f"Guess the State {len(guessed_states)}/50", prompt="What's another state name?")).title()
    if answer_state == "Exit":
        game_is_on = False
    if answer_state in data.values:
        x = int(data.x[data.state == answer_state])
        y = int(data.y[data.state == answer_state])
        # print(f'x: {x.iloc[0]}, y: {y.iloc[0]}, state: {check_state}')
        write_state(x, y, answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
    elif len(guessed_states) == 50:
        game_is_on = False
    print(guessed_states)

# missing_states = []

# for state in data.state:
#     if state not in guessed_states:
#         missing_states.append(state)
missing_states = [state for state in data.state if state not in guessed_states]

# print(missing_states)

# data_dict = {
#     "states": missing_states,
# }
states_to_learn = pandas.DataFrame(missing_states)

states_to_learn.to_csv("./states_to_learn.csv")
