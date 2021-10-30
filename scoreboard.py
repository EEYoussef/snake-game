from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
FILE = "/Users/minaki/PycharmProjects/snake/data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open(FILE, mode="r") as file:
            high_score = int(file.read())
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()




