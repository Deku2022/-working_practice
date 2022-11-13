import sys
import pygame
from Options import Settings
from traveler import Traveler
import game_functions as gf
from pygame.sprite import Group

#запуск игры
def run_game():

#инициализация игры и создание отображаемого объекта
    pygame.init()
    ai_Options = Settings()
    screen = pygame.display.set_mode((ai_Options.screen_width,ai_Options.screen_height))
    #создаем объект путешественника
    traveler = Traveler(ai_Options,screen)
    bullets = Group()
    #заголовок
    pygame.display.set_caption("Traveler")
    #задаем фоновый цвет
    bg_color = (0, 0, 0)

    # игровой цикл
    while True:
        #вызываем функцию ответственную за прослушивание событий
        gf.check_events(ai_Options, screen, traveler,bullets)
        #вызываем функцию "обновление позиции путешествинника"
        traveler.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_Options, screen, traveler,bullets)

#запуск
run_game()