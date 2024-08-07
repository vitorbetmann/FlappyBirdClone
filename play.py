from fading_element import FadingElement


class Play(FadingElement):
    def __init__(self, game):
        super().__init__(game, "images/play.png")
        self.transparency_rate = 0
        self.hide()

    def update(self):
        self.transparency_rate = min(self.transparency_rate + 1, 255)
        self.image.set_alpha(self.image.get_alpha() - self.transparency_rate)

    def show(self):
        super().show()
        self.transparency_rate = 0
