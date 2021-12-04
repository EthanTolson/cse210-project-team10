from arcade import Window
from arcade import set_background_color, run
from arcade.color import ARSENIC
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from game.startScreen import StartScreen

def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable = True, fullscreen = True)
    set_background_color(ARSENIC)
    gameView = StartScreen()
    window.show_view(gameView)
    run()
            
if __name__ == "__main__":
    main()