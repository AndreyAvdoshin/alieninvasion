import pygame
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from ship import Ship
from pygame.sprite import Group


def run():
    pygame.init()  # Инициальзация игры и создание объекта экрана
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))  # размеры окна
    pygame.display.set_caption('Alien Invasion 9000')  # заголовок окна
    stats = GameStats(settings)  # экземпляр для хранения статистики
    ship = Ship(settings, screen)  # создание корабля
    bullets = Group()  # создание группы для хранения пуль
    aliens = Group()  # сождание группы пришельцев
    gf.create_fleet(settings, screen, ship, aliens)  # создание флота пришельцев

    while True:
        gf.check_events(settings, screen, ship, bullets)  # проверяем действия игрока
        if stats.game_active:
            ship.update()  # проверяем что с кораблем
            gf.update_bullets(settings, screen, ship, aliens, bullets)  # проверяем что с пулями
            gf.update_aliens(settings,stats, screen, ship, aliens, bullets)
        gf.update_screen(settings, screen, ship, aliens, bullets)  # перерисовываем экран

run()
