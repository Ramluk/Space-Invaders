class GameStats:
    """Tracking statistics for the game"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.high_score = 0
        self.game_active = True
        self.settings = ai_game.settings
        self.reset_stats() #creating separate method so it can call each time a new game is created.

        #starting game in inactive state
        self.game_active = False

    def reset_stats(self):
        """Initializing stats to be changed during gameplay"""
        self.ships_left = self.settings.ship_limit
        self.score = 0