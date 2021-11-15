import arcade
import math
from game import constants as const
from game.playerSprite import PlayerSprite
from game.enemysprite import EnemySprite
from game.projectile import ProjectileSprite

class Director(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.start_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()
