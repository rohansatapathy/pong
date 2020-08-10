class GameStats:
    """Track scores for pong"""

    def __init__(self, pong_game):
        """Initialize statistics"""
        self.pong_game = pong_game
        self.reset_stats()

    def reset_stats(self):
        """Reset the scores for left and right"""
        self.left_score = self.right_score = 0
