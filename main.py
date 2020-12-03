import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run():
    pygame.init()  # Инициальзация игры и создание объекта экрана
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))  # размеры окна
    pygame.display.set_caption('Alien Invasion 9000')  # заголовок окна
    ship = Ship(settings, screen)  # создание корабля

    while True:
        gf.check_events(ship)  # проверяем действия игрока
        ship.update()  # проверяем что с кораблем
        gf.update_screen(settings, screen, ship)  # перерисовываем экран


run()
