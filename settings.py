class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1200  # задаем ширину экрана
        self.screen_height = 800  # задаем высоту экрана
        self.bg_color = (102, 178, 255)  # задаем цвет бэкграунда
        self.ship_limit = 3  # за игру дается три корабля
        self.ship_speed_factor = 1.5  # скорость перемещения корабля
        # параметры пули
        self.bullet_speed_factor = 3  # скорость пули
        self.bullet_width = 3  # ширина пули
        self.bullet_height = 15  # высота пули
        self.bullet_color = 60, 60, 60  # цвет пули
        self.bullet_allowed = 3  # количество доступных пуль
        # настройки пришельцев
        self.alien_speed_factor = 1  # скорость перемещения пришельца
        self.fleet_drop_speed = 10  # величина снижения пришельцев
        self.fleet_direction = 1  # направнеине по координате X