import pygame

class Ufo(pygame.sprite.Sprite):
    """класс для НЛО"""

    def __init__(self, screen):
        """инициализация НЛО и начальная позиция"""
        super(Ufo, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """выводим НЛО на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """передвижение НЛО"""
        self.y += 0.1
        self.rect.y = self.y