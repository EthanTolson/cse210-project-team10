from arcade import Sprite
from time import time
from math import sqrt, atan2, sin, cos
from game.constants import RESOURCE_PATH, SCALING
from game.projectile import ProjectileSprite

class GrenadeSprite(Sprite):
    def __init__(self, director):
        super().__init__(f"{RESOURCE_PATH}grenadePNG.png", SCALING)
        self.director = director
        self.time = time()
        self.check = 0
   
    def update(self):
        super().update()
        self.angle += 6
        if self.time + 1 < time() and self.check < 3:
            angle = atan2(10, 10)
            enemies = self.director.enemySprites
            projectiles = self.director.projectileSprites
            all = self.director.allSprites
            file = f"{RESOURCE_PATH}projectilePNG.png"
            scaling = 1/8 * SCALING
            distanceshot = sqrt(200)

            for i in range(0, 10):
                projectile = ProjectileSprite(file, scaling)
                projectile.setPositionUsed(self.center_x, self.center_y)
                projectile.setSpriteList(enemies)
                projectile.center_x, projectile.center_y = self.center_x, self.center_y

                x = cos(angle + (i * 0.628319)) * distanceshot + self.center_x
                y = sin(angle + (i * 0.628319)) * distanceshot + self.center_y

                distance = sqrt((x - self.center_x) ** 2 + (y - self.center_y) ** 2)

                projectile.change_x = 20 * ((x - self.center_x) / distance)
                projectile.change_y = 20 * ((y - self.center_y ) / distance)

                projectiles.append(projectile)
                all.append(projectile)

            self.time = time()
            self.check += 1
        elif self.check >= 3:
            self.remove_from_sprite_lists()
