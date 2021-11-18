import arcade

class PlayerSprite(arcade.Sprite):

    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.player_hp = 30
        self.enemySprites = None
        self.collision = False
        self.lastEventX = None
        self.lastEventY = None

    def update(self):
        super().update()

        for i in range(0, 6):
            if self.lastEventX != None and (self.lastEventX <= self.center_x + i and self.lastEventX \
                >= self.center_x - i) and(self.lastEventY <= self.center_y + i and self.lastEventY \
                    >= self.center_y - i):
                self.change_x = 0
                self.change_y = 0
        if self.enemySprites != None:
            self.collision = self.collides_with_list(self.enemySprites)
        if(self.collision == True):
           self.onHit()

    def setEnemySprites(self, enemy_sprite_list):
        self.enemySprites = enemy_sprite_list

    def getHealth(self):
        return self.player_hp

    def getMaxHealth(self):
        return 30

    def onHit(self):
        self.player_hp -= 3