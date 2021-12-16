from arcade import draw_text, draw_circle_filled, load_texture, draw_xywh_rectangle_filled, draw_lrwh_rectangle_textured
from arcade.color import ARSENIC, GENERIC_VIRIDIAN, SMOKY_BLACK
from game.constants import RESOURCE_PATH

class drawHUD():
    def drawHUD(director = None):
        if director.grenade[0]:
            w = 125
        else:
            w = 255
        if director.doubleDamage[0]:
            e = 125
        else:
            e = 255
        if director.ult[0]:
            r = 125
        else:
            r = 255
        playery = director.player.center_y
        x = director.player.center_x - director.window.width / 2
        draw_xywh_rectangle_filled(x + 25, playery - 200, 125, 400, ARSENIC)
        draw_lrwh_rectangle_textured(x + 50, playery + 105, 75, 75, load_texture(f"{RESOURCE_PATH}qhudPNG.png"))
        draw_circle_filled(x + 125, playery + 180, 14, GENERIC_VIRIDIAN)
        draw_circle_filled(x + 50, playery + 180, 14, GENERIC_VIRIDIAN)
        draw_text(f"{director.q.shotsLeft[1]}", x + 125, playery + 180, SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        draw_text(f"{director.q.shotsLeft[0]}", x + 50, playery + 180, SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        draw_lrwh_rectangle_textured(x + 50, playery + 10, 75, 75, load_texture(f"{RESOURCE_PATH}wasdehudPNG.png"), alpha = w)
        draw_lrwh_rectangle_textured(x + 50, playery - 85, 75, 75, load_texture(f"{RESOURCE_PATH}wasdrhudPNG.png"), alpha = e)
        draw_circle_filled(x + 125, playery + 85, 14, GENERIC_VIRIDIAN)
        draw_text(f"{director.grenade[1]}", x + 125, playery + 85, SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        draw_lrwh_rectangle_textured(x + 50, playery - 180, 75, 75, load_texture(f"{RESOURCE_PATH}wasdthudPNG.png"), alpha = r)
        