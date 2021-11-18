import arcade
import math

class ProjectileSprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.positionUsedX = None
        self.positionUsedY = None
        self.enemySprites = None
        

    def update(self):
        super().update()
        if math.sqrt((self.positionUsedY - self.center_y)**2 + (self.positionUsedX - self.center_x)**2) > 600:
            self.remove_from_sprite_lists()

        collisionList = self.collides_with_list(self.enemySprites)

        if len(collisionList) != 0:
            collisionList[0].onHit()
            self.onHit()

    def onHit(self):
        """
        deletes projectile
        """
        self.remove_from_sprite_lists()

    def setPositionUsed(self, x, y):
        self.positionUsedX = x
        self.positionUsedY = y

    def setEnemySprites(self, enemySprites):
        self.enemySprites = enemySprites