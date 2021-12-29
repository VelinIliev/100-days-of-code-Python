from turtle import Turtle, position

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.positions = [-20, -40, -60, -80, -100, -120, -140, -160, -180, -200, -220, -240, -260, -280, -300, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
        self.hideturtle()
        self.borders = []
        self.add_td_boredr(self.positions, 305)
        self.add_td_boredr(self.positions, -297)
        self.add_lr_border(297, self.positions)
        self.add_lr_border(-305, self.positions)
        
    def add_td_boredr(self, x_pos, y_pos):
        for position in x_pos:
            new_bordrer = Turtle()
            new_bordrer.color("white")
            new_bordrer.shape('square')
            new_bordrer.penup()
            new_bordrer.goto(position, y_pos)
            self.borders.append(new_bordrer)
    
    def add_lr_border(self, x_pos, y_pos):
        for position in y_pos:
            new_bordrer = Turtle()
            new_bordrer.color("white")
            new_bordrer.shape('square')
            new_bordrer.penup()
            new_bordrer.goto(x_pos, position)
            self.borders.append(new_bordrer)
