import pygame


class Ship():

    def __init__(self, settings, screen):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ship.png')  # изображение
        self.rect = self.image.get_rect()  # прямоугольник из картинки
        self.screen_rect = screen.get_rect()  # прямоугольник экрана
        self.rect.centerx = self.screen_rect.centerx  # Х картинки = Х экрана
        self.rect.bottom = self.screen_rect.bottom  # картинка внизу экрана
        self.center = float(self.rect.centerx)  # приведение к вещ числу
        self.mright = False
        self.mleft = False

    def update(self):  # движение корабля
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.mleft and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
