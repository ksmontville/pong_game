from random import randint, choice
from turtle import Turtle


class Ball(Turtle):
    """A class to manage the ball in Pong."""
    def __init__(self):
        """Initialise the attributes of the ball."""
        super().__init__()
        self.screen = self.getscreen()
        self.penup()
        self.shape('circle')
        self.color('light blue')
        self.shapesize(stretch_wid=0.80, stretch_len=0.80)
        self.ball_speed = 5
        self.serve_ball()

    def serve_ball(self):
        """Places the ball at the bottom of the table and serves it at a semi-random heading."""
        self.setheading(choice([15, 30, 45, 135, 150, 165]))
        self.setpos(0, -280)

    def bounce(self, heading_adjust, deviation_amount):
        """Reflects the ball and add a small, random deviation to ball bounces for realism."""
        return self.setheading(self.heading() + heading_adjust + randint(-deviation_amount, deviation_amount))

    def detect_wall(self):
        """Detects collisions with the side walls of the table."""
        if self.ycor() >= 0.48 * self.getscreen().window_height():
            if 0 <= self.heading() <= 90:
                self.bounce(-90, 2)
            elif 90 < self.heading() <= 180:
                self.bounce(90, 2)
        elif self.ycor() <= -0.46 * self.getscreen().window_height():
            if 180 < self.heading() <= 270:
                self.bounce(-90, 2)
            elif 270 < self.heading() < 360:
                self.bounce(90, 2)



