from math import sqrt, sin, cos, pi
from game.constants import RESOURCE_PATH, SCALING
from game.projectile import ProjectileSprite

class SpawnProjectiles():

    def spawnProjectiles(director, x, y):
            """
            Spawns projectiles
            creates projectile objects and saves them to sprite lists
            """
            playerx, playery = director.player.center_x, director.player.center_y
            offsetangle = director.player.angle + 45.8550973963
            distance = sqrt((x - playerx) ** 2 + (y - playery) ** 2)
            radconversion = pi / 180

            projectile = ProjectileSprite("".join([RESOURCE_PATH, "projectilePNG.png"]), 1/8 * SCALING)
            projectile.setPositionUsed(playerx, playery)
            projectile.setSpriteList(director.enemySprites)
            
            projectile.center_x = playerx + sin(radconversion * (offsetangle)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
            projectile.center_y = playery - cos(radconversion * (offsetangle)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
        
            projectile.change_x = 20 * ((x - playerx ) / distance)
            projectile.change_y = 20 * ((y - playery ) / distance)
            director.projectileSprites.append(projectile)
            director.allSprites.append(projectile)