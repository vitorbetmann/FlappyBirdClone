import random

import pygame
from pygame.sprite import Sprite


class Pipe(Sprite):
    PIPE_IMAGE = pygame.transform.scale_by(pygame.image.load("images/pipe.png"), 2)
    PIPE_SCROLL = -3

    def __init__(self, game, group):
        super().__init__(group)
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        effective_screen_height = int(0.9 * self.screen_rect.height)
        self.image = Pipe.PIPE_IMAGE
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.right
        self.rect.top = random.randrange(
            int(self.screen_rect.height / 4),
            effective_screen_height - int(self.rect.height * 0.1),
        )

    def update(self):
        self.rect.x += Pipe.PIPE_SCROLL
        if self.rect.right < self.screen_rect.left:
            self.kill()
