from fading_element import FadingElement


class Pause(FadingElement):
    def __init__(self, game):
        super().__init__(game, "images/pause.png")
