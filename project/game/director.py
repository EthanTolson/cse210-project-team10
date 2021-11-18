import arcade
import math
from game import constants as const
from game.playerSprite import PlayerSprite
from game.enemysprite import EnemySprite
from game.projectile import ProjectileSprite
from game.spritehealth import SpriteHealth

class Director(arcade.View):
    def __init__(self):
        super().__init__()
        self.playerSprite = arcade.SpriteList()
        self.enemySprites = arcade.SpriteList()
        self.allSprites = arcade.SpriteList()

    def on_update(self, delta_time: float):       
        self.allSprites.update()

    def on_draw(self):
        arcade.start_render()
        self.enemySprites_list.draw()
        self.player_list.draw()

        for enemySprites in self.enemySprites_list:
            enemySprites.draw_health_number()
            enemySprites.draw_health_bar()

        for playerSprite in self.playerSprite_list:
            playerSprite.draw_health_number()
            playerSprite.draw_health_bar()

        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        self.allSprites.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def setup(self):
        self.player = PlayerSprite(const.RESOURCE_PATH + "playerPNG.png", const.SCALING)
        self.player.center_x = 100
        self.player.center_y = 200
        self.score = 0
        self.playerSprite.append(self.player)
        self.allSprites.append(self.player)

        self.enemy = EnemySprite(const.RESOURCE_PATH + "enemySpritesPNG.png", const.SCALING)
        self.enemy.center_x = 400
        self.enemy.center_y = 200
        self.enemySprites.append(self.enemy)
        self.allSprites.append(self.enemy)


        