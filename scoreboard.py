from turtle import Turtle

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
ALIGN = 'center'
FONT = ('Courier', 40, 'bold')


class Scoreboard(Turtle):
    """A class to manage the scoreboard in Pong game."""
    def __init__(self, x_cor, y_cor):
        """Initialize the attributes of the scoreboard."""
        super().__init__()
        self.x = x_cor
        self.y = y_cor
        self.color('light green')
        self.penup()
        self.hideturtle()
        self.setpos(x_cor, y_cor)
        self.score = 0
        self.show_score()

    def show_score(self):
        """Displays the score on screen."""
        self.write(f'{self.score}', align=ALIGN, font=FONT)

    def increment_score(self):
        """Clears the current score, then increments scoreboard by 1."""
        self.clear()
        self.score += 1

