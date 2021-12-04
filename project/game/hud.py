import arcade
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
        arcade.draw_xywh_rectangle_filled(director.player.center_x - director.window.width / 2 + 25, director.player.center_y  - 200, 125, 400, arcade.color.ARSENIC)
        arcade.draw_lrwh_rectangle_textured(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  + 105, 75, 75, arcade.load_texture(const.RESOURCE_PATH + "qhudPNG.png"))
        arcade.draw_circle_filled(director.player.center_x - director.window.width / 2 + 125, director.player.center_y  + 180, 14, arcade.color.GENERIC_VIRIDIAN)
        arcade.draw_circle_filled(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  + 180, 14, arcade.color.GENERIC_VIRIDIAN)
        arcade.draw_text(f"{director.q.shotsLeft[1]}", director.player.center_x - director.window.width / 2 + 125, director.player.center_y  + 180, arcade.color.SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        arcade.draw_text(f"{director.q.shotsLeft[0]}", director.player.center_x - director.window.width / 2 + 50, director.player.center_y  + 180, arcade.color.SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        arcade.draw_lrwh_rectangle_textured(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  + 10, 75, 75, arcade.load_texture(const.RESOURCE_PATH + "whudPNG.png"), alpha = w)
        arcade.draw_lrwh_rectangle_textured(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  - 85, 75, 75, arcade.load_texture(const.RESOURCE_PATH + "ehudPNG.png"), alpha = e)
        arcade.draw_circle_filled(director.player.center_x - director.window.width / 2 + 125, director.player.center_y  + 85, 14, arcade.color.GENERIC_VIRIDIAN)
        arcade.draw_text(f"{director.grenade[1]}", director.player.center_x - director.window.width / 2 + 125, director.player.center_y  + 85, arcade.color.SMOKY_BLACK, 14, anchor_x = "center", anchor_y = "center")
        arcade.draw_lrwh_rectangle_textured(director.player.center_x - director.window.width / 2 + 50, director.player.center_y  - 180, 75, 75, arcade.load_texture(const.RESOURCE_PATH + "rhudPNG.png"), alpha = r)
        