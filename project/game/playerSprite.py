import arcade

class PlayerSprite(arcade.Sprite):

    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.player_hp = 3
        self.enemySprites = None
        self.collision = False

    def update(self, enemySpriteList):
        super().update()
        self.enemySprites = enemySpriteList
        self.collision = arcade.check_for_collision_with_list(self.enemySprites)
        if(self.collision == True):
           self.onHit()

    def onHit(self):
        self.player_hp -= 1