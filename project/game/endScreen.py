import arcade

class EndScreen(arcade.View):
    def __init__(self):
        super().__init__()
    
    def game_over(self):
        WHITE = (255, 255, 255)
        WIDTH = 800
        HEIGHT = 600

        if not self.running:
            return
        self.screen.fill(255, 0, 0)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        arcade.display.flip()
        self.wait_for_key()
    
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in arcade.event.get():
                if event.type == arcade.QUIT:
                    waiting = False
                    self.running = False
                if event.type == arcade.KEYUP:
                    waiting = False