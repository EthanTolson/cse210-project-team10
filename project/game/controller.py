from time import time
from math import atan2, pi
from arcade import MOUSE_BUTTON_RIGHT, MOUSE_BUTTON_LEFT, play_sound
from arcade.key import F, ESCAPE, TAB, P, Q, E, R, W
from game.endScreen import EndScreen
from game.spawnGrenadeSprite import SpawnGrenade


class Controller():
    def keyevent(director, symbol, playerDeath = False):
        if symbol == F:
            director.window.set_fullscreen(not director.window.fullscreen)
        elif symbol == ESCAPE:
            director.pauseBool = True
            if director.level == 1 and not playerDeath:
                director.level = -1
            director.player.stopFootSteps()
            gameView = EndScreen()
            gameView.setDirector(director)
            director.window.show_view(gameView)
        elif symbol == TAB:
            director.help_bool = not director.help_bool
        elif symbol == P:
            director.pauseBool = not director.pauseBool
        elif symbol == Q:
            director.q.switchStance(director.player)
        elif symbol == E:
            director.doubleDamage[0] = not director.doubleDamage[0]
            if director.doubleDamage[1] != 1:
                director.doubleDamage[1] = time()
        elif symbol == R:
            director.ult[0] = not director.ult[0]
            if director.ult[1] != 1:
                director.ult[1] = time()
        elif symbol == W:
            director.grenade[0] = not director.grenade[0]

    def keyremoveevent(director, symbol):
        if symbol == TAB:
            director.help_bool = not director.help_bool
    
    def mouseevent(director, x, y, button):
        playerx = director.player.center_x
        playery = director.player.center_y
        x = x + playerx - director.window.width/2
        y = y + playery - director.window.height/2
        
        if not director.pauseBool:
            
            if button == MOUSE_BUTTON_RIGHT:
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

            director.player.angle = atan2(y - playery, x - playerx) * 180 / pi
            
            #Spawns the projectiles
            if button == MOUSE_BUTTON_LEFT and not director.grenade[0]:
                q = director.q
                if q.shoot(director, x, y, playery, playerx):
                    if q.getStance() == 0:
                        play_sound(director.gunSound, volume= .2)
                    else:
                        play_sound(director.shotgunSound, volume= .25)

                if director.doubleDamage[0] and director.doubleDamage[1] != 1:
                    q.shoot(director, x, y, playery, playerx)
                    if q.shotsLeft[q.stance] != 0:
                        q.shotsLeft[q.stance] += 1
                        
            elif button == MOUSE_BUTTON_LEFT and director.grenade[0] and director.grenade[1] > 0:
                director.grenade[1] -= 1
                SpawnGrenade.spawnGrenade(director, x, y)
                director.grenade[0] = False