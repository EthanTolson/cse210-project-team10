import arcade

class EnemySprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        
    def update(self):
        super().update()

    def onHit(self):
        pass