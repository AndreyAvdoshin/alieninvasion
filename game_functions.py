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

def get_number_aliens_x(settings, alien_width):
    """Вычисляет количество пришельцев в ряду"""
    available_space_x = settings.screen_width - 2 * alien_width  # вычисление места на экране
    number_aliens_x = int(available_space_x / (2 * alien_width))  # сколько влезет на экран
    return number_aliens_x  # возвращаем полученное значение

def get_number_rows(settings, ship_height, alien_height):
    """Определяет количество рядов, помещяющихся на экране"""
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width  # ширина пришельца = ширине прямоугольника
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """Создет флот пришельцев"""
    alien = Alien(settings, screen)  # создание пришельца
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # создание первого ряда пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)

def update_aliens(aliens):
    aliens.update()