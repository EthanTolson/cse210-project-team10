import math
from game import constants as const
from game.projectile import ProjectileSprite

class SpawnProjectiles():

    def spawnProjectiles(director, x, y):
            """
            Spawns projectiles
            creates projectile objects and saves them to sprite lists
            """
            projectile = ProjectileSprite(const.RESOURCE_PATH + "projectilePNG.png", 1/8 * const.SCALING)
            projectile.setPositionUsed(director.player.center_x, director.player.center_y)
            projectile.setEnemySprites(director.enemySprites)
            
            projectile.center_x = director.player.center_x + math.sin(math.pi/180 * (director.player.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
            projectile.center_y = director.player.center_y - math.cos(math.pi/180 * (director.player.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
        
            projectile.change_x = 20 * ((x - director.player.center_x ) / math.sqrt((x-director.player.center_x)**2 + (y- director.player.center_y)**2))
            projectile.change_y = 20 * ((y - director.player.center_y ) / math.sqrt((x-director.player.center_x)**2 + (y- director.player.center_y)**2))
            director.projectileSprites.append(projectile)
            director.allSprites.append(projectile)