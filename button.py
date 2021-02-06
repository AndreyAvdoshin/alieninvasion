import pygame.font

class Button():

    def __init__(self, settings, screen, msg):
        """Инициализирует атрибуты кнопки"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50  # размеры кнопки
        self.button_color = (0, 255, 0)  # цвет кнопки
        self.text_color = (255, 255, 255)  # цвет текста
        self.font = pygame.font.SysFont(None, 48)  # шрифт кнопки
        # построение объекта rect кнопки и выравнивание по центру
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)  # сообщение только один раз

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """отображение пустой кнопки и вывод сообщения"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)