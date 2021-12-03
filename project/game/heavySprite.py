import arcade
import math

"""
HeavySprite Class:
Subclass of Arcade Sprite. Used for Heavy Enemies.

Attributes:
    hitPoints (INT) The current health of enemy
    player (PlayerSprite) Sprite object for player
"""

class HeavySprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 9
        self.player = None
        self.damage = 7
        self.lastHit = 99999999
        self.points = 20
        self.director = None
        
    def update(self):
        super().update()
        self.change_x = 3 * (( self.player.center_x - self.center_x ) / math.sqrt((self.center_x-self.player.center_x)**2 + (self.center_y- self.player.center_y)**2))
        self.change_y = 3 * (( self.player.center_y - self.center_y ) / math.sqrt((self.center_x-self.player.center_x)**2 + (self.center_y- self.player.center_y)**2))
        self.angle = math.atan2(self.player.center_y - self.center_y, self.player.center_x - self.center_x) * 180 / math.pi
        if self.hitPoints <= 0:
            self.director.score += self.points
            self.remove_from_sprite_lists()

    def getHealth(self):
        return self.hitPoints

    def getMaxHealth(self):
        return 9
    
    def getDamage(self):
        return self.damage

    def onHit(self):
        self.hitPoints -= 1
    
    def setPlayer(self, player):
        self.player = player

    def getLastHit(self):
        return self.lastHit

    def setLastHit(self, hit):
        self.lastHit = hit
    
    def setDirector(self, director):
        self.director = director