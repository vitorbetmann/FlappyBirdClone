import pygame


class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.reset()

    def reset(self):
        self.score = 0

    def draw(self):
        text = pygame.font.SysFont(None, 100).render(
            f"Score: {self.score}", True, (255, 255, 255)
        )
        self.screen.blit(text, (0, 0))

    def draw_menu(self):
        text = pygame.font.SysFont(None, 100).render(
            f"FIFTY BIRD", True, (255, 255, 255)
        )
        text_rect = text.get_rect()
        text_rect.center = self.screen_rect.center
        text_rect.top -= 100
        self.screen.blit(text, text_rect)

        text = pygame.font.SysFont(None, 100).render(
            f"Press 'space' to play", True, (255, 255, 255)
        )
        text_rect = text.get_rect()
        text_rect.center = self.screen_rect.center
        text_rect.top += 100
        self.screen.blit(text, text_rect)

    def draw_game_over(self):
        text = pygame.font.SysFont(None, 80).render(
            f"Oh no, you lost!", True, (255, 255, 255)
        )
        text_rect = text.get_rect()
        text_rect.center = self.screen_rect.center
        text_rect.top -= 80
        self.screen.blit(text, text_rect)

        text = pygame.font.SysFont(None, 100).render(
            f"Your score was: {self.score}", True, (255, 255, 255)
        )
        text_rect = text.get_rect()
        text_rect.center = self.screen_rect.center
        self.screen.blit(text, text_rect)

        text = pygame.font.SysFont(None, 60).render(
            f"Press 'space' to play again", True, (255, 255, 255)
        )
        text_rect = text.get_rect()
        text_rect.center = self.screen_rect.center
        text_rect.top += 80
        self.screen.blit(text, text_rect)
