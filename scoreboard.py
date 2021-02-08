from turtle import Turtle
FONT = ("Courier", 24, "normal")
GAME_END_FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.display_score()
        self.update_level()

    def display_score(self):
        self.goto(x= 210, y = 270)
        self.write(arg = f"Score : {self.score}", align = "center", font = FONT)

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write(arg = "GAME OVER !!", align = "center", font = GAME_END_FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def update_level(self):
        self.clear()
        self.goto(x = -210, y = 270)
        self.write(arg=f"Level : {self.score + 1}", align="center", font = FONT)


