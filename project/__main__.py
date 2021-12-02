import arcade
from game import constants as const
from game.startScreen import StartScreen

def main():
    window = arcade.Window(const.SCREEN_WIDTH, const.SCREEN_WIDTH, const.SCREEN_TITLE, resizable = True, fullscreen = True)
    arcade.set_background_color(arcade.color.ARSENIC)
    gameView = StartScreen()
    window.show_view(gameView)
    arcade.run()
            
if __name__ == "__main__":
    main()