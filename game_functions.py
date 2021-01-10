import sys
import pygame
from bullet import Bullet


def check_events(settings, screen, ship, bullets):
    """Орабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():  # отслеживание событий
        if event.type == pygame.QUIT:  # если нажимаем на крестик
            sys.exit()  # закрытие окна
        elif event.type == pygame.KEYDOWN:  # если кнопка нажата
            if event.key == pygame.K_RIGHT:  # если нажата кнопка вправо
                ship.mright = True  # движение
            elif event.key == pygame.K_LEFT:
                ship.mleft = True
            elif event.key == pygame.K_SPACE:
                if len(bullets) < settings.bullet_allowed:
                    new_bullet = Bullet(settings, screen, ship)  # новая пуля
                    bullets.add(new_bullet)  # добавление пули в группу
        elif event.type == pygame.KEYUP:  # если кнопка отжата
            if event.key == pygame.K_RIGHT:  # если отжата кнопка вправо
                ship.mright = False  # остановка движения
            elif event.key == pygame.K_LEFT:
                ship.mleft = False


def update_screen(settings, screen, ship, bullets):
    """Обновляет изображения на экране и отображает новый экран"""
    screen.fill(settings.bg_color)  # заливка экрана
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # рисуем пули
    ship.blitme()  # отображение корабля
    pygame.display.flip()  # отображение последнего показа экрана
