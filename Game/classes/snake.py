class Snake:
    RIGHT = (0, 1)
    LEFT = (0, -1)
    UP = (-1, 0)
    DOWN = (1, 0)

    def __init__(self, field, sprite, length=2):
        self.field = field
        self.sprite = sprite
        self.length = length
        self.positions = [(0, 0)] * length
        self.direction = self.RIGHT

    def move(self):
        for i in range(0, self.length - 1):
            self.positions[i] += self.positions[i - 1]

        self.positions = tuple(x + y for x, y in zip(self.positions[0], self.direction))
        self.positions = tuple(x % y for x, y in zip(self.positions[1], self.field))

    def grow(self):
        self.length += 1
        self.positions.append(self.positions[-1])

    def change_direction_to_left(self, direction):
        if self.direction != self.RIGHT:
            self.direction = self.LEFT

    def change_direction_to_right(self, direction):
        if self.direction != self.LEFT:
            self.direction = self.RIGHT

    def change_direction_to_up(self, direction):
        if self.direction != self.DOWN:
            self.direction = self.UP

    def change_direction_to_down(self, direction):
        if self.direction != self.UP:
            self.direction = self.DOWN

    def is_collision(self, point=None):
        if point is None:
            point = self.positions[0]

        for position in self.positions[1:]:
            if point == position:
                return True

        return False
