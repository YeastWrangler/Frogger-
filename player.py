from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y=new_y)
    def move_down(self):
        if self.ycor() >= -280:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), y=new_y)

    def move_left(self):
        if self.xcor() >= -280:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() <= 280:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())
