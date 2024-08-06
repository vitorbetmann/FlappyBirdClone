import sys

import pygame

from bird import Bird
from pipe_pair import PipePair
from scenery import Scenery
from settigns import Settings


class FlappyBirdClone:
    """A class to initialize elements and manage the main game loop."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(Settings.SCREEN_SIZE, flags=pygame.SCALED)
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()

        self.scenery = Scenery(self)
        self.bird = Bird(self)

        pygame.display.set_caption("Fifty Bird")
        pygame.display.set_icon(pygame.image.load("images/bird.png"))

        self.pipe_pairs = pygame.sprite.Group()
        self.spawn_timer = int()

    def run(self):
        while True:
            self._check_for_events()
            self._update_all()

            ...

            self._draw_all()
            pygame.display.update()
            self.clock.tick(self.settings.FPS)
            print(self.clock.get_fps())

    def _check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_f:
                        pygame.display.toggle_fullscreen()
                    case pygame.K_SPACE:
                        self.bird.jump()

    def _update_all(self):
        self.scenery.update()
        self._spawn_pipe()
        self.pipe_pairs.update()
        self.bird.update()

    def _draw_all(self):
        self.scenery.draw_bg()
        self.pipe_pairs.draw(self.screen)
        self.scenery.draw_ground()
        self.bird.draw()

    def _spawn_pipe(self):
        if pygame.time.get_ticks() - self.spawn_timer > self.settings.SPAWN_TIME:
            PipePair(self, self.pipe_pairs)
            self.spawn_timer = pygame.time.get_ticks()


if __name__ == "__main__":
    game = FlappyBirdClone()
    game.run()
