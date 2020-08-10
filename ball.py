import random
import math
from time import sleep

import pygame


class Ball(pygame.sprite.Sprite):
    """A class to handle the pong ball"""

    def __init__(self, pong_game):
        """Create the ball and initialize static settings"""
        super().__init__()
        self.pong_game = pong_game
        self.screen = pong_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pong_game.settings
        self.color = self.settings.ball_color

        # Create a ball rect at (0, 0) 
        self.rect = pygame.Rect(0, 0, self.settings.ball_width, self.settings.ball_height)
        
        # Set the ball for the starting position
        self.reset()

    def reset(self):
        """Reset the ball's dynamic attributes"""
        # Center the ball
        self.rect.center = self.screen_rect.center

        # Store the ball's x and y positions as decimals
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Randomly initialize the ball's angle in radians
        self.angle = self.angle = math.radians(random.randint(0, 359))

        # Reset the speed
        self.speed = self.settings.ball_speed

    def _touching_sides(self):
        """Return True if ball is touching right or left edges of screen"""
        return self.touching_right() or self.touching_left()

    def touching_right(self):
        """Return True if the ball is touching the right side"""
        return self.rect.right >= self.screen_rect.right

    def touching_left(self):
        """Return True if the ball is touching the left side"""
        return self.rect.left <= self.screen_rect.left
    
    def _touching_top_bottom(self):
        """Return True if ball is touching top or bottom edges of screen"""
        return self.rect.top <= self.screen_rect.top or \
                self.rect.bottom >= self.screen_rect.bottom

    def update(self):
        """Update the x and y positions of the ball"""
        # Check for bounces
        if self._touching_sides():
            self.pong_game.reset_round()
        if self._touching_top_bottom():
            self.angle *= -1
        if pygame.sprite.spritecollideany(self, self.pong_game.paddles):
            self.angle = math.pi - self.angle
            # Vary the angle by plus or minus 15 degrees in either direction
            self.angle += random.random() * random.choice([-1, 1]) * math.pi / 12
            # Speed up the game
            self.speed *= 1.1

        # Change the float x and y positions
        self.x += math.cos(self.angle) * self.speed
        self.y -= math.sin(self.angle) * self.speed

        # Update the rect position
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_ball(self):
        """Draw the ball to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

