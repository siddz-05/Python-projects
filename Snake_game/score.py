from turtle import Turtle


ALIGN="center"
FONT=("Arial", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=self.high_score()
        self.game_speed=0.3
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.scoreboard()

    def high_score(self):
        try:
            with open("Snake_game\highscore.txt") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def scoreboard(self):
        self.write(f"SCORE :{self.score} HIGHSCORE:{self.highscore}",align=ALIGN,font=FONT)
    
    def game_score(self):
        self.score+=1
        if self.score>self.highscore:
            self.highscore=self.score
            with open("Snake_game\highscore.txt","w") as file:
                file.write(str(self.score))

        if self.score==9:
            self.game_speed-=0.1
        elif self.score==19:
            self.game_speed-=0.1
        elif self.score==29:
            self.game_speed-=0.1
        self.clear()
        self.scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGN,font=FONT)
        self.goto(0,-25)
        self.write(f"SCORE:{self.score}",align=ALIGN,font=FONT)
    
    