import sys
import pygame

"""обработка событий"""
def check_keydown_events(event,traveler):
#кнопка вправо
    if event.key == pygame.K_d:
#задаем истиное значение правой кнопке когда она нажата
        traveler.moving_right = True
#кнопка влево
    elif event.key == pygame.K_a:
#задаем истиное значение левой кнопке когда она нажата
        traveler.moving_left = True
def check_keyup_events(event,traveler):
#кнопка вправо
    if event.key == pygame.K_d:
#задаем значение правой кнопке когда она отжата
        traveler.moving_right = False
#кнопка влево
    elif event.key == pygame.K_a:
 #задаем значение левой кнопке когда она отжата
        traveler.moving_left = False
def check_events(traveler):
    #получение всех событий пользователя
    for event in pygame.event.get():
        #выход из игры
        if event.type == pygame.QUIT:
            #закрываем окно игры
            sys.exit()
        #определяем тип события: "нажатая клавиша"
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,traveler)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,traveler)

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

#задаем команду для запуска магии путешественника
def fire_bullet(ai_Options,screen,traveler,bullets):
    if len(bullets) < ai_Options.bullets_allowed:
        new_bullet = Bullet(ai_Options,screen,traveler)
        bullets.add(new_bullet)


def update_screen(ai_Options,screen,traveler):
#задаем цвет заливки
    screen.fill(ai_Options.bg_color)
 #отрисовываем путешественника
    traveler.blitme()
 #визуализирование окна
    pygame.display.flip()
