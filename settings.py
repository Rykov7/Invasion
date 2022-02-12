class Settings:
    """A class to store all settings for Invasion."""

    def __init__(self):
        # """Initializa the game's static settings."""
        # # Screen settings to HD resolution
        self.screen_width = 1366
        self.screen_height = 768
        
        # Screen settings to FullHD resolution
        # self.screen_width = 1920
        # self.screen_height = 1080
        self.bg_color = (33, 30, 35) # Dark grey

        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 7
        self.bullet_height = 14
        self.bullet_color = (247, 225, 207)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Star settings
        self.star_speed = 0.3
        self.star_width = 7
        self.star_height = 7
        self.star_color = (60, 50, 50)
        self.stars_allowed = 700
        self.stars_probability = 7

        # How quickly the game speeds up
        self.speedup_scale = 1.3

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)