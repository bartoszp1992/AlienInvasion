import pygame

class Ship:
    """klasa przeznaczona do zarządzania statkiem kosmicznym"""

    def __init__(self, ai_game):
        """inicjalizacja statku kosmicznego i jego położenie poczatkowe"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #wczytanie obrazu statku i pobranie prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        #położenie statku jest przechowywane we float
        self.x = float(self.rect.x)

        #przechowuje informację o tym, czy statek się porusza
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """uaktualnienie położenia statku na podstawie opcji wskazującycy na jego ruch"""

        #aktualizacja wartości współrzędnej X statku
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #aktualizacja obiektu rect na podstawie wartości self.x
        self.rect.x = self.x

    def blitme(self):
        """wyświetlenie statu w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)