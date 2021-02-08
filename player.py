from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.level_speed = 0.1

    def move_forward(self):
        self.forward(10)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def increase_level(self):
        self.level_speed *= 0.8


