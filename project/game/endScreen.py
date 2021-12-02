import arcade
from game import constants as const

class EndScreen(arcade.View):
    def __init__(self):
        super().__init__()
    
    def on_draw(self):
        
        # if not self.running:
        #     return
        #self.screen.fill(255, 0, 0)
        arcade.start_render()
        # arcade.draw_text("GAME OVER", 48, 100, arcade.color.WHITE, const.SCREEN_WIDTH / 2, const.SCREEN_HEIGHT/ 4)
        # arcade.draw_text(f"Score: {str(100)}", 22, 200, arcade.color.WHITE, const.SCREEN_WIDTH / 2, const.SCREEN_HEIGHT/ 2)
        arcade.draw_text("Press a key to play again", 22, 300, arcade.color.WHITE, const.SCREEN_WIDTH / 2)#, const.SCREEN_HEIGHT * 3/4)
        # arcade.display.flip()
        # # self.wait_for_key()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
    
    # def wait_for_key(self):
    #     waiting = True
    #     while waiting:
    #         self.clock.tick(60)
    #         for event in arcade.event.get():
    #             if event.type == arcade.QUIT:
    #                 waiting = False
    #                 self.running = False
    #             if event.type == arcade.KEYUP:
    #                 waiting = False