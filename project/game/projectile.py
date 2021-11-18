import arcade

class ProjectileSprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.destinaion = ""
        self.speed = 100 # change as needed, 100 is not a special number
        self.enemySprites = None
        #vector is made from source, destination, and speed.

    def update(self):
        super().__init__()

        # moves according to vecto

        # executes onHit() if it hits something
        if self.collides_with_list(self.enemySprites):
            self.onHit()

    def onHit(self):
        """
        deletes projectile
        """

        self.remove_from_sprite_lists()

    def set_enemysprites(self, enemylist):
        self.enemySprites = enemylist