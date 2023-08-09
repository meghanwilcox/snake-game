from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
            file.close()
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.pendown()
        self.pencolor("white")
        self.write("Score: 0  High Score: 0", False, "center",
                   font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score = self.score + 1

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.pendown()
        self.pencolor("white")
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, "center",
                   font=('Arial', 20, 'normal'))

    def reset_scoreboard(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.pendown()
        self.pencolor("white")
        self.write(f"Score: 0  High Score: {self.high_score}", False, "center",
                   font=('Arial', 20, 'normal'))
        self.score = 0

    # def game_over(self):
    #     self.hideturtle()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, "center", font=('Arial', 20, 'normal'))

