from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed(0)
        self.spawn_food()
    
    def spawn_food(self):
        x=random.randrange(-280,281,20)
        y=random.randrange(-280,261,20)
        self.goto(x,y)
