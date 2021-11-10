import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry"""

    def __init__(self):
        """inicjalizacja gry i utworzenie jej zasobów"""
        pygame.init()

        # utwórz atrybut self.settings  z przypisaną klasą settings.
        self.settings = Settings()

            #w oknie
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

            #fullscreen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("inwazja obcych")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Rozpoczęcie pętli głownej gry"""

        while True:
            #Oczekiwanie na naciśnięcie klawisz alub przycisku myszy
            self._check_events()
            self.ship.update()
            self.bullets.update()

            #usunięcie pocisków znajdujących się poza ekranem
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()



    def _check_events(self):
        """Reakcja na zdarzenia"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """reakcja na wciśnięcie klawisza"""
        if event.key == pygame.K_RIGHT:
            # przesunięcie statku w prawo
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """reakcja na puszczenie klawisza"""
        if event.key == pygame.K_RIGHT:
            # przesunięcie statku w prawo
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """utworzenie nowego pocisku i dodanie go do grupy pocisków"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """uaktualnienie obrazów na ekranie i przejście do nowego ekranu"""

        # odświeżenie ekranu w trakcie każdyj iteracji pętli
        self.screen.fill(self.settings.bg_color)

        # pokazanie statku
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # wyświetlanie ostatnio zmodyfikowanego ekranu
        pygame.display.flip()

if __name__ == '__main__':
    #utworzenie egzemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()
