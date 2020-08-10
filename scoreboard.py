import pygame

class ScoreBoard():
    """A class to hold the pong scoreboard"""

    def __init__(self, pong_game):
        """Create the scoreboard"""
        self.pong_game = pong_game
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = self.pong_game.settings

        # Initialize font settings
        pygame.font.init()
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont("futurattc", 100)
        self.score_spacing = 15

        # Prep the initial score image
        self.prep_score()

    def prep_score(self):
        """Turn the right side score into a rendered image"""
        score = f"{self.pong_game.stats.left_score}   {self.pong_game.stats.right_score}"
        self.score_image = self.font.render(score, True, self.text_color)

        # Score is in the right-center of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = self.screen_rect.midtop

    def draw_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        