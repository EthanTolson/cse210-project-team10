import math
from game import constants as const
from game.enemyProjectile import ProjectileSprite

class SpawnEnemyProjectiles():

    def spawnProjectiles(director, x, y, shooterSprite):
            """
            Spawns projectiles
            creates projectile objects and saves them to sprite lists
            """
            projectile = ProjectileSprite(const.RESOURCE_PATH + "enemyProjectilePNG.png", 3/16 * const.SCALING)
            projectile.setPositionUsed(shooterSprite.center_x, shooterSprite.center_y)
            projectile.setSpriteList(director.playerSprite)
            
            projectile.center_x = shooterSprite.center_x + math.sin(math.pi/180 * (shooterSprite.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
            projectile.center_y = shooterSprite.center_y - math.cos(math.pi/180 * (shooterSprite.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
        
            projectile.change_x = 10 * ((director.player.center_x - x) / math.sqrt((x-director.player.center_x)**2 + (y- director.player.center_y)**2))
            projectile.change_y = 10 * ((director.player.center_y - y) / math.sqrt((x-director.player.center_x)**2 + (y- director.player.center_y)**2))
            projectile.setDamage(shooterSprite.getDamage())
            director.projectileSprites.append(projectile)
            director.allSprites.append(projectile)

            if shooterSprite.damage == 7:
                projectile = ProjectileSprite(const.RESOURCE_PATH + "enemyProjectilePNG.png", 3/16 * const.SCALING)
                projectile.setPositionUsed(shooterSprite.center_x, shooterSprite.center_y)
                projectile.setSpriteList(director.playerSprite)
                
                projectile.center_x = shooterSprite.center_x + math.sin(math.pi/180 * (shooterSprite.angle + 45.8550973963*2)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
                projectile.center_y = shooterSprite.center_y - math.cos(math.pi/180 * (shooterSprite.angle + 45.8550973963*2)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
            
                projectile.change_x = 10 * ((director.player.center_x - x) / math.sqrt((x-director.player.center_x)**2 + (y- director.player.center_y)**2))
                projectile.change_y = 10 * ((director.player.center_y - y) / math.sqrt((x-director.player.center_x)**2 + (y- director.player.center_y)**2))
                projectile.setDamage(shooterSprite.getDamage())
                director.projectileSprites.append(projectile)
                director.allSprites.append(projectile)