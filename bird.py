import pygame
from pygame.sprite import Sprite


class Bird(Sprite):
    """A class to control and represent the bird character."""

    BIRD_IMAGE = pygame.transform.scale_by(pygame.image.load("images/bird.png"), 2.5)
    GRAVITY = 0.5
    JUMP_SPEED = 8

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.image = Bird.BIRD_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.speed = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.speed += Bird.GRAVITY
        self.rect.y += self.speed

    def jump(self):

        self.speed = -Bird.JUMP_SPEED
