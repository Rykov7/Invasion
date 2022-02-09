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
        self.bg_color = (43, 40, 50) # Dark grey

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 7
        self.bullet_height = 15
        self.bullet_color = (160,155,170)
        self.bullets_allowed = 3