import arcade
import math
import time
"""
Projectile Class:
Subclass of Arcade Sprite. Used for Projectiles.

Attributes:
    positionUsedX (INT) X Position that the projectile was spawned
    positionUsedY (INT) Y Position that the projectile was spawned
    enemySprites (SpriteList) List of enemy sprites
"""

class ProjectileSprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.positionUsedX = None
        self.positionUsedY = None
        self.spriteList = None
        self.damage = None
        

    def update(self):
        super().update()
        if math.sqrt((self.positionUsedY - self.center_y)**2 + (self.positionUsedX - self.center_x)**2) > 600:
            self.remove_from_sprite_lists()

        collisionList = self.collides_with_list(self.spriteList)

        if len(collisionList) != 0:
            collisionList[0].onHit(self.damage)
            self.onHit()

    def onHit(self):
        """
        deletes projectile
        """
        self.remove_from_sprite_lists()

    def setPositionUsed(self, x, y):
        self.positionUsedX = x
        self.positionUsedY = y

    def setDamage(self, damage):
        self.damage = damage

    def setSpriteList(self, spriteList):
        self.spriteList = spriteList