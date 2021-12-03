import random
from game.enemysprite import EnemySprite
from game.sprinterSprite import SprinterSprite
from game.heavySprite import HeavySprite
from game.bossSprite import BossSprite
from game.bossShooterSprite import BossShooterSprite
from game.shooterSprite import ShooterSprite
from game import constants as const

class SpawnEnemies():

    def spawnEnemies(director):
        if director.level <= 1000:
            SpawnEnemies.spawnShooter(director)
            if director.level % 30 == 0 or director.level % 50 == 0 and director.level > 0:
                SpawnEnemies.spawnBoss(director)
                SpawnEnemies.spawnShooterBoss(director)
            elif director.level > 5 and director.level % 3 == 0:
                for i in range(0, int(director.level / 3)):
                    if len(director.enemySprites) <= 250:
                        if i % 2:
                            SpawnEnemies.spawnSprinterTB(director)
                        else:
                            SpawnEnemies.spawnSprinterLR(director)
                
                for i in range(0, 3 * director.level):   
                    if len(director.enemySprites) <= 250:           
                        if i % 2:
                            SpawnEnemies.spawnZombieTB(director)
                        else:
                            SpawnEnemies.spawnZombieLR(director)

            elif director.level > 10 and director.level % 5 == 0:
                for i in range(0, int(director.level/5)):
                    if len(director.enemySprites) <= 250:
                        SpawnEnemies.spawnHeavy(director)
                        for i in range(0, 10):
                            if len(director.enemySprites) <= 250:
                                if i % 2:
                                    SpawnEnemies.spawnZombieTB(director)
                                else:
                                    SpawnEnemies.spawnZombieLR(director)

            else:
                for i in range(0, 3 * director.level):
                    if len(director.enemySprites) <= 250:
                        if i % 2:
                            SpawnEnemies.spawnZombieTB(director)
                        else:
                            SpawnEnemies.spawnZombieLR(director)

    def spawnShooterBoss(director):
        enemy = BossShooterSprite(const.RESOURCE_PATH + "robotbossPNG.png", const.SCALING + 1.0) 
        enemy.center_x = random.randint(0, 6200)
        enemy.center_y = 6220
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnShooter(director):
        enemy = ShooterSprite(const.RESOURCE_PATH + "shooterPNG.png", const.SCALING) 
        enemy.center_x = random.randint(0, 6400)
        enemy.center_y = random.randrange(-50, 6450, 6489)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnBoss(director):
        enemy = BossSprite(const.RESOURCE_PATH + "bossPNG.png", const.SCALING + 1.0) 
        enemy.center_x = random.randint(0, 6200)
        enemy.center_y = 6220
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnHeavy(director):
        enemy = HeavySprite(const.RESOURCE_PATH + "heavyPNG.png", const.SCALING + 1.0) 
        enemy.center_x = random.randrange(-50, 6450, 6489)
        enemy.center_y = random.randint(0, 6400)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnZombieTB(director):
        enemy = EnemySprite(const.RESOURCE_PATH + "zombiePNG.png", const.SCALING) 
        enemy.center_x = random.randint(0, 6400)
        enemy.center_y = random.randrange(-50, 6450, 6489)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnZombieLR(director):
        enemy = EnemySprite(const.RESOURCE_PATH + "zombiePNG.png", const.SCALING) 
        enemy.center_x = random.randrange(-50, 6450, 6489)
        enemy.center_y = random.randint(0, 6400)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnSprinterTB(director):
        enemy = SprinterSprite(const.RESOURCE_PATH + "sprinterPNG.png", const.SCALING) 
        enemy.center_x = random.randint(0, 6400)
        enemy.center_y = random.randrange(-50, 6450, 6489)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)

    def spawnSprinterLR(director):
        enemy = SprinterSprite(const.RESOURCE_PATH + "sprinterPNG.png", const.SCALING) 
        enemy.center_x = random.randrange(-50, 6450, 6489)
        enemy.center_y = random.randint(0, 6400)
        enemy.setPlayer(director.player)
        enemy.setDirector(director)
        director.enemySprites.append(enemy)
        director.allSprites.append(enemy)