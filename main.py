import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

while game_is_on:
    time.sleep(player.level_speed)
    screen.update()
    cars.car_generator()
    cars.move_cars()
    score.display_score()
    for c in cars.cars_generated:
        if player.distance(c) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 290:
        score.update_score()
        player.reset_player()
        score.update_level()
        player.increase_level()

screen.exitonclick()

