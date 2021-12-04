from game.grenadeSprite import GrenadeSprite
from math import sqrt, sin, cos, pi

class SpawnGrenade():
    def spawnGrenade(director, x, y):
        playerx, playery = director.player.center_x, director.player.center_y
        distance = sqrt((x - playerx) ** 2 + (y - playery) ** 2)
        offsetangle = director.player.angle + 45.8550973963
        radconversion = pi / 180

        grenade = GrenadeSprite(director)

        grenade.center_x = playerx + sin(radconversion * (offsetangle)) * 33.54 #Calculates the offset for the grenade to come out of the players hand
        grenade.center_y = playery + cos(radconversion * (offsetangle)) * 33.54

        grenade.change_x = 4 * ((x - playerx ) / distance)
        grenade.change_y = 4 * ((y - playery ) / distance)

        director.projectileSprites.append(grenade)
        director.allSprites.append(grenade)