import random


class Settings:
    SCREEN_SIZE = 1280, 720
    FPS = 60
    TIME_SPAWN_OPTIONS = [1500, 1750, 2000]

    def __init__(self):
        self.pipes_spawn_time = None
        self.new_spawn_time()

    def new_spawn_time(self):
        self.pipes_spawn_time = random.choice(Settings.TIME_SPAWN_OPTIONS)
