from arcade import View, Camera, load_texture, start_render, draw_text, draw_lrtb_rectangle_outline, draw_lrwh_rectangle_textured, close_window
from arcade.key import ESCAPE, ENTER, F
from arcade.color import RED_DEVIL, BLACK
from game.constants import RESOURCE_PATH

class EndScreen(View):

    def __init__(self):
        super().__init__()
        self.camera_sprites = Camera(self.window.width, self.window.height)
        self.director = None
        self.texture = load_texture("".join([RESOURCE_PATH, "game_over.png"]))
        
    def on_update(self, delta_time: float):
        level = self.director.level
        music = self.director.backgroundmusic
        if (level >= 500 or level == 1) and music.getPlayingID() != 4:
            music.play(4)
        elif level < 500 and level != 1 and music.getPlayingID() != 3:
            music.play(3)
        self.scroll_to_start

    def scroll_to_start(self):
        self.camera_sprites.move_to((0,0), 1)

    def on_draw(self):
        """
        Draws sprites to screen, also draws health bars and mouse clicks
        """
        width = self.window.width
        height = self.window.height
        x = width / 2
        offx = width / 2 -3
        y = height / 2
        score = self.director.score
        level = self.director.level

        start_render()
        self.camera_sprites.use()
        draw_lrtb_rectangle_outline(200, (width - 200), (height - 200), 200, color = RED_DEVIL, border_width = 1000)
        draw_lrwh_rectangle_textured(200, 200, width - 400, height - 400, self.texture)
        draw_text("Press Enter to Retry", offx, y - 200, font_size = 75, anchor_x = "center", color = BLACK)
        draw_text("Esc: Quit Game", offx, y - 300, font_size = 75, anchor_x = "center", color = BLACK)
        draw_text(f"Score: {score}", offx, y + 200, font_size = 75, anchor_x = "center", color = BLACK)
        draw_text(f"Level: {abs(level)}", offx, y + 300, font_size = 75, anchor_x = "center", color = BLACK)
        draw_text("Press Enter to Retry", x, y - 200, font_size = 75, anchor_x = "center")
        draw_text("Esc: Quit Game", x, y - 300, font_size = 75, anchor_x = "center")
        draw_text(f"Score: {score}", x, y + 200, font_size = 75, anchor_x = "center")
        draw_text(f"Level: {abs(level)}", x, y + 300, font_size = 75, anchor_x = "center")

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Checks for key presses and does corresponding action
        """
        if symbol == F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == ESCAPE:
            close_window()
        elif symbol == ENTER:
            self.director.backgroundmusic.play(1)
            self.director.reset(self.director.backgroundmusic)
            self.window.show_view(self.director)
            
    def setDirector(self, director):
        self.director = director

    def on_resize(self, width: int, height: int):
        """
        Ensures camera works if user resizes screen
        """
        self.camera_sprites.resize(int(width), int(height))

    