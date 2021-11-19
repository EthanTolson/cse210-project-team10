import arcade
import math
"""
EnemySprite Class:
Subclass of Arcade Sprite. Used for Enemies.

Attributes:
    hitPoints (INT) The current health of enemy
    player (PlayerSprite) Sprite object for player
"""

class EnemySprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 3
        self.player = None
        
    def update(self):
        super().update()
        self.change_x = 4 * (( self.player.center_x - self.center_x ) / math.sqrt((self.center_x-self.player.center_x)**2 + (self.center_y- self.player.center_y)**2))
        self.change_y = 4 * (( self.player.center_y - self.center_y ) / math.sqrt((self.center_x-self.player.center_x)**2 + (self.center_y- self.player.center_y)**2))

        if self.hitPoints <= 0:
            self.remove_from_sprite_lists()

    def getHealth(self):
        return self.hitPoints

    def getMaxHealth(self):
        return 3

    def onHit(self):
        self.hitPoints -= 1
    
    def setPlayer(self, player):
        self.player = player