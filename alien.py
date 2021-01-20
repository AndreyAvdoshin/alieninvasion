import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, settings, screen):
        """Инициализирует пришельца и задает его позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ufo.png')  # вид пришельца
        self.rect = self.image.get_rect()  # прямоугольник по картинке
        self.rect.x = self.rect.width  # параметры пришельца
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)  # точная позиция пришельца

    def check_edges(self):
        """True, если пришелец достиг края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Перемещение пришельца вправо"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Выводит пришельца на экран в текущем положении"""
        self.screen.blit(self.image, self.rect)