import sys
from time import sleep

import pygame

from settings import Settings
from ball import Ball
from paddle import Paddle
from game_stats import GameStats
from scoreboard import ScoreBoard


class Pong:
    """A class to handle pong game attributes and methods"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        # Create the screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Pong")

        # Create a ball for the game
        self.ball = Ball(self)

        # Create a statistics tracker and scoreboard
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        # Create the paddles and store them in a group
        self.left_paddle = Paddle(self, 0)
        self.right_paddle = Paddle(self, self.screen_rect.right-self.settings.paddle_width)
        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.left_paddle, self.right_paddle)

    def run(self):
        """Run the game"""
        while True:
            self._check_events()
            self.ball.update()
            self.paddles.update()
            self._update_screen()

    def _check_events(self):
        """Check for keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check for key presses"""
        if event.key == pygame.K_UP:
            self.right_paddle.moving -= 1
        elif event.key == pygame.K_DOWN:
            self.right_paddle.moving += 1
        elif event.key == pygame.K_w:
            self.left_paddle.moving -= 1
        elif event.key == pygame.K_s:
            self.left_paddle.moving += 1
        elif event.key == pygame.K_r:
            self.reset_round()

    def _check_keyup_events(self, event):
        """Check for key releases"""
        if event.key == pygame.K_UP:
            self.right_paddle.moving += 1
        elif event.key == pygame.K_DOWN:
            self.right_paddle.moving -= 1
        elif event.key == pygame.K_w:
            self.left_paddle.moving += 1
        elif event.key == pygame.K_s:
            self.left_paddle.moving -= 1

    def reset_round(self):
        """Reset the ball and paddles for the next round"""
        # Update the score
        if self.ball.touching_right():
            self.stats.left_score += 1
        elif self.ball.touching_left():
            self.stats.right_score += 1

        self.sb.prep_score()

        # Reset the balls and the paddles
        self.ball.reset()
        for paddle in self.paddles.sprites():
            paddle.reset()
        
        # Pause before starting the next round
        sleep(1)

    def _draw_background(self):
        """Draw the background and the middle divider"""
        # Fill the background
        self.screen.fill(self.settings.bg_color)

        # Draw the dividers
        num_ticks = 8
        num_spaces = 2 * num_ticks - 1
        tick_height = self.settings.screen_height / num_spaces
        for y in range(0, num_spaces):
            new_rect = pygame.Rect(0, 0, 6, int(tick_height))
            new_rect.centerx = self.screen_rect.centerx
            new_rect.y = int(y * tick_height * 2)
            pygame.draw.rect(self.screen, self.settings.WHITE, new_rect)


    def _update_screen(self):
        """Draw the current screen"""
        self._draw_background()

        # Draw the scoreboard
        self.sb.draw_score()

        # Draw the ball
        self.ball.draw_ball()

        # Draw the paddles
        for paddle in self.paddles.sprites():
            paddle.draw_paddle()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    pong_game = Pong()
    pong_game.run()
