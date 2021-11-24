import arcade
import time
import math
"""
PlayerSprite Class:
Subclass of Arcade Sprite. Used for the Player.

Attributes:
    player_hp (INT) The player's current health
    enemySprites (SpriteList) List of enemy sprites
    collision (SpriteList) List of EnemySprites that are currently colliding with player sprite
    lastEventX (INT) X Position of the last movement command
    lastEventY (INT) Y Position of the last movement command
    hitCount (int) Number of hits the player has taken used to make sure player gets hit on first hit
    starttime (Float) Time.time() the time of the last collision with enemy
"""

class PlayerSprite(arcade.Sprite):

    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.player_hp = 30
        self.enemySprites = None
        self.collision = None
        self.lastEventX = None
        self.lastEventY = None
        self.hitCount = 0
        self.starttime = time.time()

    def update(self):
        super().update()

        if self.player_hp <= 0:
            arcade.close_window()
        for i in range(0, 6):
            if self.lastEventX != None and (self.lastEventX <= self.center_x + i and self.lastEventX \
                >= self.center_x - i) and(self.lastEventY <= self.center_y + i and self.lastEventY \
                    >= self.center_y - i):
                self.change_x = 0
                self.change_y = 0
        if self.enemySprites != None:
            self.collision = self.collides_with_list(self.enemySprites)
            if len(self.collision) != 0 and (self.starttime + 2.5 <= time.time() or self.hitCount < 1):
                self.onHit(self.collision[0].getDamage())
                self.starttime = time.time()
                self.hitCount += 1
        

    def setEnemySprites(self, enemy_sprite_list):
        self.enemySprites = enemy_sprite_list

    def getHealth(self):
        return self.player_hp

    def getMaxHealth(self):
        return 30

    def onHit(self, damage = 3):
        self.player_hp -= damage
    
    def movement(self, x, y):
        #You will see a similar line of code in many other places
        #in order to keep the velocity consistent despite player moevment direction we take the 
        # distance between the values of the click and divide by the distance to that point on the screen
        # this ensures that your character moves the same distance over the same amount of time no matter the direction they are moving
        self.change_x = 3.5 * ((x- self.center_x ) / math.sqrt((x-self.center_x)**2 + (y- self.center_y)**2))
        self.change_y = 3.5 * ((y- self.center_y ) / math.sqrt((x-self.center_x)**2 + (y- self.center_y)**2))
        self.lastEventY = y
        self.lastEventX = x