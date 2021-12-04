import arcade
from time import time
from math import sqrt
from math import atan2
from math import sin
from math import cos
from math import pi
from game import constants as const
from game.projectile import ProjectileSprite

class GrenadeSprite(arcade.Sprite):
    def __init__(self, director):
        super().__init__(const.RESOURCE_PATH + "grenadePNG.png", const.SCALING)
        self.director = director
        self.time = time()
        self.check = 0
   
    def update(self):
        super().update()
        self.angle += 6
        if self.time + 1 < time() and self.check < 3:
            for i in range(0, 10):
                projectile = ProjectileSprite(const.RESOURCE_PATH + "projectilePNG.png", 1/8 * const.SCALING)
                projectile.setPositionUsed(self.center_x, self.center_y)
                projectile.setSpriteList(self.director.enemySprites)
                projectile.center_x, projectile.center_y = self.center_x, self.center_y

                x = cos( atan2(10, 10) + (36 * i * pi / 180)) * sqrt((10)**2 + (10)**2) + self.center_x
                y = sin( atan2(10, 10) + (36 * i * pi / 180)) * sqrt((10)**2 + (10)**2) + self.center_y

                projectile.change_x = 20 * ((x - self.center_x ) / sqrt((x-self.center_x)**2 + (y- self.center_y)**2))
                projectile.change_y = 20 * ((y - self.center_y ) / sqrt((x-self.center_x)**2 + (y- self.center_y)**2))

                self.director.projectileSprites.append(projectile)
                self.director.allSprites.append(projectile)

            self.time = time()
            self.check += 1
        elif self.check >= 3:
            self.remove_from_sprite_lists()
