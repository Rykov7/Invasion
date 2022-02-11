class GameStats:
    """Track statistics for Invasion."""

    def __init__(self, game):
        """Initializa statistics."""
        self.settings = game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit