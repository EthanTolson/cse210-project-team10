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

        
        
    def on_draw(self):
        """
        Draws sprites to screen, also draws health bars and mouse clicks
        """
        arcade.start_render()
        self.tileMap = arcade.load_tilemap(const.RESOURCE_PATH + "background.json", 2)
        self.scene = arcade.Scene.from_tilemap(self.tileMap)
        self.scene.draw()
        arcade.draw_lrtb_rectangle_outline(100,self.window.width-50,(self.window.height - 50),50, color = BLACK)
        arcade.draw_lrwh_rectangle_textured(self.window.width*.22, self.window.height*.25,800,400, texture = self.helpscreen)
        arcade.draw_text("Welcome!", self.window.width*.25, self.window.height*.75, font_size = 120)   
        arcade.draw_text("press enter to begin.", self.window.width*.2, self.window.height*.15, font_size = 75)
        

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Checks for key presses and does corresponding action
        """
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.ENTER: 
            gameView = Director()
            gameView.setup()
            self.window.show_view(gameView)

    def on_resize(self, width: int, height: int):
        """
        Ensures camera works if user resizes screen
        """
        self.camera_sprites.resize(int(width), int(height))

    