FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setpos(-280, 260)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)