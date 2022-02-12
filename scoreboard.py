import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    def __init__(self, game):
        """Initialize scorekeeping attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect =  self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font settings for scoring information.
        # Text color is equal to Ship color
        self.text_color = (247, 225, 207) # Ship color
        # self.high_score_text_color = (255, 130, 49) # Invador color
        # self.high_score_text_color = self.settings.bullet_color
        self.high_score_text_color  = self.text_color
        self.font = pygame.font.Font('fonts/PixelTactical-AWOx.ttf', 40)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 21
        self.score_rect.top = 14

    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "HIGH: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.high_score_text_color)

        # Center the high score at the top of the screen.
        self.high_score_rect  = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            
    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level) + ' lvl'
        self.level_image = self.font.render(level_str, True, self.text_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 0 # Zero interval

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 21 + ship_number * (ship.rect.width + 7)
            ship.rect.y = 21
            self.ships.add(ship)