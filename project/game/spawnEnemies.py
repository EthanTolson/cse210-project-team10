from random import randint
from random import randrange
from game.enemysprite import EnemySprite
from game.sprinterSprite import SprinterSprite
from game.heavySprite import HeavySprite
from game.bossSprite import BossSprite
from game.bossShooterSprite import BossShooterSprite
from game.shooterSprite import ShooterSprite
from game import constants as const

class SpawnEnemies():

    def spawnShooterBoss(director):
        enemy = BossShooterSprite(const.RESOURCE_PATH + "robotbossPNG.png", const.SCALING + .5) 
        enemy.center_x = randint(0, 6200)
        enemy.center_y = 6220
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnShooter(director):
        enemy = ShooterSprite(const.RESOURCE_PATH + "shooterPNG.png", const.SCALING) 
        enemy.center_x = randint(0, 6400)
        enemy.center_y = randrange(-50, 6450, 6489)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnBoss(director):
        enemy = BossSprite(const.RESOURCE_PATH + "bossPNG.png", const.SCALING + 1.0) 
        enemy.center_x = randint(0, 6200)
        enemy.center_y = 6220
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnHeavy(director):
        enemy = HeavySprite(const.RESOURCE_PATH + "heavyPNG.png", const.SCALING + 1.0) 
        enemy.center_x = randrange(-50, 6450, 6489)
        enemy.center_y = randint(0, 6400)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnZombieTB(director):
        enemy = EnemySprite(const.RESOURCE_PATH + "zombiePNG.png", const.SCALING) 
        enemy.center_x = randint(0, 6400)
        enemy.center_y = randrange(-50, 6450, 6489)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnZombieLR(director):
        enemy = EnemySprite(const.RESOURCE_PATH + "zombiePNG.png", const.SCALING) 
        enemy.center_x = randrange(-50, 6450, 6489)
        enemy.center_y = randint(0, 6400)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnSprinterTB(director):
        enemy = SprinterSprite(const.RESOURCE_PATH + "sprinterPNG.png", const.SCALING) 
        enemy.center_x = randint(0, 6400)
        enemy.center_y = randrange(-50, 6450, 6489)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnSprinterLR(director):
        enemy = SprinterSprite(const.RESOURCE_PATH + "sprinterPNG.png", const.SCALING) 
        enemy.center_x = randrange(-50, 6450, 6489)
        enemy.center_y = randint(0, 6400)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnEnemies(director):
        if director.level % 10 == 0:
            for i in range(0, int(director.level/5)):
                if len(director.enemySprites) < 30 and (director.level / 10) % 2 != 0:
                    SpawnEnemies.spawnBoss(director)
                elif len(director.enemySprites) < 30 and (director.level / 10) % 2 == 0:
                    SpawnEnemies.spawnShooterBoss(director)
        elif director.level < 5:
            for i in range(0, 5 * director.level):
                if len(director.enemySprites) <= 250:
                    if i % 2:
                        SpawnEnemies.spawnZombieTB(director)
                    else:
                        SpawnEnemies.spawnZombieLR(director)
        else:
            if director.level * 3 < 250:
                numEnemies = director.level * 3
            else:
                numEnemies = 250
                
            for i in range(0, int(numEnemies * .1)):
                SpawnEnemies.spawnShooter(director)

            for i in range(0, int(numEnemies * .2)):
                if i % 2:
                    SpawnEnemies.spawnSprinterTB(director)
                else:
                    SpawnEnemies.spawnSprinterLR(director)

            for i in range(0, int(numEnemies * .05)):
                SpawnEnemies.spawnHeavy(director)

            for i in range(0, int(numEnemies * .65)):
                if i % 2:
                    SpawnEnemies.spawnZombieTB(director)
                else:
                    SpawnEnemies.spawnZombieLR(director)