import turtle

class Paddle:
    def __init__(self, x, y):
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)

    def up(self):
        new_y = self.paddle.ycor() + 20
        if new_y < 250:  # Prevent paddle from going out of bounds
            self.paddle.sety(new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        if new_y > -250:  # Prevent paddle from going out of bounds
            self.paddle.sety(new_y)
