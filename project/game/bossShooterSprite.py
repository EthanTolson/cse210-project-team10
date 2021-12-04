from arcade import Sprite
from math import sqrt, atan2, pi
from time import time
from game.spawnEnemyProjectiles import SpawnEnemyProjectiles

"""
BossShooterSprite Class:
Subclass of Arcade Sprite. Used for Enemies.

Attributes:
    hitPoints (INT) The current health of enemy
    player (PlayerSprite) Sprite object for player
"""

class BossShooterSprite(Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 30
        self.player = None
        self.damage = 7
        self.lastHit = 99999999
        self.points = 250
        self.director = None
        self.lastShot = 0
        
    def update(self):
        super().update()
        playercenterx = self.player.center_x
        playercentery = self.player.center_y
        distance = sqrt((self.center_x - playercenterx) ** 2 + (self.center_y - playercentery) ** 2)
        if self.lastShot + 1 < time():
            self.change_x = 5 * (( playercenterx - self.center_x ) / distance)
            self.change_y = 5 * (( playercentery - self.center_y ) / distance)
        else:
            self.change_x = 0
            self.change_y = 0

        self.angle = atan2(playercentery - self.center_y, playercenterx - self.center_x) * 180 / pi

        if distance < 500 and self.lastShot + 1 < time():
            self.lastShot = time()
            SpawnEnemyProjectiles.spawnProjectiles(self.director, self.center_x, self.center_y, self)
            
        if self.hitPoints <= 0:
            self.director.score += self.points
            if len(self.director.enemySprites) != 1:
                self.director.playDeath()
            self.remove_from_sprite_lists()

    def getHealth(self):
        return self.hitPoints

    def getMaxHealth(self):
        return 30
    
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