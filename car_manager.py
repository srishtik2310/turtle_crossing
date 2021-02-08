from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_generated = []

    def car_generator(self):
        a = random.randint(0, 6)
        if a == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.pen()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(x = 300, y = random.randint(-250 ,250))
            self.cars_generated.append(new_car)

    def move_cars(self):
        for cars in self.cars_generated:
            cars.forward(STARTING_MOVE_DISTANCE)



