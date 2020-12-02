import sys
import pygame


def check_events(ship):
    """Орабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():  # отслеживание событий
        if event.type == pygame.QUIT:  # если нажимаем на крестик
            sys.exit()  # закрытие окна
        elif event.type == pygame.KEYDOWN:  # если кнопка нажата
            if event.key == pygame.K_RIGHT:  # если нажата кнопка вправо
                ship.mright = True  # движение
        elif event.type == pygame.KEYUP:  # если кнопка отжата
            if event.key == pygame.K_RIGHT:  # если отжата кнопка вправо
                ship.mright = False  # остановка движения

def update_screen(settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран"""
    screen.fill(settings.bg_color)  # заливка экрана
    ship.blitme()  # отображение корабля
    pygame.display.flip()  # отображение последнего показа экрана
