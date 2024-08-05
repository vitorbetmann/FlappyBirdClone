import pygame
from pygame.sprite import Sprite


class Bird(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.image = pygame.image.load("images/bird.png")
        self.image = pygame.transform.scale_by(self.image, 2.5)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        pass
