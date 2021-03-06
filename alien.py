import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        super().__init__()
        self.game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen
        self.rect.x = ai_game.settings.scr_sz[0] - 2 * self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        return True if (
            self.rect.top >= self.game.settings.scr_sz[1] - self.rect.height
            or self.rect.bottom <= self.rect.height) else False

    def update(self):
        """Move the alien to the top."""
        self.y -= (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.y = self.y
