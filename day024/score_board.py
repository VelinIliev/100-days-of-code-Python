from os import close
from turtle import Turtle

ALIGMENT = 'center'
FONT = ('Arial', 24, 'normal')
POSITION = (0,260)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 
        self.high_score = int(self.read_high_score())
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt") as data:
            contents = data.read()
        return contents
        
    def write_high_score(self):
        with open("data.txt", mode = "w") as data:
            data.write(f'{self.high_score}')

    def update_scoreboard (self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGMENT,  font = FONT )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()
    
    
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGMENT,  font = FONT )


