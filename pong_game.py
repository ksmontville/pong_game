import time
from table import Table
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

GAME_SPEED = 0.01
PADDLE_HIT_BUFFER = 30

table = Table()
table.screen.cv._rootwindow.resizable(False, False)
screen_width = table.screen.window_width()
screen_height = table.screen.window_height()

# Set position of scoreboards
r_scoreboard = Scoreboard(0.15 * screen_width, 0.38 * screen_height)
l_scoreboard = Scoreboard(-0.1 * screen_width, 0.38 * screen_height)

# Set position of paddles
r_paddle = Paddle((0.46 * screen_width, 0))
l_paddle = Paddle((-0.47 * screen_width, 0))

# Set ball into motion
ball = Ball()

# Respond to key presses
table.screen.listen()
table.screen.onkey(key='Up', fun=r_paddle.move_up)
table.screen.onkey(key='Down', fun=r_paddle.move_down)
table.screen.onkey(key='w', fun=l_paddle.move_up)
table.screen.onkey(key='s', fun=l_paddle.move_down)


def set_table():
    """
    Resets table components to their starting positions.
    Pause the game for three seconds, then serve the ball.
    """
    r_paddle.setpos(0.46 * screen_width, 0)
    l_paddle.setpos(-0.47 * screen_width, 0)
    ball.setpos(0, -0.47 * screen_height)
    ball.ball_speed = 5
    table.screen.update()
    time.sleep(3)
    ball.serve_ball()


set_table()
game_on = True
while game_on:
    time.sleep(GAME_SPEED)
    table.screen.update()

    ball.forward(ball.ball_speed)
    ball.detect_wall()

    if ball.distance(r_paddle) < PADDLE_HIT_BUFFER and ball.xcor() >= 0.38 * screen_width:
        ball.bounce(180, 5)
        ball.ball_speed += 1

    if ball.distance(l_paddle) < PADDLE_HIT_BUFFER and ball.xcor() <= -0.38 * screen_width:
        ball.bounce(180, 5)
        ball.ball_speed += 1

    if ball.xcor() < -0.55 * screen_width:
        r_scoreboard.increment_score()
        r_scoreboard.show_score()
        set_table()

    if ball.xcor() > 0.55 * screen_width:
        l_scoreboard.increment_score()
        l_scoreboard.show_score()
        set_table()


table.screen.exitonclick()

