import arcade
import math
import random
from game import constants as const
from game.playerSprite import PlayerSprite
from game.enemysprite import EnemySprite
from game.projectile import ProjectileSprite

HEALTHBAR_WIDTH = 50
HEALTHBAR_HEIGHT = 6
HEALTHBAR_OFFSET_Y = -50

HEALTH_NUMBER_OFFSET_Y = -50

class Director(arcade.View):
    def __init__(self):
        super().__init__()
        self.playerSprite = arcade.SpriteList()
        self.enemySprites = arcade.SpriteList()
        self.projectileSprites = arcade.SpriteList()
        self.allSprites = arcade.SpriteList()
        self.camera_sprites = arcade.Camera(self.window.width, self.window.height)
        self.level = 0

    def on_update(self, delta_time: float):       
        self.allSprites.update()
        self.scroll_to_player()
        if len(self.enemySprites) == 0:
            self.level += 1
            self.spawnEnemies()
            self.player.setEnemySprites(self.enemySprites)


    def on_draw(self):
        arcade.start_render()
        for enemySprite in self.enemySprites:            
            self.drawHealthBars(enemySprite)
        self.drawHealthBars(self.playerSprite[0])
        arcade.draw_text(f"Score: {self.score}", self.player.center_x - self.window.width/2 + 10, self.player.center_y - self.window.height/2 + 20, arcade.color.WHITE, 14)
        self.camera_sprites.use()
        self.allSprites.draw()
        
    def drawHealthBars(self, sprite):
        health_width = HEALTHBAR_WIDTH * (sprite.getHealth() / sprite.getMaxHealth())
        if sprite.getHealth() < sprite.getMaxHealth():
            arcade.draw_rectangle_filled(center_x = sprite.center_x,
                    center_y=sprite.center_y + HEALTHBAR_OFFSET_Y,
                    width=HEALTHBAR_WIDTH,
                    height=3,
                    color=arcade.color.RED)
        arcade.draw_rectangle_filled(center_x=sprite.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                    center_y=sprite.center_y + HEALTHBAR_OFFSET_Y,
                    width=health_width,
                    height=HEALTHBAR_HEIGHT,
                    color=arcade.color.GREEN)
        arcade.draw_text(f"{sprite.getHealth()}/{sprite.getMaxHealth()}",
                    start_x=sprite.center_x,
                    start_y=sprite.center_y + HEALTH_NUMBER_OFFSET_Y,
                    font_size=12,
                    color=arcade.color.WHITE, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        x = x + self.player.center_x - self.window.width/2
        y = y + self.player.center_y - self.window.height/2
        
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.player.change_x = 7 * ((x- self.player.center_x ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
            self.player.change_y = 7 * ((y- self.player.center_y ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
            self.player.lastEventX = x
            self.player.lastEventY = y

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.spawnProjectiles(x, y)

    def scroll_to_player(self):
        position = self.player.center_x - self.window.width / 2, \
            self.player.center_y - self.window.height / 2
        self.camera_sprites.move_to(position, 1)

    def on_resize(self, width: int, height: int):
        self.camera_sprites.resize(int(width), int(height))

    def spawnEnemies(self):
        if self.level <= 10:
            for i in range(0, 10 * self.level):
                self.enemy = EnemySprite(const.RESOURCE_PATH + "zombiePNG.png", const.SCALING) 
                self.enemy.center_x = random.randint(0, 1000)
                self.enemy.center_y = random.randint(0, 1000)
                self.enemySprites.append(self.enemy)
                self.allSprites.append(self.enemy)

    def spawnProjectiles(self, x, y):
        self.projectile = ProjectileSprite(const.RESOURCE_PATH + "projectilePNG.png", 1/8 * const.SCALING)
        self.projectile.setPositionUsed(self.player.center_x, self.player.center_y)
        self.projectile.setEnemySprites(self.enemySprites)
        self.projectile.center_x = self.player.center_x
        self.projectile.center_y = self.player.center_y
        self.projectile.change_x = 20 * ((x - self.player.center_x ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
        self.projectile.change_y = 20 * ((y - self.player.center_y ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
        self.projectileSprites.append(self.projectile)
        self.allSprites.append(self.projectile)
       
    def setup(self):
        self.player = PlayerSprite(const.RESOURCE_PATH + "playerPNG.png", const.SCALING) 
        self.player.center_x = 100
        self.player.center_y = 200
        self.score = 0
        self.playerSprite.append(self.player)     
        self.allSprites.append(self.player)

