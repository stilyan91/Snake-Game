from random import randint


class Fruit:
    def __init__(self, field, sprite):
        self.field = field
        self.sprite = sprite
        self.position = (self.field[0] - 1, self.field[1] - 1)

    def spawn(self, occupied_positions):
        while True:
            self.position = (randint(0, self.field[0]), randint(0, self.field[1]))
            if self.position not in occupied_positions:
                break
