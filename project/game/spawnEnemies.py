from random import randint, randrange
from game.enemysprite import EnemySprite
from game.sprinterSprite import SprinterSprite
from game.heavySprite import HeavySprite
from game.bossSprite import BossSprite
from game.bossShooterSprite import BossShooterSprite
from game.shooterSprite import ShooterSprite
from game.constants import RESOURCE_PATH, SCALING

class SpawnEnemies():

    def spawnShooterBoss(director, player, enemies, all):
        enemy = BossShooterSprite("".join([RESOURCE_PATH, "robotbossPNG.png"]), SCALING + .5) 
        enemy.center_x = randint(0, 6200)
        enemy.center_y = 6220
        enemy.setPlayer(player)
        enemy.setDirector(director)
        enemies.append(enemy)
        all.append(enemy)

    def spawnShooter(director, player, enemies, all):
        enemy = ShooterSprite("".join([RESOURCE_PATH, "shooterPNG.png"]), SCALING) 
        enemy.center_x = randint(0, 6400)
        enemy.center_y = randrange(-50, 6450, 6489)
        enemy.setPlayer(player)
        enemy.setDirector(director)
        enemies.append(enemy)
        all.append(enemy)

    def spawnBoss(director, player, enemies, all):
        enemy = BossSprite("".join([RESOURCE_PATH, "bossPNG.png"]), SCALING + 1.0) 
        enemy.center_x = randint(0, 6200)
        enemy.center_y = 6220
        enemy.setPlayer(player)
        enemy.setDirector(director)
        enemies.append(enemy)
        all.append(enemy)

    def spawnHeavy(director, player, enemies, all):
        enemy = HeavySprite("".join([RESOURCE_PATH, "heavyPNG.png"]), SCALING + 1.0) 
        enemy.center_x = randrange(-50, 6450, 6489)
        enemy.center_y = randint(0, 6400)
        enemy.setPlayer(player)
        enemy.setDirector(director)
        enemies.append(enemy)
        all.append(enemy)

    def spawnZombieTB(director, player, enemies, all):
        enemy = EnemySprite("".join([RESOURCE_PATH, "zombiePNG.png"]), SCALING) 
        enemy.center_x = randint(0, 6400)
        enemy.center_y = randrange(-50, 6450, 6489)
        enemy.setPlayer(player)
        enemy.setDirector(director)
        enemies.append(enemy)
        all.append(enemy)

    def spawnZombieLR(director, player, enemies, all):
        enemy = EnemySprite("".join([RESOURCE_PATH, "zombiePNG.png"]), SCALING) 
        enemy.center_x = randrange(-50, 6450, 6489)
        enemy.center_y = randint(0, 6400)
        enemy.setPlayer(player)
        enemy.setDirector(director)
        enemies.append(enemy)
        all.append(enemy)

    def spawnSprinterTB(director, player, enemies, all):
        enemy = SprinterSprite("".join([RESOURCE_PATH, "sprinterPNG.png"]), SCALING) 
        enemy.center_x = randint(0, 6400)
        enemy.center_y = randrange(-50, 6450, 6489)
        enemy.setPlayer(player)
        enemy.setDirector(director)
        enemies.append(enemy)
        all.append(enemy)

    def spawnSprinterLR(director, player, enemies, all):
        enemy = SprinterSprite("".join([RESOURCE_PATH, "sprinterPNG.png"]), SCALING) 
        enemy.center_x = randrange(-50, 6450, 6489)
        enemy.center_y = randint(0, 6400)
        enemy.setPlayer(player)
        enemy.setDirector(director)
        enemies.append(enemy)
        all.append(enemy)

    def spawnEnemies(director):
        enemies = director.enemySprites
        all = director.allSprites
        player = director.player
        level = director.level
        if level % 10 == 0:
            for i in range(0, int(level/5)):
                if len(enemies) < 30 and (level / 10) % 2 != 0:
                    SpawnEnemies.spawnBoss(director, player, enemies, all)
                elif len(enemies) < 30 and (level / 10) % 2 == 0:
                    SpawnEnemies.spawnShooterBoss(director, player, enemies, all)
        elif level < 5:
            for i in range(0, 5 * level):
                if len(enemies) <= 250:
                    if i % 2:
                        SpawnEnemies.spawnZombieTB(director, player, enemies, all)
                    else:
                        SpawnEnemies.spawnZombieLR(director, player, enemies, all)
        else:
            if level * 3 < 250:
                numEnemies = level * 3
            else:
                numEnemies = 250
                
            for i in range(0, int(numEnemies * .1)):
                SpawnEnemies.spawnShooter(director, player, enemies, all)

            for i in range(0, int(numEnemies * .2)):
                if i % 2:
                    SpawnEnemies.spawnSprinterTB(director, player, enemies, all)
                else:
                    SpawnEnemies.spawnSprinterLR(director, player, enemies, all)

            for i in range(0, int(numEnemies * .05)):
                SpawnEnemies.spawnHeavy(director, player, enemies, all)

            for i in range(0, int(numEnemies * .65)):
                if i % 2:
                    SpawnEnemies.spawnZombieTB(director, player, enemies, all)
                else:
                    SpawnEnemies.spawnZombieLR(director, player, enemies, all)