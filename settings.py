class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry"""

    def __init__(self):
        """Inicjalizacja ustawien gry"""
        #ustawienie ekranu
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2

        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

