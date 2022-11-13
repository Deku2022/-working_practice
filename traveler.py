import pygame
#задаем в класс все что касается путешественника
class Traveler():

"""инициализация путешественника"""
    def init(self, ai_Options, screen):
        #получение экрана
        self.screen = screen
        self.ai_Options = ai_Options
        #загружаем изображение путешественника
        self.image = pygame.image.load('images/pixilart-drawing.png')
        #располагаем путешественника на нашем графическом объекте
        self.rect = self.image.get_rect()
        #задаем получение объекта, нашего экрана
        self.screen_rect = screen.get_rect()
        #координаты центра нашего путешественника
        self.rect.centerx = self.screen_rect.centerx
        #задаем нижнюю координату путешественника
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            #движение вправо
            self.rect.centerx += 1