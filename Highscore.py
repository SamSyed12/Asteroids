
import arcade



class Highscore:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.y_pos = 300







    def showcase(self):
        arcade.draw_text( str(self.name) + ": " + str(self.score), 450, self.y_pos , arcade.color.WHITE, 20, "left")





