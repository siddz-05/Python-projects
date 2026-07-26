from turtle import Turtle,Screen,colormode
import random

color_list=[(254, 254, 253), (249, 254, 45), (224, 249, 252), (237, 247, 252), (226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96), (113, 174, 215), (244, 227, 95), (173, 20, 41), (233, 79, 51), (224, 126, 156), (118, 184, 130), (11, 172, 207), (165, 151, 25), (13, 58, 148), (83, 37, 23), (128, 37, 27), (37, 129, 78), (42, 192, 160), (14, 39, 92), (129, 238, 190), (244, 162, 151), (235, 162, 181), (100, 101, 186), (127, 214, 239), (66, 77, 38), (74, 31, 46), (20, 93, 54), (160, 175, 234), (254, 238, 0), (26, 65, 48), (251, 7, 38)]
    
art=Turtle()
colormode(255)
art.hideturtle()
art.setheading(225)
art.penup()
art.forward(300)
art.setheading(0)
art.pendown()

art.speed(0)
c=-180
for _ in range(10):
    for _ in range(10):
        art.dot(20,random.choice(color_list))
        art.penup()
        art.forward(50)
        art.pendown()
    # tutty.teleport(-212,y=c)
    # c+=40
    art.setheading(90)
    art.penup()
    art.forward(50)
    art.setheading(180)
    art.forward(500)
    art.setheading(0)
    art.pendown()

screen=Screen()
screen.exitonclick()
