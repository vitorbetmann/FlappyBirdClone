import sys

import pygame

from bird import Bird
from pause import Pause
from pipe_pair import PipePair
from play import Play
from scenery import Scenery
from settigns import Settings


class FlappyBirdClone:
    """A class to initialize elements and manage the main game loop."""

    STATE_START, STATE_PLAY, STATE_PAUSE = "start", "play", "pause"

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(Settings.SCREEN_SIZE, flags=pygame.SCALED)
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Fifty Bird")
        pygame.display.set_icon(pygame.image.load("images/bird.png"))

        self.bird = Bird(self)
        self.scenery = Scenery(self)

        self.sprites = pygame.sprite.Group()
        self.play = Play(self)
        self.pause = Pause(self)

        self.pipes_spawn_timer = int()

        self.state = self.STATE_START

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

            if (
                self.state == self.STATE_PAUSE
                and event.type == pygame.KEYDOWN
                and (event.key == pygame.K_ESCAPE or event.key == pygame.K_p)
            ):
                self.state = self.STATE_PLAY

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_f:
                        pygame.display.toggle_fullscreen()
                    case pygame.K_SPACE:
                        if self.state == self.STATE_PAUSE:
                            self.play.show()
                        if (
                            self.state == self.STATE_PAUSE
                            or self.state == self.STATE_START
                        ):
                            self.state = self.STATE_PLAY
                        self.bird.jump()
                    case pygame.K_p:
                        self.state = self.STATE_PAUSE

    def _update_all(self):
        if not self.state == self.STATE_PAUSE:
            self.scenery.update()
        if self.state == self.STATE_PLAY:
            self._spawn_pipe()
            self.sprites.update()
            self.bird.update()
            self.play.update()

    def _draw_all(self):
        self.scenery.draw_bg()
        self.sprites.draw(self.screen)
        self.scenery.draw_ground()
        self.bird.draw()
        if self.state == self.STATE_PAUSE:
            self.pause.draw()
        self.play.draw()

    def _spawn_pipe(self):
        if pygame.time.get_ticks() - self.pipes_spawn_timer > self.settings.SPAWN_TIME:
            PipePair(self, self.sprites)
            self.pipes_spawn_timer = pygame.time.get_ticks()


if __name__ == "__main__":
    game = FlappyBirdClone()
    game.run()
