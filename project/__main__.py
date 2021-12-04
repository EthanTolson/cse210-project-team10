from arcade import Window
from arcade import set_background_color
from arcade.color import ARSENIC
from arcade import run
from game import constants as const
from game.startScreen import StartScreen

def main():
    window = Window(const.SCREEN_WIDTH, const.SCREEN_WIDTH, const.SCREEN_TITLE, resizable = True, fullscreen = True)
    set_background_color(ARSENIC)
    gameView = StartScreen()
    window.show_view(gameView)
    run()
            
if __name__ == "__main__":
    main()