import pygame


class Scoreboard:
    GOLD_MEDAL_THRESHOLD = 15
    SILVER_MEDAL_THRESHOLD = 10
    BRONZE_MEDAL_THRESHOLD = 5
    MEDAL_OFFSET = 100

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect

        self.gold_medal = pygame.image.load("images/gold_medal.png")
        self.gold_medal = pygame.transform.scale(
            self.gold_medal, (200, 200)
        ).convert_alpha()
        self.gold_medal_rect = self.gold_medal.get_rect()
        self.gold_medal_rect.center = self.screen_rect.center
        self.gold_medal_rect.top = self.screen_rect.top + Scoreboard.MEDAL_OFFSET

        self.silver_medal = pygame.image.load("images/silver_medal.png")
        self.silver_medal = pygame.transform.scale(
            self.silver_medal, (200, 200)
        ).convert_alpha()
        self.silver_medal_rect = self.silver_medal.get_rect()
        self.silver_medal_rect.center = self.screen_rect.center
        self.silver_medal_rect.top = self.screen_rect.top + Scoreboard.MEDAL_OFFSET

        self.bronze_medal = pygame.image.load("images/bronze_medal.png")
        self.bronze_medal = pygame.transform.scale(
            self.bronze_medal, (200, 200)
        ).convert_alpha()
        self.bronze_medal_rect = self.bronze_medal.get_rect()
        self.bronze_medal_rect.center = self.screen_rect.center
        self.bronze_medal_rect.top = self.screen_rect.top + Scoreboard.MEDAL_OFFSET

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
        offset = 0

        if self.score >= self.GOLD_MEDAL_THRESHOLD:
            medal = self.gold_medal
            medal_rect = self.gold_medal_rect
            medal_type = "GOLD"
        elif self.score >= self.SILVER_MEDAL_THRESHOLD:
            medal = self.silver_medal
            medal_rect = self.silver_medal_rect
            medal_type = "SILVER"
        elif self.score >= self.BRONZE_MEDAL_THRESHOLD:
            medal = self.bronze_medal
            medal_rect = self.bronze_medal_rect
            medal_type = "BRONZE"
        else:
            medal = None

        if medal:
            offset = Scoreboard.MEDAL_OFFSET
            self.screen.blit(medal, medal_rect)

            text = pygame.font.SysFont(None, 100).render(
                f"WOW, You got a {medal_type} medal!", True, (255, 255, 255)
            )
            text_rect = text.get_rect()
            text_rect.center = self.screen_rect.center
            text_rect.top = self.screen_rect.top + offset / 3
            self.screen.blit(text, text_rect)

        text = pygame.font.SysFont(None, 80).render(
            f"Oh no, you lost!", True, (255, 255, 255)
        )
        text_rect = text.get_rect()
        text_rect.center = self.screen_rect.center
        text_rect.top += -80 + offset
        self.screen.blit(text, text_rect)

        text = pygame.font.SysFont(None, 100).render(
            f"Your score was: {self.score}", True, (255, 255, 255)
        )
        text_rect = text.get_rect()
        text_rect.center = self.screen_rect.center
        text_rect.top += offset
        self.screen.blit(text, text_rect)

        text = pygame.font.SysFont(None, 60).render(
            f"Press 'space' to play again", True, (255, 255, 255)
        )
        text_rect = text.get_rect()
        text_rect.center = self.screen_rect.center
        text_rect.top += 80 + offset
        self.screen.blit(text, text_rect)
