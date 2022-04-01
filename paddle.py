from turtle import Turtle


class Paddle(Turtle):
    """A class to manage the paddle in Pong game."""
    def __init__(self, position_tuple):
        """Initialize the attributes of the paddle. Include a starting position (tuple) at instantiation."""
        super().__init__()
        self.shape('square')
        self.color('pink')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position_tuple)

    def move_up(self):
        """Moves the paddle up the screen."""
        if self.ycor() <= 0.40 * self.getscreen().window_height():
            self.sety(self.ycor() + 50)

    def move_down(self):
        """Moves the paddle down the screen."""
        if self.ycor() >= -0.40 * self.getscreen().window_height():
            self.sety(self.ycor() - 50)



