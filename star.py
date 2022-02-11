import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):


    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.star_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.random_x = randint(0, self.settings.screen_width)
        

        self.rect = pygame.Rect(self.random_x, -140, self.settings.star_width, self.settings.star_height)
        # self.screen_rect = self.screen.get_rect()
        # self.rect.center  = self.screen_rect.center

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y += self.settings.star_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_star(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)