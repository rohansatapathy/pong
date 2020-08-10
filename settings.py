class Settings:
    """A class to hold settings for pong"""

    def __init__(self):
        """Initialize game settings"""

        # Colors
        self.BLACK = (20, 20, 20)
        self.WHITE = (255, 255, 255)

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = self.BLACK

        # Ball settings
        self.ball_width = 20
        self.ball_height = 20
        self.ball_color = self.WHITE
        self.ball_speed = 4

        # Paddle settings
        self.paddle_width = 10
        self.paddle_height = 120
        self.paddle_color = self.WHITE
        self.paddle_speed = 4
 