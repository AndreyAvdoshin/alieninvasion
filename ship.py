import pygame


class Ship():

    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')  # изображение
        self.rect = self.image.get_rect()  # прямоугольник из картинки
        self.screen_rect = screen.get_rect()  # прямоугольник экрана
        self.rect.centerx = self.screen_rect.centerx  # Х картинки = Х экрана
        self.rect.bottom = self.screen_rect.bottom  # картинка внизу экрана

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
