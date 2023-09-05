from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.high_score = int(self.read_data())
        self.refresh_score()
        self.hideturtle()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.write_data(self.score)
        self.score = 0
        self.high_score = int(self.read_data())
        self.refresh_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def write_data(self, data):
        with open("data.txt", mode="w") as f:
            f.write(str(data))

    def read_data(self):
        with open("data.txt", mode="r") as f:
            return f.read()
