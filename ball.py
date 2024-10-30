import turtle
import random

class Ball:
    def __init__(self, x, y):
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(x, y)
        self.ball.shapesize(stretch_wid=1, stretch_len=1)
        self.dx = 0.1 * random.choice([1, -1])
        self.dy = 0.1 * random.choice([1, -1])

    def move(self, right_paddle, left_paddle):
        x = self.ball.xcor()
        y = self.ball.ycor()
        x += self.dx
        y += self.dy

        # Wall collision
        if y > 280 or y < -280:
            self.dy *= -1

        # Paddle collision
        if (340 < x < 350) and self.is_collision(y, right_paddle):
            self.dx *= -1
        elif (-350 < x < -340) and self.is_collision(y, left_paddle):
            self.dx *= -1

        self.ball.goto(x, y)

    def is_collision(self, y, paddle):
        return paddle.paddle.ycor() + 50 > y > paddle.paddle.ycor() - 50

    def reset_position(self):
        """Resets the ball to the center and gives it a random direction."""
        self.ball.goto(0, 0)
        self.dx *= random.choice([1, -1])
        self.dy *= random.choice([1, -1])
