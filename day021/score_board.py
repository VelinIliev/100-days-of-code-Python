from turtle import Turtle

ALIGMENT = 'center'
FONT = ('Arial', 24, 'normal')
POSITION = (0,260)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard (self):
        self.write(f"Score: {self.score}", align = ALIGMENT,  font = FONT )

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGMENT,  font = FONT )


