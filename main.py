from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scorboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game by Pragnesh Shrimal")
screen.tracer(0)

# Paddles
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Ball
ball = Ball(0, 0)

# Scoreboard
scoreboard = Scoreboard()

# Centerline Function
def draw_centerline():
    """Draws a dashed vertical line down the center."""
    line = Turtle()
    line.color("white")
    line.hideturtle()
    line.penup()
    line.goto(0, 300)  # Start at the top center
    line.setheading(270)  # Face downwards
    for _ in range(30):  # Adjust for the desired number of dashes
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)

# Draw the dashed line
draw_centerline()

# Keyboard Binding
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

# Game Loop
game_is_on = True
try:
    while game_is_on:
        screen.update()
        ball.move(right_paddle, left_paddle)

        # Detect Out of Bounds (Right Side)
        if ball.ball.xcor() > 390:
            scoreboard.increase_left_score()  # Left player scores
            ball.reset_position()

        # Detect Out of Bounds (Left Side)
        if ball.ball.xcor() < -390:
            scoreboard.increase_right_score()  # Right player scores
            ball.reset_position()
except Turtle.Terminator:
    print("Game closed.")

screen.bye()
