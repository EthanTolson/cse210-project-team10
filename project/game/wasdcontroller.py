from time import time
from math import atan2, pi
from arcade import MOUSE_BUTTON_LEFT, play_sound
from arcade.key import F, ESCAPE, TAB, P, Q, E, R, W, A, S, D, T
from game.endScreen import EndScreen
from game.spawnGrenadeSprite import SpawnGrenade


class WASDController():
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
            director.grenade[0] = not director.grenade[0]
        elif symbol == R:
            director.doubleDamage[0] = not director.doubleDamage[0]
            if director.doubleDamage[1] != 1:
                director.doubleDamage[1] = time()
        elif symbol == W:
            director.wBool = 1
            director.sBool = 0
            WASDController.angle(director)
        elif symbol == A:
            director.aBool = 1
            director.dBool = 0
            WASDController.angle(director)
        elif symbol == S:
            director.sBool = 1
            director.wBool = 0
            WASDController.angle(director)
        elif symbol == D:
            director.dBool = 1
            director.aBool = 0
            WASDController.angle(director)
        elif symbol == T:
            director.ult[0] = not director.ult[0]
            if director.ult[1] != 1:
                director.ult[1] = time()

    def keyremoveevent(director, symbol):
        if symbol == TAB:
            director.help_bool = not director.help_bool
        elif symbol == W:
            director.wBool = 0
            WASDController.angle(director)
            director.player.change_y = 0
        elif symbol == A:
            director.aBool = 0
            WASDController.angle(director)
            director.player.change_x = 0
        elif symbol == S:
            director.sBool = 0
            WASDController.angle(director)
            director.player.change_y = 0
        elif symbol == D:
            director.dBool = 0
            WASDController.angle(director)
            director.player.change_x = 0
    
    def mouseevent(director, x, y, button):
        playerx = director.player.center_x
        playery = director.player.center_y
        x = x + playerx - director.window.width/2
        y = y + playery - director.window.height/2
        
        if not director.pauseBool:          
            #Spawns the projectiles
            if button == MOUSE_BUTTON_LEFT and not director.grenade[0]:
                director.player.angle = atan2(y - playery, x - playerx) * 180 / pi
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
                director.player.angle = atan2(y - playery, x - playerx) * 180 / pi
                director.grenade[1] -= 1
                SpawnGrenade.spawnGrenade(director, x, y)
                director.grenade[0] = False

    def angle(director):
        if director.wBool and director.dBool:
            director.player.change_y = 3
            director.player.change_x = 3
            director.player.angle = 45
        elif director.wBool and director.aBool:
            director.player.change_y = 3
            director.player.change_x = -3
            director.player.angle = 135
        elif director.sBool and director.dBool:
            director.player.change_y = -3
            director.player.change_x = 3
            director.player.angle = -45
        elif director.sBool and director.aBool:
            director.player.change_y = -3
            director.player.change_x = -3
            director.player.angle = -135
        elif director.wBool and not director.dBool:
            director.player.change_y = 4.24
            director.player.angle = 90
        elif director.sBool and not director.aBool:
            director.player.change_y = -4.24
            director.player.angle = -90
        elif not director.wBool and director.dBool:
            director.player.change_x = 4.24
            director.player.angle = 0
        elif not director.sBool and director.aBool:
            director.player.change_x = -4.24
            director.player.angle = 180