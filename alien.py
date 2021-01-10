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

    def blitme(self):
        """Выводит пришельца на экран в текущем положении"""
        self.screen.blit(self.image, self.rect)