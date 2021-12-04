from arcade import draw_text
from arcade import draw_circle_filled
from arcade import color
from arcade import load_texture
from arcade import draw_xywh_rectangle_filled
from arcade import draw_lrwh_rectangle_textured
from game import constants as const

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
        draw_xywh_rectangle_filled(director.player.center_x - director.window.width / 2 + 25, director.player.center_y  - 200, 125, 400, color.ARSENIC)
        draw_lrwh_rectangle_textured(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  + 105, 75, 75, load_texture(const.RESOURCE_PATH + "qhudPNG.png"))
        draw_circle_filled(director.player.center_x - director.window.width / 2 + 125, director.player.center_y  + 180, 14, color.GENERIC_VIRIDIAN)
        draw_circle_filled(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  + 180, 14, color.GENERIC_VIRIDIAN)
        draw_text(f"{director.q.shotsLeft[1]}", director.player.center_x - director.window.width / 2 + 125, director.player.center_y  + 180, color.SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        draw_text(f"{director.q.shotsLeft[0]}", director.player.center_x - director.window.width / 2 + 50, director.player.center_y  + 180, color.SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        draw_lrwh_rectangle_textured(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  + 10, 75, 75, load_texture(const.RESOURCE_PATH + "whudPNG.png"), alpha = w)
        draw_lrwh_rectangle_textured(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  - 85, 75, 75, load_texture(const.RESOURCE_PATH + "ehudPNG.png"), alpha = e)
        draw_circle_filled(director.player.center_x - director.window.width / 2 + 125, director.player.center_y  + 85, 14, color.GENERIC_VIRIDIAN)
        draw_text(f"{director.grenade[1]}", director.player.center_x - director.window.width / 2 + 125, director.player.center_y  + 85, color.SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        draw_lrwh_rectangle_textured(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  - 180, 75, 75, load_texture(const.RESOURCE_PATH + "rhudPNG.png"), alpha = r)
        