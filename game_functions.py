import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_events(settings, screen, stats, play_button, ship, aliens, bullets):
    """Орабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():  # отслеживание событий
        if event.type == pygame.QUIT:  # если нажимаем на крестик
            sys.exit()  # закрытие окна
        elif event.type == pygame.MOUSEBUTTONDOWN:  # если нажимается мышка
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats,
                play_button, ship, aliens, bullets, mouse_x, mouse_y)
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

def update_screen(settings, screen, stats, sb, ship, aliens, 
    bullets, play_button):
    """Обновляет изображения на экране и отображает новый экран"""
    screen.fill(settings.bg_color)  # заливка экрана
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # рисуем пули
    ship.blitme()  # отображение корабля
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()  # отображение последнего показа экрана

def update_bullets(settings, screen, ship, aliens, bullets):
    """Обновляет позиции пуль и уничтожает старые пули"""
    bullets.update()  # обновление позиции пули
    for bullet in bullets.copy():  # удаление пуль
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets)
    if len(aliens) == 0:
        # Уничтожение существующих пуль и создание нового флота
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, ship, aliens)

def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets):
    """Обработка коллизии пуль с пришельцами"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def check_play_button(settings, screen, stats, play_button, ship,
        aliens, bullets, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # сброс настроек
        settings.initialize_dynamic_settings()
        # указатель мышки скрывается
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

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

def check_fleet_edges(settings, aliens):
    """Реагирует на достижение пришельцем края экрана"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)  # меняем направление
            break

def change_fleet_direction(settings, aliens):
    """Опускает весь флот и меняет направление флота"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed  # применяем опускание флота
    settings.fleet_direction *= -1  # меняем направление

def ship_hit(settings, stats, screen, ship, aliens, bullets):
    """Обрабатывает столкновение корабля с пришельцем"""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        aliens.empty()  # очистка списка пришельцев
        bullets.empty()  # очистка списка пуль
        create_fleet(settings, screen, ship, aliens)  # создание флота
        ship.center_ship()  # раазмещение корабля в центре
        sleep(0.5)  # пауза
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    """Проверяет, добрались ли пришельцы до нижнего края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    # Проверка коллизий "пришелец-корабль"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)