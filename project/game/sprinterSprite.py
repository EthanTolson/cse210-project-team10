from arcade import Sprite
from math import atan2, sqrt, pi
from time import time

"""
SprinterSprite Class:
Subclass of Arcade Sprite. Used for Sprinter Enemies.

Attributes:
    hitPoints (INT) The current health of enemy
    player (PlayerSprite) Sprite object for player
"""

class SprinterSprite(Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 2
        self.player = None
        self.damage = 4
        self.starttime = time()
        self.lastHit = 9999999
        self.director = None
        self.points = 15
        
    def update(self):
        super().update()
        playercenterx = self.player.center_x
        playercentery = self.player.center_y
        distance = sqrt((self.center_x - playercenterx) ** 2 + (self.center_y - playercentery) ** 2)

        if (not self.onCollision()):
            self.change_x = 6 * (( playercenterx - self.center_x ) / distance)
            self.change_y = 6 * (( playercentery - self.center_y ) / distance)
        else:
            self.change_x = 0
            self.change_y = 0

        self.angle = atan2(playercentery - self.center_y, playercenterx - self.center_x) * 180 / pi
        
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
        if self.starttime + 1 < time():
            if(self.collides_with_sprite(self.player)):
                self.starttime = time()
                return True
            return False
        else:
            return True