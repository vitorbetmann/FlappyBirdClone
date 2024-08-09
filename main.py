import sys

import pygame

from bird import Bird
from pause import Pause
from pipe_pair import PipePair
from play import Play
from scenery import Scenery
from scoreboard import Scoreboard
from settigns import Settings
from timer import Timer


class FlappyBirdClone:
    """A class to initialize elements and manage the main game loop."""

    STATE_MENU, STATE_START, STATE_PLAY, STATE_PAUSE, STATE_GAME_OVER = (
        "menu",
        "start",
        "play",
        "pause",
        "game over",
    )

    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.settings = Settings()
        self.screen = pygame.display.set_mode(Settings.SCREEN_SIZE, flags=pygame.SCALED)
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Fifty Bird")
        pygame.display.set_icon(pygame.image.load("images/bird.png"))
        pygame.mixer.music.load("sounds/marios_way.mp3")
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")

        self.bird = Bird(self)
        self.scenery = Scenery(self)
        self.scoreboard = Scoreboard(self)

        self.pipes = pygame.sprite.Group()
        self.play = Play(self)
        self.pause = Pause(self)

        self.reset()
        self.state = self.STATE_MENU

    def reset(self):
        pygame.mixer.music.play(-1)
        self.bird.reset()
        self.scoreboard.reset()
        self.play.hide()
        self.pause.hide()
        self.state = self.STATE_START
        self.pipes_spawn_timer = int()
        self.delta_time = 0
        self.pipes = pygame.sprite.Group()
        self.timer = None
        self.timer_start = pygame.time.get_ticks()

    def run(self):
        while True:
            self._check_for_events()
            self._update_all()

            if self.state == self.STATE_START:
                self._countdown(3)

            if self.state == self.STATE_PLAY:
                self._check_points()
                self._check_for_collisions()

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
                        if self.state == self.STATE_PLAY:
                            self.bird.jump()

                        elif self.state == self.STATE_PAUSE:
                            self.pipes_spawn_timer = (
                                pygame.time.get_ticks() - self.delta_time
                            )
                            self.play.show()
                            self.state = self.STATE_PLAY
                            pygame.mixer.music.unpause()

                        elif self.state == self.STATE_MENU:
                            self.timer_start = pygame.time.get_ticks()
                            self.state = self.STATE_START

                        elif self.state == self.STATE_GAME_OVER:
                            if pygame.time.get_ticks() - self.timer_start > 1000:
                                self.reset()

                    case pygame.K_p:
                        self.delta_time = (
                            pygame.time.get_ticks() - self.pipes_spawn_timer
                        )
                        self.state = self.STATE_PAUSE
                        self.play.hide()
                        self.pause.show()
                        self.explosion_sound.play()
                        pygame.mixer.music.pause()

    def _update_all(self):
        if not (self.state == self.STATE_PAUSE or self.state == self.STATE_GAME_OVER):
            self.scenery.update()
        if self.state == self.STATE_PLAY:
            self._spawn_pipe()
            self.pipes.update()
            self.play.update()
        if self.state == self.STATE_PLAY or self.state == self.STATE_GAME_OVER:
            self.bird.update()

    def _draw_all(self):
        self.scenery.draw_bg()
        self.pipes.draw(self.screen)
        self.scenery.draw_ground()
        self.bird.draw()
        if self.state == self.STATE_PAUSE:
            self.pause.draw()
        self.play.draw()
        if not (self.state == self.STATE_GAME_OVER or self.state == self.STATE_MENU):
            self.scoreboard.draw()
        if self.state == self.STATE_GAME_OVER:
            self.scoreboard.draw_game_over()
        elif self.state == self.STATE_MENU:
            self.scoreboard.draw_menu()
        elif self.state == self.STATE_START:
            self.timer.draw()

    def _spawn_pipe(self):
        if (
            pygame.time.get_ticks() - self.pipes_spawn_timer
            > self.settings.pipes_spawn_time
        ):
            PipePair(self, self.pipes)
            self.settings.new_spawn_time()
            self.pipes_spawn_timer = pygame.time.get_ticks()

    def _check_points(self):
        for pipe in self.pipes:
            if not pipe.point_awarded and self.bird.rect.left > pipe.rect.right:
                self.scoreboard.score += pipe.award_point()
                return True
        return False

    def _check_for_collisions(self):
        if (
            pygame.sprite.spritecollide(self.bird, self.pipes, False)
            or self.bird.rect.bottom >= self.scenery.ground_rect.top
        ):
            pygame.mixer.music.pause()
            self.bird.died()
            self.timer_start = pygame.time.get_ticks()
            self.state = self.STATE_GAME_OVER

    def _countdown(self, time_amount):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.timer_start
        countdown_str = str(time_amount - int(delta_time / 1000))
        self.timer = Timer(self, countdown_str)

        if delta_time >= time_amount * 1000:
            self.state = self.STATE_PLAY


if __name__ == "__main__":
    game = FlappyBirdClone()
    game.run()
