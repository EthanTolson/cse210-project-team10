import math
from game import constants as const
from game.projectile import ProjectileSprite

class SpawnProjectiles():

    def spawnProjectiles(director, x, y, shooterSprite):
            """
            Spawns projectiles
            creates projectile objects and saves them to sprite lists
            """
            projectile = ProjectileSprite(const.RESOURCE_PATH + "enemyProjectilePNG.png", 1/8 * const.SCALING)
            projectile.setPositionUsed(shooterSprite.center_x, shooterSprite.center_y)
            projectile.setSpriteList(director.playerSprite)
            
            projectile.center_x = shooterSprite.center_x + math.sin(math.pi/180 * (shooterSprite.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
            projectile.center_y = shooterSprite.center_y - math.cos(math.pi/180 * (shooterSprite.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
        
            projectile.change_x = 20 * ((x - shooterSprite.center_x ) / math.sqrt((x-shooterSprite.center_x)**2 + (y- shooterSprite.center_y)**2))
            projectile.change_y = 20 * ((y - shooterSprite.center_y ) / math.sqrt((x-shooterSprite.center_x)**2 + (y- shooterSprite.center_y)**2))
            director.projectileSprites.append(projectile)
            director.allSprites.append(projectile)