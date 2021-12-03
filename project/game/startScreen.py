from arcade.color import BLACK
from game.director import Director
import arcade
from game import constants as const

"""
startScreen Class:
creates a user friendly starting screen.

Attributes:
    
"""

class StartScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.camera_sprites = arcade.Camera(self.window.width, self.window.height)
        self.helpscreen = arcade.load_texture(const.RESOURCE_PATH + "helpPNG.png")
        self.tileMap = arcade.load_tilemap(const.RESOURCE_PATH + "background.json", 2)
        self.scene = arcade.Scene.from_tilemap(self.tileMap)
        self.player = arcade.Sprite(const.RESOURCE_PATH + "playerPNG1.png", const.SCALING)
        self.player.center_x = 1600
        self.player.center_y = 1600
        self.i = 0
        self.j = 0
        self.k = 0
        self.instructions = False

    def on_update(self, delta_time: float):
        self.mapViewLoop()
        self.scroll_to_player()

    def mapViewLoop(self):
        if self.player.center_y < 4800 and self.i < 1:
            self.player.center_y += 4
            self.player.angle = 90
            if self.player.center_y + 4 > 4800:
                self.i += 1
        elif self.player.center_x < 4800 and self.j < 1:
            self.player.center_x += 4
            self.player.angle = 0
            if self.player.center_x + 4 > 4800:
                self.j += 1
        elif self.player.center_y > 1600 and self.k < 1:
            self.player.center_y -= 4
            self.player.angle = -90
            if self.player.center_y - 4 < 1600:
                self.k += 1
        elif self.player.center_x > 1600:
            self.player.angle = 180
            self.player.center_x -= 4
        else:
            self.i, self.j, self.k = 0, 0, 0

    def on_draw(self):
        """
        Draws sprites to screen, also draws health bars and mouse clicks
        """
        arcade.start_render()
        self.scene.draw()
        self.camera_sprites.use()
        self.player.draw()
        arcade.draw_lrtb_rectangle_outline(self.player.center_x -self.window.width /2 + 100, self.player.center_x + self.window.width /2 - 100, self.player.center_y + self.window.height /2 - 100, self.player.center_y - self.window.height /2 + 100,  color = BLACK, border_width= 20)
        arcade.draw_text("Zombie Shooter", self.player.center_x, self.player.center_y + 60, font_size = 120, anchor_x = "center")   
        arcade.draw_text("Press Enter to Begin", self.player.center_x, self.player.center_y - 200, font_size = 75, anchor_x="center")
        arcade.draw_text("Tab: Controls", self.player.center_x, self.player.center_y - 300, font_size = 50, anchor_x="center")
        if self.instructions:
            arcade.draw_lrwh_rectangle_textured(self.player.center_x - 300, self.player.center_y - 300, 600, 600, self.helpscreen)
        
    def scroll_to_player(self):
        """
        Moves the camera center to the player to ensure player does not move off screen
        """
        position = self.player.center_x - self.window.width / 2, \
            self.player.center_y - self.window.height / 2
        self.camera_sprites.move_to(position, 1)

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Checks for key presses and does corresponding action
        """
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.TAB:
            self.instructions = not self.instructions
        elif symbol == arcade.key.ENTER: 
            gameView = Director()
            gameView.setup()
            self.window.show_view(gameView)

    def on_resize(self, width: int, height: int):
        """
        Ensures camera works if user resizes screen
        """
        self.camera_sprites.resize(int(width), int(height))

    