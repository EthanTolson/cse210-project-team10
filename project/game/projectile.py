from arcade import Sprite
from math import sqrt
from time import time
"""
Projectile Class:
Subclass of Arcade Sprite. Used for Projectiles.

Attributes:
    positionUsedX (INT) X Position that the projectile was spawned
    positionUsedY (INT) Y Position that the projectile was spawned
    enemySprites (SpriteList) List of enemy sprites
"""

class ProjectileSprite(Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.positionUsedX = None
        self.positionUsedY = None
        self.spriteList = None
        

    def update(self):
        super().update()
        if sqrt((self.positionUsedY - self.center_y) ** 2 + (self.positionUsedX - self.center_x) ** 2) > 600:
            self.remove_from_sprite_lists()

        collisionList = self.collides_with_list(self.spriteList)

        if len(collisionList) != 0:
            collisionList[0].onHit()
            collisionList[0].setLastHit(time())
            self.onHit()

    def onHit(self):
        """
        deletes projectile
        """
        self.remove_from_sprite_lists()

    def setPositionUsed(self, x, y):
        self.positionUsedX = x
        self.positionUsedY = y

    def setSpriteList(self, spriteList):
        self.spriteList = spriteList