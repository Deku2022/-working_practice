class Mob(Sprite):
    """Класс, представляющий моба ."""

    def __init__(self, ai_settings, screen):
        """Инициализируйте моба и установите его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_Options = ai_Options

        # Загрузите изображение моба и установите его атрибут rect.
        self.image = pygame.image.load('images/pixilart-drawing (1).png')
        self.rect = self.image.get_rect()

        # Запускайте каждого нового моба в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохраните точное положение моба
        self.x = float(self.rect.x)

    def blitme(self):
        """Появляется  моб в его текущем местоположении."""
        self.screen.blit(self.image, self.rect)
