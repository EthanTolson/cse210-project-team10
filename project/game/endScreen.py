import arcade
from arcade.color import RED_DEVIL
from game import constants as const

class EndScreen(arcade.View):

    def __init__(self):
        super().__init__()
        self.camera_sprites = arcade.Camera(self.window.width, self.window.height)
        self.director = None
        self.texture = arcade.load_texture(const.RESOURCE_PATH + "game_over.png")
        
    def on_update(self, delta_time: float):
        if self.director.backgroundmusic.getPlayingID() != 3:
            self.director.backgroundmusic.play(3)
        self.scroll_to_start

    def scroll_to_start(self):
        self.camera_sprites.move_to((0,0), 1)

    def on_draw(self):
        """
        Draws sprites to screen, also draws health bars and mouse clicks
        """
        arcade.start_render()
        self.camera_sprites.use()
        arcade.draw_lrtb_rectangle_outline(200,(self.window.width - 200),(self.window.height - 200),200, color = RED_DEVIL, border_width = 1000)
        arcade.draw_lrwh_rectangle_textured(200, 200, self.window.width - 400, self.window.height - 400, self.texture)
        arcade.draw_text("Press Enter to Retry", self.window.width/2 , self.window.height / 2 - 100, font_size = 75, anchor_x = "center")
        arcade.draw_text("Esc: Quit Game", self.window.width/2 , self.window.height / 2 - 200, font_size = 75, anchor_x = "center")

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Checks for key presses and does corresponding action
        """
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.ENTER:
            self.director.backgroundmusic.play(1)
            self.director.reset(self.director.backgroundmusic)
            self.window.show_view(self.director)
            
    def setDirector(self, director):
        self.director = director
        #director.backgroundmusic.play(3)

    def on_resize(self, width: int, height: int):
        """
        Ensures camera works if user resizes screen
        """
        self.camera_sprites.resize(int(width), int(height))

    