from arcade import draw_rectangle_filled, draw_text
from arcade.color import WHITE, GREEN, RED
from game.constants import HEALTHBAR_HEIGHT, HEALTHBAR_OFFSET_Y, HEALTHBAR_WIDTH

class DrawHealthBars():
    
    def drawHealthBars(sprite):
        """
        Method for drawing health bars above enemies and player separated from on draw due to being repeated
        """
        y = sprite.center_y + HEALTHBAR_OFFSET_Y * sprite.scale
        x = sprite.center_x
        spritehealth = sprite.getHealth()
        spritemaxhealth = sprite.getMaxHealth()
        health_width = HEALTHBAR_WIDTH * (spritehealth / spritemaxhealth)

        if spritehealth < spritemaxhealth:
            draw_rectangle_filled(center_x = x,
                    center_y = y,
                    width = HEALTHBAR_WIDTH,
                    height = HEALTHBAR_HEIGHT * 2 / 3,
                    color = RED)

        if spritehealth >= 0:
            draw_rectangle_filled(center_x = x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                        center_y = y,
                        width = health_width,
                        height = HEALTHBAR_HEIGHT,
                        color = GREEN)

            draw_text(f"{spritehealth}/{spritemaxhealth}",
                        start_x = x,
                        start_y = y,
                        font_size = 12,
                        color = WHITE, anchor_x = "center")