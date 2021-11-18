import arcade

class EnemySprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 3
        
    def update(self):
        super().update()
        if self.hitPoints <= 0:
            self.remove_from_sprite_lists()

    def getHealth(self):
        return self.hitPoints

    def getMaxHealth(self):
        return 3

    def onHit(self):
        self.hitPoints -= 1