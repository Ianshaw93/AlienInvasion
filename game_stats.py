class GameStats():
    # Track Statistics for game

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # start alien invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        # start up stats that can change during the game
        self.ships_left = self.ai_settings.ship_limit
