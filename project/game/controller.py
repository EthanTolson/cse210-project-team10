import arcade
import time
import math
from game.endScreen import EndScreen
from game.spawnGrenadeSprite import SpawnGrenade


class Controller():
    def keyevent(director, symbol, playerDeath = False):
        if symbol == arcade.key.F:
                    director.window.set_fullscreen(not director.window.fullscreen)
        elif symbol == arcade.key.ESCAPE:
            director.pauseBool = True
            if director.level == 1 and not playerDeath:
                director.level = -1
            director.player.stopFootSteps()
            gameView = EndScreen()
            gameView.setDirector(director)
            director.window.show_view(gameView)
        elif symbol == arcade.key.TAB:
            director.help_bool = not director.help_bool
        elif symbol == arcade.key.P:
            director.pauseBool = not director.pauseBool
        elif symbol == arcade.key.Q:
            director.q.switchStance(director.player)
        elif symbol == arcade.key.E:
            director.doubleDamage[0] = not director.doubleDamage[0]
            if director.doubleDamage[1] != 1:
                director.doubleDamage[1] = time.time()
        elif symbol == arcade.key.R:
            director.ult[0] = not director.ult[0]
            if director.ult[1] != 1:
                director.ult[1] = time.time()
        elif symbol == arcade.key.W:
            director.grenade[0] = not director.grenade[0]

    def keyremoveevent(director, symbol):
        if symbol == arcade.key.TAB:
            director.help_bool = not director.help_bool
    
    def mouseevent(director, x, y, button):
        x = x + director.player.center_x - director.window.width/2
        y = y + director.player.center_y - director.window.height/2
        
        if not director.pauseBool:
            
            if button == arcade.MOUSE_BUTTON_RIGHT:
                #These if statements prevent wall kiting
                if x < 170:
                    x = 170
                elif x > 6040:
                    x = 6040

                if y < 170:
                    y = 170
                elif y > 6230:
                    y = 6230

                director.player.movement(x,y)
                director.lastEventY = y
                director.lastEventX = x

            director.player.angle = math.atan2(y - director.player.center_y, x - director.player.center_x) * 180 / math.pi
            
            #Spawns the projectiles
            if button == arcade.MOUSE_BUTTON_LEFT and not director.grenade[0]:
                if director.q.shoot(director, x, y, director.player.center_y, director.player.center_x):
                    if director.q.getStance() == 0:
                        arcade.play_sound(director.gunSound, volume= .2)
                    else:
                        arcade.play_sound(director.shotgunSound, volume= .25)
                if director.doubleDamage[0] and director.doubleDamage[1] != 1:
                    director.q.shoot(director, x, y, director.player.center_y, director.player.center_x)
                    if director.q.shotsLeft[director.q.stance] != 0:
                        director.q.shotsLeft[director.q.stance] += 1
            elif button == arcade.MOUSE_BUTTON_LEFT and director.grenade[0] and director.grenade[1] > 0:
                director.grenade[1] -= 1
                SpawnGrenade.spawnGrenade(director, x, y)
                director.grenade[0] = False