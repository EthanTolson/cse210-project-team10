import arcade

class PlayerSprite(arcade.Sprite):

    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.player_hp = 30
        self.enemySprites = None
        self.collision = False

    def update(self):
        super().update()
        if self.enemySprites != None:
            self.collision = self.collides_with_list(self.enemySprites)
        if(self.collision == True):
           self.onHit()

    def setEnemySprites(self, enemy_sprite_list):
        self.enemySprites = enemy_sprite_list

    def getPlayerHealth(self):
        return self.player_hp

    def onHit(self):
        self.player_hp -= 1