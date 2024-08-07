import pygame


class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.score = 0

    def draw(self):
        text = pygame.font.SysFont("fonts/flappy.ttf", 50).render(
            f"Score: {self.score}", True, (255, 255, 255)
        )
        self.screen.blit(text, (0, 0))
