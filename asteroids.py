import arcade
from ship import ship
from random import randint
from rocks import rocks
from particle import torpedo
from math import cos
from math import sin
from math import radians
from random import uniform
from Highscore import Highscore





class Asteroids(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        self.name = ""
        self.center_x = 500
        self.center_y = 500
        self.ship= ship(randint(400, 600), randint(200, 300))
        self.turn_left = False
        self.turn_right = False
        self.shoot = True
        self.thrust = False
        self.alive = True
        self.restart = False
        self.score = 0
        self.torpedo_list = []
        self.particle_system_list = []
        self.rocks_list= []
        self.ship_display = True
        self.particle_list_ship_collision = []
        self.name_enter = True
        self.score_list = []
        self.begin = False
        try:
            highscore_file = open("scores.txt", "r")
            for line in highscore_file:
               self.line_list = []
               self.line_list = line.split()
               g = Highscore(self.line_list[0], int(self.line_list[1]))
               self.score_list.append(g)
        except:
            pass





        while len(self.rocks_list) < 10:
            self.rocks_list.append(rocks(randint(20, 980), randint(10, 490), randint(20, 50), randint(20, 50)))





    def on_draw(self):
        self.clear(arcade.color.BLACK)

        if self.begin == True:
            self.updateparticle()
            self.change()
            self.collision()
            self.endsequence()
            self.restarts()
            self.new_rocks()

        for rocks in self.rocks_list:
            rocks.display()

        if self.name_enter:
            arcade.draw_text("ENTER NAME: " + self.name , 325, 250, arcade.color.GREEN, 24)

        if self.turn_right == True:
            self.ship.turn(-5)

        elif self.turn_left == True:
            self.ship.turn(5)

        if self.thrust == True:
            self.ship.thrust(0.2)

        if self.thrust == False:
            self.ship.speed = 0

        if self.begin == False:
            self.shoot = False

        for rocks in self.rocks_list:
            rocks.display()

        for torpedo in self.torpedo_list:
            torpedo.display()

        for particle_list in self.particle_system_list:
            for torpedo in particle_list:
                torpedo.display()
                torpedo.transparent(5)

        for torpedo in self.particle_list_ship_collision:
            torpedo.display()
            torpedo.transparent(5)





        arcade.draw_text("SCORE:" + str(self.score), 40, 50, arcade.color.WHITE_SMOKE, 20, 50 ,  "right", "calibri", False )





    def change(self):
        for i in range(len(self.torpedo_list)-1, -1, -1):
            x = self.torpedo_list[i]

            if x.center_x < 0 or x.center_x > 1000:
                    del(self.torpedo_list[i])
            elif x.center_y < 0 or x.center_y > 500:
                    del(self.torpedo_list[i])

            for g in range(len(self.rocks_list) - 1, -1, -1):
                y = self.rocks_list[g]
                if y.center_x + y.width/2 > x.center_x > y.center_x - y.width/2 and \
                y.center_y + y.height/2 > x.center_y > y.center_y - y.height/2:
                    del(self.torpedo_list[i])
                    del(self.rocks_list[g])
                    self.score +=1

                    particle_list = []

                    while len(particle_list)< 12:
                        particle_list.append(torpedo(y.center_x, y.center_y, 3, 5, uniform(-1, 1), uniform(-1, 1), arcade.color.WHITE))

                    self.particle_system_list.append(particle_list)



    def new_rocks(self):
        if len(self.rocks_list) < 10:
            self.rocks_list.append(rocks(randint(20, 980), randint(10, 490), randint(20, 50), randint(20, 50)))

            for r in range(len(self.rocks_list)-1, -1, -1):
                h = self.rocks_list[r]
                if self.ship.center_x - 50 < h.center_x < self.ship.center_x + 50 and self.ship.center_y -50 < h.center_y < self.ship.center_y + 50:
                    del self.rocks_list[r]

    def updateparticle(self):
        for particle_list in range(len(self.particle_system_list)-1 , -1, -1):
            for e in range(len(self.particle_system_list[particle_list]) - 1, -1, -1):
                u = self.particle_system_list[particle_list][e]
                if u.life < 0:
                    del self.particle_system_list[particle_list][e]

    def collision (self):
        if self.ship_display == True:
            for rocks in self.rocks_list:
                if self.ship.center_x - 25 < rocks.center_x < self.ship.center_x + 25 and self.ship.center_y - 25 < rocks.center_y < self.ship.center_y + 25:
                    if self.ship_display == True:
                        y = Highscore(self.name, self.score)
                        self.score_list.append(y)
                    self.ship_display = False

                    while len(self.particle_list_ship_collision) < 20:
                        self.particle_list_ship_collision.append(torpedo(self.ship.center_x, self.ship.center_y, 3, 5, uniform(-1, 1), uniform(-1, 1), arcade.color.WHITE))


    def endsequence (self):
        if self.ship_display == True:
            self.ship.display()

        else:
            self.turn_right = False
            self.turn_left = False
            self.thrust = False
            self.shoot = False
            arcade.draw_text("GAME OVER", 360, 250, arcade.color.RED, 36)
            arcade.draw_text("FINAL SCORE:" + str(self.score), 360, 200, arcade.color.WHITE, 28)
            arcade.draw_rectangle_outline(900 , 60, 180 , 50, arcade.color.WHITE)
            arcade.draw_text("RESTART", 820, 50, arcade.color.GRAY, 26)


            for i, y in enumerate(self.score_list):
                y.y_pos = 170 - i*25
                y.showcase()




    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.turn_right = True
        if symbol == arcade.key.LEFT:
            self.turn_left = True
        if symbol == arcade.key.UP:
            self.thrust = True
        if symbol == arcade.key.SPACE:
            if self.shoot == True:
                self.torpedo_list.append(torpedo(self.ship.center_x + cos(radians(self.ship.angle)) * self.ship.length / 2, self.ship.center_y
                        + sin(radians(self.ship.angle)) * self.ship.width / 2, 8 , 10, self.ship.x_dir, self.ship.y_dir, arcade.color.WHITE))
        if self.name_enter:
            if symbol == arcade.key.ENTER:
                self.name_enter = False
                self.begin = True
                self.shoot = True
            else:
                self.name += chr(symbol)


    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.turn_right = False
        if symbol == arcade.key.LEFT:
            self.turn_left = False
        if symbol == arcade.key.UP:
            self.thrust = False

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 810 < x < 990 and 10 < y < 110 and self.ship_display == False:
            self.restart = True

    def restarts(self):
        if self.restart == True:
            self.name = ""
            self.center_x = 500
            self.center_y = 500
            self.ship = ship(randint(400, 600), randint(200, 300))
            self.turn_left = False
            self.turn_right = False
            self.shoot = True
            self.thrust = False
            self.alive = True
            self.restart = False
            self.score = 0
            self.torpedo_list = []
            self.particle_system_list = []
            self.rocks_list = []
            self.ship_display = True
            self.particle_list_ship_collision = []
            self.name_enter = True
            self.begin = False

            while len(self.rocks_list) < 10:
                self.rocks_list.append(rocks(randint(20, 980), randint(10, 490), randint(20, 50), randint(20, 50)))



arcade.window=Asteroids(1000, 500, "Asteroids")
arcade.run()


highscore_file = open("scores.txt", "w")
for score in arcade.window.score_list:
    highscore_file.write(score.name + " " + str(score.score)+ "\n")
highscore_file.close()

