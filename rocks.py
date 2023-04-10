import arcade
from random import randint
from random import uniform
from ship import ship

class rocks:
    def __init__(self, x, y, width, height):
        self.center_x = x
        self.center_y = y
        self.color = arcade.color.BATTLESHIP_GREY
        self.speed = 2
        self.x_dir = uniform(-1,1)
        self.y_dir = uniform(-1,1)
        self.width1 = 1000
        self.height1 = 500
        self.width = width
        self.height = height

    def display(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y, self.width ,self.height , self.color)
        self.center_x += self.speed * self.x_dir
        self.center_y += self.speed * self.y_dir

        if self.center_x > self.width1:
            self.center_x = 0
        elif self.center_x < 0:
            self.center_x = self.width1
        if self.center_y > self.height1:
            self.center_y = 0
        elif self.center_y < 0:
            self.center_y = self.height1









