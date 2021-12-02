import math
from game import constants as const
from game.projectile import ProjectileSprite
from game.shooterSprite import ShooterSprite

class SpawnProjectiles():

    def spawnProjectiles(director, x, y):
            """
            Spawns projectiles
            creates projectile objects and saves them to sprite lists
            """
            projectile = ProjectileSprite(const.RESOURCE_PATH + "projectilePNG.png", 1/8 * const.SCALING)
            projectile.setPositionUsed(ShooterSprite.center_x, ShooterSprite.center_y)
            projectile.setSpriteList(director.playerSprite)
            
            projectile.center_x = ShooterSprite.center_x + math.sin(math.pi/180 * (ShooterSprite.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
            projectile.center_y = ShooterSprite.center_y - math.cos(math.pi/180 * (ShooterSprite.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
        
            projectile.change_x = 20 * ((x - ShooterSprite.center_x ) / math.sqrt((x-ShooterSprite.center_x)**2 + (y- ShooterSprite.center_y)**2))
            projectile.change_y = 20 * ((y - ShooterSprite.center_y ) / math.sqrt((x-ShooterSprite.center_x)**2 + (y- ShooterSprite.center_y)**2))
            director.projectileSprites.append(projectile)
            director.allSprites.append(projectile)