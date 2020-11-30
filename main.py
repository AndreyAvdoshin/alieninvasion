import sys
import pygame
from settings import Settings
from ship import Ship


def run():
    pygame.init()  # Инициальзация игры и создание объекта экрана
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))  # размеры окна
    pygame.display.set_caption('Alien Invasion 9000')  # заголовок окна
    ship = Ship(screen)  # создание корабля

    while True:
        for event in pygame.event.get():  # отслеживание событий
            if event.type == pygame.QUIT:  # если нажимаем на крестик
                sys.exit()  # закрытие окна
        screen.fill(settings.bg_color)  # заливка экрана
        ship.blitme()  # отображение корабля
        pygame.display.flip()  # отображение последнего показа экрана


run()
