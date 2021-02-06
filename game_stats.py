class GameStats():
    """Отслеживание статистики для игры"""
    def __init__(self, settings):
        """Инициализирует статистику"""
        self.game_active = True
        self.settings = settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ship_left = self.settings.ship_limit
        self.score = 0