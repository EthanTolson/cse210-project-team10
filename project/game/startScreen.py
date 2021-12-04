from arcade import View, Camera, load_tilemap, load_texture, Scene, Sprite, start_render, draw_text, draw_lrtb_rectangle_outline, draw_lrwh_rectangle_textured, close_window
from arcade.key import F, ESCAPE, TAB, ENTER
from arcade.color import BLACK, RED_DEVIL
from game.constants import RESOURCE_PATH, SCALING
from game.director import Director
from game.backgroundMusic import BackgroundMusic

"""
startScreen Class:
creates a user friendly starting screen.

Attributes:
    
"""

class StartScreen(View):
    def __init__(self):
        super().__init__()
        self.camera_sprites = Camera(self.window.width, self.window.height)
        self.helpscreen = load_texture(RESOURCE_PATH + "helpPNG.png")
        self.tileMap = load_tilemap(RESOURCE_PATH + "background.json", 2)
        self.scene = Scene.from_tilemap(self.tileMap)
        self.player = Sprite(RESOURCE_PATH + "playerPNG1.png", SCALING)
        self.player.center_x = 1600
        self.player.center_y = 1600
        self.i = 0
        self.j = 0
        self.k = 0
        self.instructions = False
        self.music = BackgroundMusic()
        self.music.play(0)

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
        start_render()
        self.scene.draw()
        self.camera_sprites.use()
        self.player.draw()

        playerx, playery = self.player.center_x, self.player.center_y
        width, height = self.window.width / 2, self.window.height / 2
        playeroffsetx = playerx - 2

        draw_lrtb_rectangle_outline(playerx - width + 100, playerx + width - 100, playery + height - 100, playery - height + 100,  color = BLACK, border_width = 20)
        draw_text("Zombie Shooter", playeroffsetx, playery + 60, font_size = 120, anchor_x = "center", color = BLACK)   
        draw_text("Press Enter to Begin", playeroffsetx, playery - 200, font_size = 75, anchor_x = "center", color = BLACK)
        draw_text("Tab: Controls", playeroffsetx, playery - 300, font_size = 50, anchor_x = "center", color = BLACK)
        draw_text("Zombie Shooter", playerx, playery + 60, font_size = 120, anchor_x = "center", color = RED_DEVIL)   
        draw_text("Press Enter to Begin", playerx, playery - 200, font_size = 75, anchor_x = "center", color = RED_DEVIL)
        draw_text("Tab: Controls", playerx, playery - 300, font_size = 50, anchor_x = "center", color = RED_DEVIL)

        if self.instructions:
            draw_lrwh_rectangle_textured(playerx - 300, playery - 300, 600, 600, self.helpscreen)
    
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
        if symbol == F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == ESCAPE:
            close_window()
        elif symbol == TAB:
            self.instructions = not self.instructions
        elif symbol == ENTER: 
            self.music.play(1)
            gameView = Director()
            gameView.setup(self.music)
            self.window.show_view(gameView)

    def on_resize(self, width: int, height: int):
        """
        Ensures camera works if user resizes screen
        """
        self.camera_sprites.resize(int(width), int(height))

    