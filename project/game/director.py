from arcade import SpriteList, View, Camera, Sound, Scene, load_texture, start_render, draw_text, draw_lrwh_rectangle_textured, draw_lrtb_rectangle_outline, load_tilemap
from arcade.key import ESCAPE
from arcade.color import GRAPE, BLACK, WHITE
from time import time
from game.constants import RESOURCE_PATH, SCALING
from game.controller import Controller
from game.playerSprite import PlayerSprite
from game.drawHealthbars import DrawHealthBars
from game.hud import drawHUD
from game.spawnEnemies import SpawnEnemies
from game.qAbility import QAbility
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

class Director(View):
    def __init__(self):
        super().__init__()
        self.playerSprite = SpriteList(use_spatial_hash = False)
        self.enemySprites = SpriteList(use_spatial_hash = False)
        self.projectileSprites = SpriteList(use_spatial_hash = False)
        self.allSprites = SpriteList(use_spatial_hash = False)
        self.camera_sprites = Camera(self.window.width, self.window.height)
        self.tileMap = None
        self.level = 0
        self.lastEventX = 0
        self.lastEventY = 0
        self.help_bool = False
        self.pauseBool = False
        self.doubleDamage = [False, 0]
        self.ult = [False, 0]
        self.grenade = [False, 2]
        self.deathsound = Sound(f"{RESOURCE_PATH}zombiedeathsound.mp3")
        self.levelup = Sound(f"{RESOURCE_PATH}levelup.mp3")
        self.gunSound = Sound(f"{RESOURCE_PATH}gunshot.mp3")
        self.shotgunSound = Sound(f"{RESOURCE_PATH}shotgunshot.mp3")
        self.reloadSound = Sound(f"{RESOURCE_PATH}reload.mp3")
        self.helpscreen = load_texture(f"{RESOURCE_PATH}helpPNG.png")        

    def on_update(self, delta_time: float):
        """
        Updates the sprites positions also spawns enemies if there are none
        """ 
        self.player.stopFootSteps()
        if self.doubleDamage[1] + 5 <= time() and self.doubleDamage[1] != 0:
            self.doubleDamage = [False, 1]
        if self.grenade[1] <= 0:
            self.grenade[0] = False
        if not self.pauseBool:
            if self.ult[1] + 1.5 < time() and (self.ult[1] == 0 or self.ult[1] == 1):
                self.ult[0] = False
                self.enemySprites.update()
            elif self.ult[1] + 1.5 > time():
                self.ult[0] = True
                pass
            else:
                self.ult[1] = 1

            self.projectileSprites.update()
            self.playerSprite.update()
            self.scroll_to_player()
            if len(self.enemySprites) == 0 and self.level < 1003:
                if self.level != 0:
                    self.levelup.play(.7)
                self.doubleDamage = [False, 0]
                self.ult = [False, 0]
                if self.level > 25:
                    self.grenade = [False, 6]
                else:
                    self.grenade = [False, 2 + int(self.level/5)]
                self.level += 1
                SpawnEnemies.spawnEnemies(self)
                self.player.setEnemySprites(self.enemySprites)
                if self.level > 1001:
                    Controller.keyevent(self, ESCAPE)
            if self.level % 10 == 0 and self.backgroundmusic.getPlayingID() != 2:
                self.backgroundmusic.play(2)
            elif self.level % 10 != 0 and self.backgroundmusic.getPlayingID() != 1:
                self.backgroundmusic.play(1)
        
    def on_draw(self):
        """
        Draws sprites to screen, also draws health bars and mouse clicks
        """
        start_render()
        self.scene.draw()

        #Healthbars were causing game to lag need to find fix
        #Fix is to only draw healthbars for enemies after they have been hit and only for 1.5 seconds after the hit
        for enemySprite in self.enemySprites:
            if enemySprite.getHealth() < enemySprite.getMaxHealth() and enemySprite.getLastHit() + 1.5 > time():
                DrawHealthBars.drawHealthBars(enemySprite)

        DrawHealthBars.drawHealthBars(self.playerSprite[0])

        draw_text("x", self.lastEventX, self.lastEventY, GRAPE, 10, bold = True)

        self.camera_sprites.use()
        self.allSprites.draw()
        draw_lrtb_rectangle_outline(-500, 6900, 6900, -500, BLACK, 1000)  

        drawHUD.drawHUD(self)

        if self.help_bool or self.pauseBool:
            draw_lrwh_rectangle_textured(self.player.center_x - 300,
            self.player.center_y - 300, 600 , 600, texture = self.helpscreen)

        draw_text(f"Level: {self.level} | Score: {self.score} | Zombies Left: {len(self.enemySprites)} | TAB: Show Controls/Help",
         self.player.center_x - self.window.width/2 + 10, 
         self.player.center_y - self.window.height/2 + 20, 
         WHITE, 14)   

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Checks for key presses and does corresponding action
        """
        Controller.keyevent(self, symbol)


    def on_key_release(self, symbol: int, modifiers: int):
        Controller.keyremoveevent(self, symbol)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """
        Checks for mouse clicks for movement updates player velocity 
        Also checks for mouse clicks for projectiles
        """
        Controller.mouseevent(self, x, y, button)  
                  
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

    def playDeath(self):
        self.deathsound.play(.15)

    def reset(self, music):
        self.playerSprite = SpriteList(use_spatial_hash = False)
        self.enemySprites = SpriteList(use_spatial_hash = False)
        self.projectileSprites = SpriteList(use_spatial_hash = False)
        self.allSprites = SpriteList(use_spatial_hash = False)
        self.camera_sprites = Camera(self.window.width, self.window.height)
        self.level = 0
        self.lastEventX = 0
        self.lastEventY = 0
        self.help_bool = False
        self.pauseBool = False
        self.doubleDamage = [False, 0]
        self.ult = [False, 0]
        self.setup(music)
       
    def setup(self, music):
        """
        Setup for before first update cycle
        creates the player object
        """
        self.player = PlayerSprite(f"{RESOURCE_PATH}playerPNG1.png", SCALING) 
        self.player.center_x = 3200
        self.player.center_y = 3200
        self.score = 0
        self.playerSprite.append(self.player)     
        self.allSprites.append(self.player)
        self.q = QAbility()
        self.tileMap = load_tilemap(f"{RESOURCE_PATH}background.json", 2)
        self.backgroundmusic = music
        self.player.setDirector(self)
        self.scene = Scene.from_tilemap(self.tileMap)