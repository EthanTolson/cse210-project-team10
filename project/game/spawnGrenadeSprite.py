from game.grenadeSprite import GrenadeSprite
from math import sqrt
from math import sin
from math import cos
from math import pi

class SpawnGrenade():
    def spawnGrenade(director, x, y):
        grenade = GrenadeSprite(director)
        grenade.center_x = director.player.center_x + sin(pi/180 * (director.player.angle + 45.8550973963)) * 33.54 #Calculates the offset for the grenade to come out of the players hand
        grenade.center_y = director.player.center_y + cos(pi/180 * (director.player.angle + 45.8550973963)) * 33.54

        grenade.change_x = 4 * ((x - director.player.center_x ) / sqrt((x-director.player.center_x)**2 + (y- director.player.center_y)**2))
        grenade.change_y = 4 * ((y - director.player.center_y ) / sqrt((x-director.player.center_x)**2 + (y- director.player.center_y)**2))

        director.projectileSprites.append(grenade)
        director.allSprites.append(grenade)