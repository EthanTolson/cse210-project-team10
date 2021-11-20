import arcade
import math
import random
from game import constants as const
from game.playerSprite import PlayerSprite
from game.enemysprite import EnemySprite
from game.projectile import ProjectileSprite
"""
Director Class:
Class that hanldes the main game view. Inherits from Arcade View.

Attributes:
    playerSprite (SpriteList) The Player Sprite used for collision methods
    enemySprites (SpriteList) List of all enemysprite objects
    projectileSprites (SpriteList) List of all projectilesprite objects
    allSprites (SpriteList) List of All Non Camera Sprites
    camera_sprites (Camera Sprite) Handles the camera sprites for display
    level (INT) Stores the current Leve as an INT
    lastEventX (INT) Stores the x value of the last mouse movement click
    lastEventY (INT) Stores the x value of the last mouse movement click
"""

class Director(arcade.View):
    def __init__(self):
        super().__init__()
        self.playerSprite = arcade.SpriteList()
        self.enemySprites = arcade.SpriteList()
        self.projectileSprites = arcade.SpriteList()
        self.allSprites = arcade.SpriteList()
        self.camera_sprites = arcade.Camera(self.window.width, self.window.height)
        self.level = 0
        self.lastEventX = 0
        self.lastEventY = 0

    def on_update(self, delta_time: float):
        """
        Updates the sprites positions also spawns enemies if there are none
        """ 
        self.allSprites.update()
        self.scroll_to_player()
        if len(self.enemySprites) == 0 and self.level < 13:
            self.level += 1
            self.spawnEnemies()
            self.player.setEnemySprites(self.enemySprites)
            if self.level > 11:
                arcade.close_window()
        


    def on_draw(self):
        """
        Draws sprites to screen, also draws health bars and mouse clicks
        """
        arcade.start_render()
        for enemySprite in self.enemySprites:            
            self.drawHealthBars(enemySprite)
        self.drawHealthBars(self.playerSprite[0])
        arcade.draw_text(f"Level: {self.level} | Score: {self.score} | Zombies Left: {len(self.enemySprites)}",
         self.player.center_x - self.window.width/2 + 10, 
         self.player.center_y - self.window.height/2 + 20, 
         arcade.color.WHITE, 14)
        arcade.draw_text("x", self.lastEventX, self.lastEventY, arcade.color.GRAPE, 10)
        self.camera_sprites.use()
        self.allSprites.draw()
        
    def drawHealthBars(self, sprite):
        """
        Method for drawing health bars above enemies and player separated from on draw due to being repeated
        """
        health_width = const.HEALTHBAR_WIDTH * (sprite.getHealth() / sprite.getMaxHealth())
        if sprite.getHealth() < sprite.getMaxHealth():
            arcade.draw_rectangle_filled(center_x = sprite.center_x,
                    center_y=sprite.center_y + const.HEALTHBAR_OFFSET_Y,
                    width=const.HEALTHBAR_WIDTH,
                    height=3,
                    color=arcade.color.RED)
        arcade.draw_rectangle_filled(center_x=sprite.center_x - 0.5 * \
                    (const.HEALTHBAR_WIDTH - health_width),
                    center_y=sprite.center_y + const.HEALTHBAR_OFFSET_Y,
                    width=health_width,
                    height=const.HEALTHBAR_HEIGHT,
                    color=arcade.color.GREEN)
        arcade.draw_text(f"{sprite.getHealth()}/{sprite.getMaxHealth()}",
                    start_x=sprite.center_x,
                    start_y=sprite.center_y + const.HEALTH_NUMBER_OFFSET_Y,
                    font_size=12,
                    color=arcade.color.WHITE, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Checks for key presses and does corresponding action
        """
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """
        Checks for mouse clicks for movement updates player velocity 
        Also checks for mouse clicks for projectiles
        """
        x = x + self.player.center_x - self.window.width/2
        y = y + self.player.center_y - self.window.height/2
        self.player.angle = math.atan2(y - self.player.center_y, x - self.player.center_x) * 180 / math.pi
        
        if button == arcade.MOUSE_BUTTON_RIGHT:
            #You will see a similar line of code in many other places
            #in order to keep the velocity consistent despite player moevment direction we take the 
            # distance between the values of the click and divide by the distance to that point on the screen
            # this ensures that your character moves the same distance over the same amount of time no matter the direction they are moving
            self.player.change_x = 7 * ((x- self.player.center_x ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
            self.player.change_y = 7 * ((y- self.player.center_y ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
            self.player.lastEventX = x
            self.player.lastEventY = y
            self.lastEventY = y
            self.lastEventX = x

        #Spawns the projectiles
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.spawnProjectiles(x, y)

    def scroll_to_player(self):
        """
        Moves the camera center to the player to ensure player does not move off screen
        """
        position = self.player.center_x - self.window.width / 2, \
            self.player.center_y - self.window.height / 2
        self.camera_sprites.move_to(position, 1)

    def on_resize(self, width: int, height: int):
        """
        Ensures camera works if user resizes screen
        """
        self.camera_sprites.resize(int(width), int(height))

    def spawnEnemies(self):
        """
        Used to spawn enemies based on the level the player is on
        """
        if self.level <= 10:
            for i in range(0, 5 * self.level):
                if i % 2:
                    self.enemy = EnemySprite(const.RESOURCE_PATH + "zombiePNG.png", const.SCALING) 
                    self.enemy.center_x = random.randint(0, 3000)
                    self.enemy.center_y = random.randrange(0, 3001, 3000)
                    self.enemy.setPlayer(self.player)
                    self.enemySprites.append(self.enemy)
                    self.allSprites.append(self.enemy)
                else:
                    self.enemy = EnemySprite(const.RESOURCE_PATH + "zombiePNG.png", const.SCALING) 
                    self.enemy.center_x = random.randrange(0, 3001, 3000)
                    self.enemy.center_y = random.randint(0, 3000)
                    self.enemy.setPlayer(self.player)
                    self.enemySprites.append(self.enemy)
                    self.allSprites.append(self.enemy)

    def spawnProjectiles(self, x, y):
        """
        Spawns projectiles
        creates projectile objects and saves them to sprite lists
        """
        self.projectile = ProjectileSprite(const.RESOURCE_PATH + "projectilePNG.png", 1/8 * const.SCALING)
        self.projectile.setPositionUsed(self.player.center_x, self.player.center_y)
        self.projectile.setEnemySprites(self.enemySprites)
        
        self.projectile.center_x = self.player.center_x + math.sin(math.pi/180 * (self.player.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
        self.projectile.center_y = self.player.center_y - math.cos(math.pi/180 * (self.player.angle + 45.8550973963)) * 33.54 # Calculates the offset for the bullet to shoot out of the gun
    
        self.projectile.change_x = 20 * ((x - self.player.center_x ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
        self.projectile.change_y = 20 * ((y - self.player.center_y ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
        self.projectileSprites.append(self.projectile)
        self.allSprites.append(self.projectile)
       
    def setup(self):
        """
        Setup for before first update cycle
        creates the player object
        """
        self.player = PlayerSprite(const.RESOURCE_PATH + "playerPNG.png", const.SCALING) 
        self.player.center_x = 1500
        self.player.center_y = 1500
        self.score = 0
        self.playerSprite.append(self.player)     
        self.allSprites.append(self.player)

