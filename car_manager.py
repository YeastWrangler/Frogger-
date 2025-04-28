COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
from turtle import Turtle
import random

class CarManager:


    def __init__(self):
        self.cars = []
        self.level = 1

    def generate_car(self):
        ycor = random.randint(-240,240)
        car = Turtle()
        car.penup()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=random.randint(2,3))
        car.setpos(300,ycor)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            self.move(car)
    def move(self, car):
        car.setposition(car.xcor() - MOVE_INCREMENT - self.level,car.ycor())