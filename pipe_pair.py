import random

from pipe import Pipe
from settigns import Settings


def new_random_y():
    PipePair.spawn_y += random.choice([-50, 50])
    if PipePair.spawn_y <= int(Settings.SCREEN_SIZE[1] / 3):
        return int(Settings.SCREEN_SIZE[1] / 3)
    if PipePair.spawn_y >= PipePair.EFFECTIVE_SCREEN_HEIGHT:
        return PipePair.EFFECTIVE_SCREEN_HEIGHT
    return PipePair.spawn_y


class PipePair:
    EFFECTIVE_SCREEN_HEIGHT = int(0.8 * Settings.SCREEN_SIZE[1])

    spawn_y = random.randrange(
        int(Settings.SCREEN_SIZE[1] / 3), EFFECTIVE_SCREEN_HEIGHT
    )

    def __init__(self, game, group):
        self.screen_rect = game.screen_rect

        self.bottom_pipe = Pipe(group)
        self.bottom_pipe.rect.top = PipePair.spawn_y
        self.bottom_pipe.rect.left = self.screen_rect.right

        self.top_pipe = Pipe(group, "top")
        self.top_pipe.rect.left = self.bottom_pipe.rect.left
        self.top_pipe.rect.bottom = self.bottom_pipe.rect.top - 150

        PipePair.spawn_y = new_random_y()
