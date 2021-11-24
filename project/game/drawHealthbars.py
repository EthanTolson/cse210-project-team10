import arcade
from game import constants as const

class DrawHealthBars():
    
    def drawHealthBars(sprite):
        """
        Method for drawing health bars above enemies and player separated from on draw due to being repeated
        """
        health_width = const.HEALTHBAR_WIDTH * (sprite.getHealth() / sprite.getMaxHealth())
        if sprite.getHealth() < sprite.getMaxHealth():
            arcade.draw_rectangle_filled(center_x = sprite.center_x,
                    center_y=sprite.center_y + const.HEALTHBAR_OFFSET_Y * sprite.scale,
                    width=const.HEALTHBAR_WIDTH,
                    height=const.HEALTHBAR_HEIGHT * 2 / 3,
                    color=arcade.color.RED)
        arcade.draw_rectangle_filled(center_x=sprite.center_x - 0.5 * \
                    (const.HEALTHBAR_WIDTH - health_width),
                    center_y=sprite.center_y + const.HEALTHBAR_OFFSET_Y * sprite.scale,
                    width=health_width,
                    height=const.HEALTHBAR_HEIGHT,
                    color=arcade.color.GREEN)
        arcade.draw_text(f"{sprite.getHealth()}/{sprite.getMaxHealth()}",
                    start_x=sprite.center_x,
                    start_y=sprite.center_y + const.HEALTHBAR_OFFSET_Y * sprite.scale,
                    font_size=12,
                    color=arcade.color.WHITE, anchor_x="center")