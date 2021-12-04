from arcade import load_texture
from arcade import play_sound
from math import sqrt
from math import atan2
from math import sin
from math import cos
from game import constants as const
from game.spawnProjectiles import SpawnProjectiles

class QAbility():
    def __init__(self):
        self.stance = 0
        self.shotsLeft = [30, 20]

    def switchStance(self, player):

        if self.stance != 1:
            self.stance += 1
            texture = load_texture(const.RESOURCE_PATH + f"playerPNG{self.stance + 1}.png")
            player.texture = texture

        else:
            self.stance = 0
            texture = load_texture(const.RESOURCE_PATH + f"playerPNG{self.stance + 1}.png")
            player.texture = texture

    def getShotsLeft(self):
        return int(self.shotsLeft[self.stance])

    def shoot(self, director, x, y, playery = 0, playerx = 0):
        if self.shotsLeft[0] == 0:
            play_sound(director.reloadSound , .4)
            self.shotsLeft = [30, 20]

        
        if self.shotsLeft[self.stance] != 0:
            if self.stance == 0:
                SpawnProjectiles.spawnProjectiles(director, x, y)
                self.shotsLeft[self.stance] -= 1
                return True
            elif self.stance == 1:
                SpawnProjectiles.spawnProjectiles(director, x, y)
                SpawnProjectiles.spawnProjectiles(director, cos( atan2(y - playery, x - playerx) + .26799) * sqrt((x - playerx)**2 + (y - playery)**2) + playerx, sin( atan2(y - playery, x - playerx) + .26799) * sqrt((x - playerx)**2 + (y - playery)**2)+ playery)
                SpawnProjectiles.spawnProjectiles(director, cos( atan2(y - playery, x - playerx) - .26799) * sqrt((x - playerx)**2 + (y - playery)**2) + playerx, sin( atan2(y - playery, x - playerx) - .26799) * sqrt((x - playerx)**2 + (y - playery)**2)+ playery)
                self.shotsLeft[self.stance] -= 1
                return True
        else:
            return False

    def getStance(self):
        return self.stance