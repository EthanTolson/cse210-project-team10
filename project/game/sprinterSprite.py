import arcade
import math
import time

from arcade.color import HELIOTROPE
"""
EnemySprite Class:
Subclass of Arcade Sprite. Used for Enemies.

Attributes:
    hitPoints (INT) The current health of enemy
    player (PlayerSprite) Sprite object for player
"""

class SprinterSprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 2
        self.player = None
        
    def update(self):
        super().update()
        self.change_x = 8 * (( self.player.center_x - self.center_x ) / math.sqrt((self.center_x-self.player.center_x)**2 + (self.center_y- self.player.center_y)**2))
        self.change_y = 8 * (( self.player.center_y - self.center_y ) / math.sqrt((self.center_x-self.player.center_x)**2 + (self.center_y- self.player.center_y)**2))
        self.angle = math.atan2(self.player.center_y - self.center_y, self.player.center_x - self.center_x) * 180 / math.pi
        if self.hitPoints <= 0:
            self.remove_from_sprite_lists()
        self.onCollision(self.player)

    def getHealth(self):
        return self.hitPoints

    def getMaxHealth(self):
        return 2

    def onHit(self):
        self.hitPoints -= 1
    
    def setPlayer(self, player):
        self.player = player

    def onCollision(self, player):
        self.player = player
        if(self.collides_with_sprite(self.player)):
            if len(self.collision) != 0 and (self.starttime + 2.5 <= time.time() or self.hitCount < 1):
                self.onHit()
                self.starttime = time.time()
                self.hitCount += 1
