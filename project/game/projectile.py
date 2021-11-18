import arcade
import playerSprite

class ProjectileSprite(arcade.Sprite):
    def __init__(self, filename, scaling, spawn_x, spawn_y):
        super().__init__(filename, scaling)

        self.sprite = arcade.Sprite("", scaling)

        self.destinaion = ""
        self.speed = 100 # change as needed, 100 is not a special number

        #vector is made from source, destination, and speed.
        self.vector = super().velocity

    def update(self):
        super().__init__()

        # moves according to vecto

        # executes onHit() if it hits something
        if self.collides_with_sprite("""enemy"""):
            self.onHit()

    def onHit(self):
        """
        deletes projectile
        """
        self.remove_from_sprite_lists()