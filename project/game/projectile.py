import arcade

class ProjectileSprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)

    def update(self):
        super().__init__()

    def onHit(self):
        pass