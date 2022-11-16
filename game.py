class Game:
    def __init__(self, field, game_over=False):
        self.field = field
        self.game_over = game_over

    def make_move(self, move):
        row = move // 10
        col = move % 10

        if self.field[row][col].num == -1:
            for row in range(self.field.height):
                for col in range(self.field.width):
                    if self.field[row][col].num == -1:
                        self.field[row][col].state = 1
            self.game_over = True
        else:
            self.field[row][col].state = 1

            self.open_cells_around(row, col)

    def open_cells_around(self, row, col):
        if self.field[row][col].num == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i, j) != (0, 0) \
                            and 0 <= row + i < self.field.height \
                            and 0 <= col + j < self.field.width \
                            and self.field[row + i][col + j].state == 0:
                        self.field[row + i][col + j].state = 1
                        if self.field[row + i][col + j].num == 0:
                            self.open_cells_around(row + i, col + j)
