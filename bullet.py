import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

""""создаем магию в позиции путишествиника"""
    def init(self, ai_Options, screen, traveler):

        super().init()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_Options.bullet_width, ai_Options.bullet_height)
        self.rect.centerx = traveler.rect.centerx
        self.rect.top = traveler.rect.top
        self.y = float(self.rect.y)
        self.color = ai_Options.bullet_color
        self.speed_factor = ai_Options.bullet_speed_factor

"""перемещение магии вверх"""

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

"""рисуем магию на экране"""

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
