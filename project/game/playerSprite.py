import arcade

class PlayerSprite(arcade.Sprite):

    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.player_hp = 3
        self.enemySprites = None
        self.collision = False

    def update(self):
        super().update()
        self.collision = self.collides_with_list(self.enemySprites)
        if(self.collision == True):
           self.onHit()

    def enemySpriteList(self, enemy_sprite_list):
        self.enemySprites = enemy_sprite_list

    def onHit(self):
        self.player_hp -= 1