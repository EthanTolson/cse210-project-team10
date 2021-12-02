import arcade
import math
import time
from game import constants as const
from game.playerSprite import PlayerSprite
from game.drawHealthbars import DrawHealthBars
from game.spawnEnemies import SpawnEnemies
from game.qAbility import QAbility
from game.endScreen import EndScreen
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
        self.tileMap = None
        self.level = 0
        self.lastEventX = 0
        self.lastEventY = 0
        self.help_bool = False
        self.pauseBool = False
        self.gunSound = arcade.Sound(const.RESOURCE_PATH + "gunshot.ogg")
        self.helpscreen = arcade.load_texture(const.RESOURCE_PATH + "helpPNG.png")
        

    def on_update(self, delta_time: float):
        """
        Updates the sprites positions also spawns enemies if there are none
        """ 
        if not self.pauseBool:
            self.physicsEngine.update()
            self.allSprites.update()
            self.scroll_to_player()
            if len(self.enemySprites) == 0 and self.level < 1003:
                self.level += 1
                SpawnEnemies.spawnEnemies(self)
                self.player.setEnemySprites(self.enemySprites)
                if self.level > 1001:
                    arcade.close_window()
        
    def on_draw(self):
        """
        Draws sprites to screen, also draws health bars and mouse clicks
        """
        arcade.start_render()
        self.scene.draw()

        #Healthbars were causing game to lag need to find fix
        #Fix is to only draw healthbars for enemies after they have been hit and only for 1.5 seconds after the hit
        for enemySprite in self.enemySprites:
            if enemySprite.getHealth() < enemySprite.getMaxHealth() and enemySprite.getLastHit() + 1.5 > time.time():
                DrawHealthBars.drawHealthBars(enemySprite)

        DrawHealthBars.drawHealthBars(self.playerSprite[0])

        arcade.draw_text("x", self.lastEventX, self.lastEventY, arcade.color.GRAPE, 10, bold = True)

        self.camera_sprites.use()
        self.allSprites.draw()

        arcade.draw_lrtb_rectangle_outline(-500, 6900, 6900, -500, arcade.color.BLACK, 1000)  

        if self.help_bool or self.pauseBool:
            arcade.draw_lrwh_rectangle_textured(self.player.center_x - self.window.width/4 -10,
            self.player.center_y - 200, 600 , 600, texture = self.helpscreen)

        arcade.draw_text(f"Level: {self.level} | Score: {self.score} | Zombies Left: {len(self.enemySprites)} | Ammo Left(Q to Switch Weapons): {self.q.getShotsLeft()} | TAB: Show Controls/Help",
         self.player.center_x - self.window.width/2 + 10, 
         self.player.center_y - self.window.height/2 + 20, 
         arcade.color.WHITE, 14)   

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Checks for key presses and does corresponding action
        """
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            gameView = EndScreen()
            Director.show_view(gameView)
        elif symbol == arcade.key.TAB:
            self.help_bool = True
        elif symbol == arcade.key.P:
            self.pauseBool = not self.pauseBool
        elif symbol == arcade.key.Q:
            self.q.switchStance(self.player)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.TAB:
            self.help_bool = not self.help_bool

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """
        Checks for mouse clicks for movement updates player velocity 
        Also checks for mouse clicks for projectiles
        """
        x = x + self.player.center_x - self.window.width/2
        y = y + self.player.center_y - self.window.height/2
        
        if not self.pauseBool:
            
            if button == arcade.MOUSE_BUTTON_RIGHT:
                #These if statements prevent wall kiting
                if x < 170:
                    x = 170
                elif x > 6040:
                    x = 6040

                if y < 170:
                    y = 170
                elif y > 6230:
                    y = 6230

                self.player.movement(x,y)
                self.lastEventY = y
                self.lastEventX = x

            self.player.angle = math.atan2(y - self.player.center_y, x - self.player.center_x) * 180 / math.pi
            
            #Spawns the projectiles
            if button == arcade.MOUSE_BUTTON_LEFT:
                if self.q.shoot(self, x, y, self.player.center_y, self.player.center_x):
                    arcade.play_sound(self.gunSound, volume= .2)
            
            
                
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
       
    def setup(self):
        """
        Setup for before first update cycle
        creates the player object
        """
        self.player = PlayerSprite(const.RESOURCE_PATH + "playerPNG1.png", const.SCALING) 
        self.player.center_x = 3200
        self.player.center_y = 3200
        self.score = 0
        self.playerSprite.append(self.player)     
        self.allSprites.append(self.player)
        self.q = QAbility()
        layer_options = {
            "walls": {
                "use_spatial_hash": True,
            }
        }
        self.tileMap = arcade.load_tilemap(const.RESOURCE_PATH + "background.json", 2, layer_options)
        
        self.scene = arcade.Scene.from_tilemap(self.tileMap)
        self.physicsEngine = arcade.PhysicsEngineSimple(self.player, self.scene["walls"])

        def onEnemyDeath(enemyType):
            """
            Called when an enemy is removed from the sprite list
            adds points to self.score
            number of points added depends on enemy type
            - (1) Standard: 10
            - (2) Sprinter: 15
            - (3) Heavy: 20
            - (4) Shooter: 30
            - (5) Boss: 100
            - (6) Boss shooter: 250
            """

            standardPoints = 10
            sprinterPoints = 15
            heavyPoints = 20
            shooterPoints = 30
            bossPoints = 100
            bossShooterPoints = 250
            defaultPoints = 0

            if (enemyType == 1):
                self.score += standardPoints
            elif (enemyType == 2):
                self.score += sprinterPoints
            elif (enemyType == 2):
                self.score += heavyPoints
            elif (enemyType == 3):
                self.score += shooterPoints
            elif (enemyType == 4):
                self.score += bossPoints
            elif (enemyType == 6):
                self.score += bossShooterPoints
            else:
                self.score += defaultPoints