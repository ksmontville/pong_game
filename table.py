from turtle import Turtle, Screen

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
BG_COLOR = 'black'


class Table:
    """A class to manage to table (screen) in Pong."""
    def __init__(self):
        """Initialize the attributes of the table."""
        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.tracer(0)
        self.screen.title("Pong!")
        self.draw_net()
        self.draw_boundary()

    def draw_net(self):
        """Draws the turtle objects representing the net of the Pong table."""
        for i in range(1, int(SCREEN_HEIGHT / 50)):
            net = Turtle(shape='square')
            net.penup()
            net.color('light yellow')
            net.shapesize(stretch_wid=1.5, stretch_len=0.3)
            net.setpos(0, 0.5 * self.screen.window_height() - 50 * i)

    def draw_boundary(self):
        """Draws the boundaries of the table."""
        boundary = Turtle('square')
        boundary.color('light yellow')
        boundary.pensize(10)
        boundary.penup()
        boundary.setpos(-0.50 * self.screen.window_width(), 0.49 * self.screen.window_height())
        boundary.pendown()
        boundary.forward(SCREEN_WIDTH)
        boundary.penup()
        boundary.setpos(-0.50 * self.screen.window_width(), -0.48 * self.screen.window_height())
        boundary.pendown()
        boundary.forward(SCREEN_WIDTH)
