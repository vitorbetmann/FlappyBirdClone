import random

from pipe import Pipe
from settigns import Settings


def new_random_ceil():
    PipePair.gap = random.choice(PipePair.GAP_SIZE_OPTIONS)
    return int(0.1 * Settings.SCREEN_SIZE[1] + PipePair.gap)


def new_random_y():
    PipePair.spawn_y += random.choice([-50, 50])
    if PipePair.spawn_y <= PipePair.effective_y_ceil:
        return PipePair.effective_y_ceil
    if PipePair.spawn_y >= PipePair.EFFECTIVE_Y_FLOOR:
        return PipePair.EFFECTIVE_Y_FLOOR
    return PipePair.spawn_y


class PipePair:
    GAP_SIZE_OPTIONS = [150, 175, 200, 225, 250]
    gap = random.choice(GAP_SIZE_OPTIONS)

    effective_y_ceil = int(0.1 * Settings.SCREEN_SIZE[1] + gap)
    EFFECTIVE_Y_FLOOR = int(0.8 * Settings.SCREEN_SIZE[1])

    spawn_y = random.randrange(effective_y_ceil, EFFECTIVE_Y_FLOOR)

    def __init__(self, game, group):
        self.screen_rect = game.screen_rect

        self.bottom_pipe = Pipe(group)
        self.bottom_pipe.rect.top = PipePair.spawn_y
        self.bottom_pipe.rect.left = self.screen_rect.right

        self.top_pipe = Pipe(group, "top")
        self.top_pipe.rect.left = self.bottom_pipe.rect.left
        self.top_pipe.rect.bottom = self.bottom_pipe.rect.top - PipePair.gap

        PipePair.effective_y_ceil = new_random_ceil()
        PipePair.spawn_y = new_random_y()
