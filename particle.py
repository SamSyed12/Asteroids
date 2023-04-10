import arcade


class torpedo:
    def __init__(self, x, y, speed, size, x_dir, y_dir, color):
        self.center_x = x
        self.center_y = y
        self.speed = speed
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.size = size
        self.color = color
        self.life = 255





    def display(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y, self.size, self.size,
                                       self.color + (self.life,))

        self.center_x += self.speed * self.x_dir
        self.center_y += self.speed * self.y_dir

    def transparent(self, amount):
        self.life -= amount
















