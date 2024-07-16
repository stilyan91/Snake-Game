from .fruit import Fruit
from .snake import Snake


class Game:
    def __init__(self, field=(15, 15), speed=0.1):
        self.field = field
        self.speed = speed
        self.is_running = True

        self.fruit = Fruit(field=self.field, sprite='x')
        self.snake = Snake(field=self.field, sprite='@')

    def reset(self):
        self.is_running = True
        self.snake.left = 2
        self.snake.positions = [(0, 0)] * 2
        self.fruit.position = (self.field[0] - 1, self.field[1] - 1)

    def game_over(self):
        self.is_running = False
        self.reset()

    def handle_collisions(self, snake):
        if snake.is_collision():
            self.game_over()

        if snake.is_collision(self.fruit.position):
            self.fruit.spawn(self.snake.positions)
            self.snake.grow()
