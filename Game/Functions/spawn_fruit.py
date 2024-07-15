# Teleporting Fruit to Random Position
from random import random


def spawn(fruit, occupied_positions):
  while True:
    fruit.position = (random.randint(0, fruit.field[0] - 1), random.randint(0, fruit.field[0] - 1))
    if fruit.position not in occupied_positions:
      break