import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(settings, screen, ship, bullets):
    """Орабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():  # отслеживание событий
        if event.type == pygame.QUIT:  # если нажимаем на крестик
            sys.exit()  # закрытие окна
        elif event.type == pygame.KEYDOWN:  # если кнопка нажата
            if event.key == pygame.K_q:  # если нажимаем на q
                sys.exit()  # закрытие окна
            elif event.key == pygame.K_RIGHT:  # если нажата кнопка вправо
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

def update_screen(settings, screen, ship, aliens, bullets):
    """Обновляет изображения на экране и отображает новый экран"""
    screen.fill(settings.bg_color)  # заливка экрана
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # рисуем пули
    ship.blitme()  # отображение корабля
    aliens.draw(screen)
    pygame.display.flip()  # отображение последнего показа экрана

def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули"""
    bullets.update()  # обновление позиции пули
    for bullet in bullets.copy():  # удаление пуль
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(settings, screen, aliens):
    """Создет флот пришельцев"""
    alien = Alien(settings, screen)  # создание пришельца
    alien_width = alien.rect.width  # ширина пришельца = ширине прямоугольника
    available_space_x = settings.screen_width - 2 * alien_width  # вычисление места на экране
    number_aliens_x = int(available_space_x / (2 * alien_width))  # сколько влезет на экран

    # создание первого ряда пришельцев
    for alien_number in range(number_aliens_x):
        alien = Alien(settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
