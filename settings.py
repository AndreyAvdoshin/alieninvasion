class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1200  # задаем ширину экрана
        self.screen_height = 800  # задаем высоту экрана
        self.bg_color = (102, 178, 255)  # задаем цвет бэкграунда
        self.ship_speed_factor = 1.5
