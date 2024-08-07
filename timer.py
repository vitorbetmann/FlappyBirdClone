from pygame.font import SysFont


class Timer:
    def __init__(self, game, text):
        self.screen = game.screen
        self.countdown_surface = SysFont(None, 200).render(text, False, "white")
        self.countdown_rect = self.countdown_surface.get_rect()
        self.countdown_rect.center = self.screen.get_rect().center

    def draw(self):
        self.screen.blit(self.countdown_surface, self.countdown_rect)
