import arcade

HEALTHBAR_WIDTH = 50
HEALTHBAR_HEIGHT = 6
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25

class SpriteHealth(arcade.Sprite):
    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)

        
        self.max_health = max_health
        self.cur_health = max_health

    def draw_health_number(self):

        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                        start_x=self.center_x + HEALTH_NUMBER_OFFSET_X,
                        start_y=self.center_y + HEALTH_NUMBER_OFFSET_Y,
                        font_size=12,
                        color=arcade.color.WHITE)

    def draw_health_bar(self):
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                        center_y=self.center_y + HEALTHBAR_OFFSET_Y,
                                        width=HEALTHBAR_WIDTH,
                                        height=3,
                                        color=arcade.color.RED)

        health_width = HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                                    center_y=self.center_y - 10,
                                    width=health_width,
                                    height=HEALTHBAR_HEIGHT,
                                    color=arcade.color.GREEN)
