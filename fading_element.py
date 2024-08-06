from abc import ABC

import pygame


class FadingElement(ABC):
    def __init__(self, game, img_src):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.original_image = pygame.transform.scale(
            pygame.image.load(img_src), (150, 150)
        ).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = game.screen_rect.center
        self.show()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def show(self):
        self.image.set_alpha(255)

    def hide(self):
        self.image.set_alpha(0)
