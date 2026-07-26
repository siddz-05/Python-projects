from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

game_screen=Screen()
game_screen.setup(600,600)
game_screen.bgcolor("black")
game_screen.title("SNAKE GAME")
game_screen.tracer(0)
  
snake=Snake()
food=Food()
score=Scoreboard()

game_screen.listen() 
game_screen.onkey(snake.up,"Up")
game_screen.onkey(snake.down,"Down")
game_screen.onkey(snake.right,"Right")
game_screen.onkey(snake.left,"Left")

game_is_on=True

while game_is_on:
    game_screen.update()
    time.sleep(score.game_speed)
    snake.move()
            
    if snake.head.distance(food)<20:
        food.spawn_food()
        score.game_score()
        snake.extend()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>280 or snake.head.ycor()<-290:
        score.game_over()
        game_is_on=False

    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            score.game_over()
            game_is_on=False
    
game_screen.exitonclick()
   