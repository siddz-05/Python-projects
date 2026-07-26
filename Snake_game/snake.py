from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0
POSITION=[(0,0),(-20,0),(-40,0)]

class Snake():
    def __init__(self):
        self.segment=[]
        self.starting_segment()
        self.head=self.segment[0]
        
    def starting_segment(self):
        for position in POSITION:
            self.create_snake(position)
    
    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg-1].xcor()
            new_y=self.segment[seg-1].ycor()
            self.segment[seg].goto(new_x,new_y)
        
        self.head.forward(20)
    
    def create_snake(self,position):
        snake=Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.setposition(position)
        self.segment.append(snake)

    def extend(self):
        self.create_snake(self.segment[-1].position())
        
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)