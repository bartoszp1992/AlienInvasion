import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez statek"""

    def __init__(self, ai_game):
        """utworzenie obiektu pocisku w aktualnym położeniu statku"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #utworzenie prostokąta pocisku w punkcie 0, 0 a następnie zdefiniowanie dla niego położenia
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej
        self.y = float(self.rect.y)

    def update(self):
        """poruszanie pociskiem po ekranie"""

        #uaktualnienie położenia pocisku
        self.y -= self.settings.bullet_speed

        #uaktualnienie położnia prostokąta pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        """wyświetlanie pocisku na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)

