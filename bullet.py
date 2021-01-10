import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями"""
    def __init__(self, settings, screen, ship):
        """Создает объект пули в текущей позиуии корабля"""
        super(Bullet, self).__init__()
        self.screen = screen
        # создание пули
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
            settings.bullet_height)  # задаем координаты пули
        self.rect.centerx = ship.rect.centerx  # ровняем центр корабля и пули
        self.rect.top = ship.rect.top  # ровняем верх корабля и пули
        self.y = float(self.rect.y)  # позиция пули в вещественном формате
        self.color = settings.bullet_color  # цвет пули
        self.speed_factor = settings.bullet_speed_factor  # скорость пули


    def update(self):
        """Перемещение пули по экрану"""
        self.y -= self.speed_factor  # переместили пулю
        self.rect.y = self.y  # присвоили пуле новое место

    def draw_bullet(self):
        """Вывод пули на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
