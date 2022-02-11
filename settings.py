class Settings:
    """A class to store all settings for Invasion."""

    def __init__(self):
        # """Initializa the game's settings."""
        # # Screen settings to HD resolution
        self.screen_width = 1366
        self.screen_height = 768
        
        # Screen settings to FullHD resolution
        # self.screen_width = 1920
        # self.screen_height = 1080
        self.bg_color = (33, 30, 35) # Dark grey

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 7
        self.bullet_height = 14
        self.bullet_color = (160,155,170)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Star settings
        self.star_speed = 0.3
        self.star_width = 7
        self.star_height = 7
        self.star_color = (60, 50, 50)
        self.stars_allowed = 700
        self.stars_probability = 7