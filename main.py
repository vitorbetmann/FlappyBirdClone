import sys

import pygame

from scenery import Scenery
from settigns import Settings


class FlappyBirdClone:
    """A class to initialize elements and manage the main game loop."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            self.settings.WINDOW_SIZE, flags=pygame.SCALED
        )
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()

        self.scenery = Scenery(self)

        pygame.display.set_caption("Fifty Bird")
        pygame.display.set_icon(pygame.image.load("images/bird.png"))

    def run(self):
        while True:
            self._check_for_events()
            self._update_all()

            self._draw_all()
            pygame.display.update()
            self.clock.tick(self.settings.FPS)

    def _check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

    def _update_all(self):
        self.scenery.update()

    def _draw_all(self):
        self.screen.fill("black")
        self.scenery.draw()


if __name__ == "__main__":
    game = FlappyBirdClone()
    game.run()
