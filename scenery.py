import pygame


class Scenery:
    """A class to control the ground and background's movement."""

    BG_SCROLL_SPEED = 2
    BG_LOOPING_POINT = 0.357
    GROUND_SCROLL_SPEED = 4
    GROUND_LOOPING_POINT = 0.4

    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen_rect

        # Initialize background
        bg_img = pygame.image.load("images/background.png")
        self.bg_img = pygame.transform.scale_by(
            bg_img, self.settings.WINDOW_SIZE[1] / bg_img.get_height()
        )
        self.bg_rect = self.bg_img.get_rect()
        self.bg_scroll_pos = 0

        # Initialize ground
        ground_img = pygame.image.load("images/ground.png")
        self.ground_img = pygame.transform.scale_by(
            ground_img, self.settings.WINDOW_SIZE[1] / 10 / ground_img.get_height()
        )
        self.ground_rect = self.ground_img.get_rect()
        self.ground_rect.bottom = self.screen_rect.bottom
        self.ground_scroll_pos = 0

    def update(self):
        self.bg_scroll_pos += Scenery.BG_SCROLL_SPEED
        self.bg_scroll_pos %= int(self.bg_rect.width * Scenery.BG_LOOPING_POINT)
        self.bg_rect.left = -self.bg_scroll_pos

        self.ground_scroll_pos += Scenery.GROUND_SCROLL_SPEED
        self.ground_scroll_pos %= int(
            self.ground_rect.width * Scenery.GROUND_LOOPING_POINT
        )
        self.ground_rect.left = -self.ground_scroll_pos

    def draw(self):
        self.screen.blit(self.bg_img, self.bg_rect)
        self.screen.blit(self.ground_img, self.ground_rect)
