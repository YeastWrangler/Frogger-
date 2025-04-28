import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
turtle = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=turtle.move, key="Up")
screen.onkeypress(fun=turtle.move_down, key="Down")
screen.onkeypress(fun=turtle.move_left, key="Left")
screen.onkeypress(fun=turtle.move_right, key="Right")

game_is_on = True
counter = 0
for i in range(1,6):
    car_manager.generate_car()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter == 7:
        car_manager.generate_car()
        counter = 0
    counter += 1
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(turtle) < 18:
            game_is_on = False

    if turtle.ycor() >= 280:
        turtle.setpos(0,-280)
        car_manager.level += 1
        scoreboard.increase_score()

screen.exitonclick()