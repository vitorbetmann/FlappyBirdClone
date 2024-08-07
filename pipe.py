import pygame
from pygame.sprite import Sprite


class Pipe(Sprite):
    PIPE_IMAGE = pygame.transform.scale_by(pygame.image.load("images/pipe.png"), 2)
    pygame.mixer.init()
    SCORE_SOUND = pygame.mixer.Sound("sounds/score.wav")

    PIPE_SCROLL = 3
    PIPE_POSITION_TOP = "top"
    PIPE_POSITION_BOTTOM = "bottom"

    def __init__(self, group, pos=PIPE_POSITION_BOTTOM):
        super().__init__(group)

        self.image = Pipe.PIPE_IMAGE
        if pos == Pipe.PIPE_POSITION_TOP:
            self.image = pygame.transform.flip(self.image, True, True)
        self.rect = self.image.get_rect()

        self.point_awarded = False

    def update(self):
        self.rect.x -= Pipe.PIPE_SCROLL
        if self.rect.right < 0:
            self.kill()

    def award_point(self):
        Pipe.SCORE_SOUND.play()
        self.point_awarded = True
