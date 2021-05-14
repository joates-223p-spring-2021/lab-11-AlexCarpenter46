#This is the game_stats library
#it keeps track of all the stats you
#want to keep track of 

class GameStats :
    """Tracks statistics throughout the game"""

    def __init__(self, ai_game) :
        """Initialize statistics (sheesh this sounds so official) """
        self.settings = ai_game.settings
        self.reset_stats()

        #start game in an active state
        self.game_active = True

    def reset_stats(self) :
        """Initialize statistics that can change throughout the game"""
        self.ships_left = self.settings.ship_limit
