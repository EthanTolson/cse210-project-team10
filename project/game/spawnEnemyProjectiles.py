from math import sqrt, sin, cos, pi
from game.constants import RESOURCE_PATH, SCALING
from game.enemyProjectile import ProjectileSprite

class SpawnEnemyProjectiles():

    def spawnProjectiles(director, x, y, shooterSprite):
            """
            Spawns projectiles
            creates projectile objects and saves them to sprite lists
            """
            playerx, playery = director.player.center_x, director.player.center_y
            shooterx, shootery = shooterSprite.center_x, shooterSprite.center_y
            offsetangle = shooterSprite.angle + 45.8550973963
            distance = sqrt((x - playerx) ** 2 + (y - playery) ** 2)
            radconversion = pi / 180

            projectile = ProjectileSprite(f"{RESOURCE_PATH}enemyProjectilePNG.png", 3/16 * SCALING)
            projectile.setPositionUsed(shooterx, shootery)
            projectile.setSpriteList(director.playerSprite)
            
            projectile.center_x = shooterx + sin(radconversion * (offsetangle)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
            projectile.center_y = shootery - cos(radconversion * (offsetangle)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
        
            projectile.change_x = 10 * ((playerx - x) / distance)
            projectile.change_y = 10 * ((playery - y) / distance)
            projectile.setDamage(shooterSprite.getDamage())
            director.projectileSprites.append(projectile)
            director.allSprites.append(projectile)

            if shooterSprite.damage == 7:
                projectile = ProjectileSprite(f"{RESOURCE_PATH}enemyProjectilePNG.png", 3/16 * SCALING)
                projectile.setPositionUsed(shooterx, shootery)
                projectile.setSpriteList(director.playerSprite)
                
                projectile.center_x = shooterx + sin(radconversion * (offsetangle * 2)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
                projectile.center_y = shootery - cos(radconversion * (offsetangle * 2)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
            
                projectile.change_x = 10 * ((playerx - x) / distance)
                projectile.change_y = 10 * ((playery - y) / distance)
                projectile.setDamage(shooterSprite.getDamage())
                director.projectileSprites.append(projectile)
                director.allSprites.append(projectile)