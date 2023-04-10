import arcade
from math import cos
from math import sin
from math import radians

class ship:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.length = 50
        self.width = 50
        self.color = arcade.color.AIR_FORCE_BLUE
        self.angle = 0
        self.speed = 0
        self.x_dir = 1
        self.y_dir = 0


        self.width1 = 1000
        self.height1 = 500



    def display(self):
        (x, y) = arcade.rotate_point(self.center_x + self.length/2, self.center_y, self.center_x, self.center_y, self.angle)
        (x1,y1) = arcade.rotate_point(self.center_x - self.length/2, self.center_y - self.width/2, self.center_x, self.center_y, self.angle)
        (x2,y2) = arcade.rotate_point( self.center_x - self.length/2, self.center_y + self.width/2, self.center_x, self.center_y, self.angle)


        arcade.draw_triangle_filled(x, y, x1, y1, x2, y2, self.color)

        self.center_x += self.speed * self.x_dir
        self.center_y += self.speed * self.y_dir


        if self.width1 < self.center_x or self.center_x < 0:
            self.center_x = 500
            self.center_y = 250
        elif self.height1 < self.center_y or self.center_y < 0:
            self.center_x = 500
            self.center_y = 250





    def turn(self, amount):
        self.angle += amount
        self.x_dir = cos(radians(self.angle))
        self.y_dir = sin(radians(self.angle))

    def thrust(self, amountt):
        self.speed += amountt






