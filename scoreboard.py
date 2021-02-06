import pygame.font

class Scoreboard():
    """Класс для вывода игровой информации"""
    def __init__(self, settings, screen, stats):
        """Инициализирует атрибуты подсчета очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # настройки шрифта для вывода счета
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # подготовка исходного изображения
        self.prep_score()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, 
            self.text_color,self.settings.bg_color)
        # вывод счета на экран в правой верхней части
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счет на экран"""
        self.screen.blit(self.score_image, self.score_rect)