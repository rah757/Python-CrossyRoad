from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager(Turtle):
    def __init__(self,movementSpeed):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1,2.5)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250,250))
        self.speed = 5
        self.moveCarToLeft(movementSpeed)
    
    def moveCarToLeft(self, movementSpeed):
        self.goto(self.xcor() - movementSpeed, self.ycor())
    

    