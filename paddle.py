from turtle import Turtle
from ball import Ball


class Paddle(Turtle):

    def __init__(self, position, ball):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.ball = ball

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    def ai(self):
        new_y = self.ball.ycor()
        self.goto(self.xcor(), new_y)

