import arcade

class EnemySprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 3
        
    def update(self):
        super().update()

    def getEnemyHealth(self):
        return self.hitPoints

    def onHit(self):
        self.hitPoints -= 1