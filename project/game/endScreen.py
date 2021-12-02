import arcade
from arcade.color import RED_DEVIL
from game import constants as const

class EndScreen(arcade.View):

    def __init__(self):
        super().__init__()
        self.camera_sprites = arcade.Camera(self.window.width, self.window.height)
        self.director = None
        
    def on_update(self, delta_time: float):
        self.scroll_to_start

    def scroll_to_start(self):
        self.camera_sprites.move_to((0,0), 1)

    def on_draw(self):
        """
        Draws sprites to screen, also draws health bars and mouse clicks
        """
        arcade.start_render()
        self.camera_sprites.use()
        arcade.draw_lrtb_rectangle_outline(200,(self.window.width - 200),(self.window.height - 200),200, color = RED_DEVIL)
        arcade.draw_text("GAME OVER", self.window.width*.25, self.window.height*.6, font_size = 100)   
        arcade.draw_text("press enter to begin.", self.window.width*.2, self.window.height*.3, font_size = 75)

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Checks for key presses and does corresponding action
        """
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.ENTER: 
            self.director.reset()
            self.window.show_view(self.director)
            
    def setDirector(self, director):
        self.director = director

    def on_resize(self, width: int, height: int):
        """
        Ensures camera works if user resizes screen
        """
        self.camera_sprites.resize(int(width), int(height))

    