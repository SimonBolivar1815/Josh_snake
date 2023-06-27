from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape('square')
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()


    def update_score(self):
        self.write(f"Score: {str(self.score)}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def refreshScore(self):
        self.clear()
        self.score += 1
        self.update_score()