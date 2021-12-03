import arcade
import math
import time

"""
SprinterSprite Class:
Subclass of Arcade Sprite. Used for Sprinter Enemies.

Attributes:
    hitPoints (INT) The current health of enemy
    player (PlayerSprite) Sprite object for player
"""

class SprinterSprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 2
        self.player = None
        self.damage = 4
        self.starttime = time.time()
        self.lastHit = 9999999
        self.director = None
        self.points = 15
        
    def update(self):
        super().update()
        if (not self.onCollision()):
            self.change_x = 6 * (( self.player.center_x - self.center_x ) / math.sqrt((self.center_x-self.player.center_x)**2 + (self.center_y- self.player.center_y)**2))
            self.change_y = 6 * (( self.player.center_y - self.center_y ) / math.sqrt((self.center_x-self.player.center_x)**2 + (self.center_y- self.player.center_y)**2))
        else:
            self.change_x = 0
            self.change_y = 0
        self.angle = math.atan2(self.player.center_y - self.center_y, self.player.center_x - self.center_x) * 180 / math.pi
        if self.hitPoints <= 0:
            self.director.score += self.points
            if len(self.director.enemySprites) != 1:
                self.director.playDeath()
            self.remove_from_sprite_lists()
        


    def getHealth(self):
        return self.hitPoints

    def getMaxHealth(self):
        return 2

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

    def onCollision(self):
        if self.starttime + 1 < time.time():
            if(self.collides_with_sprite(self.player)):
                self.starttime = time.time()
                return True
            return False
        else:
            return True