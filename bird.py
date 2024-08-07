import pygame
from pygame.sprite import Sprite


class Bird(Sprite):
    """A class to control and represent the bird character."""

    GRAVITY = 0.5
    JUMP_SPEED = 8

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.image = pygame.transform.scale_by(
            pygame.image.load("images/bird.png"), 2.5
        )
        self.jump_sound = pygame.mixer.Sound("sounds/jump.wav")
        self.hurt_sound = pygame.mixer.Sound("sounds/hurt.wav")
        self.rect = self.image.get_rect().inflate(-4, -4)
        self.rect.center = self.screen_rect.center
        self.speed = 0
        self.can_jump = True

    def reset(self):
        self.can_jump = True
        self.speed = 0
        self.rect.center = self.screen_rect.center

    def update(self):
        self.speed += Bird.GRAVITY
        self.rect.y += self.speed

    def jump(self):
        if self.can_jump:
            self.jump_sound.play()
            self.speed = -Bird.JUMP_SPEED

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def died(self):
        self.hurt_sound.play()
        self.can_jump = False
