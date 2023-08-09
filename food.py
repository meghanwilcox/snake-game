from turtle import Turtle, Screen
from random import randint


class Food(Turtle):

    # defines a food object
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("white")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.hideturtle()
        self.goto(randint(-280, 280), randint(-280, 280))
        self.showturtle()
