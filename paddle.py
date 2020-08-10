import pygame


class Paddle(pygame.sprite.Sprite):
    """A class to handle the pong paddle"""

    def __init__(self, pong_game, x):
        """Create the paddle at the given x position"""
        super().__init__()
        
        # Screen attributes
        self.screen = pong_game.screen
        self.screen_rect = self.screen.get_rect()

        # Paddle settings
        self.settings = pong_game.settings
        self.color = self.settings.paddle_color
        self.speed = self.settings.paddle_speed

        # Create the rect at (0, 0) 
        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        self.rect.x = x
        
        # Set the paddle to the starting position
        self.reset()

        # Start without motion (-1 indicates upwards motion, 1 indicates downwards motion, 0 is no motion)
        self.moving = 0

    def reset(self):
        """Reset the paddle"""
        self.rect.centery = self.screen_rect.centery

    def update(self):
        """Update the position of the paddles"""
        if self.rect.top >= self.screen_rect.top and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += self.moving * self.settings.paddle_speed

        # Reset the paddle if it has gone too far
        if self.rect.top < self.screen_rect.top:
            self.rect.top = self.screen_rect.top
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def draw_paddle(self):
        """Draw the paddle to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
