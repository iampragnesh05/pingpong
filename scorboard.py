from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        """Clears the previous score and displays the updated one."""
        self.clear()
        self.write(f"{self.left_score}  |  {self.right_score}", align="center", font=("Courier", 24, "normal"))

    def increase_left_score(self):
        """Increases the left player's score and updates the scoreboard."""
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        """Increases the right player's score and updates the scoreboard."""
        self.right_score += 1
        self.update_score()
