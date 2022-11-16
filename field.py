import random
import const
from button import Button


class Field(list):
    def __init__(self, height=const.FH, width=const.FW, mines_q=const.MINES_Q):
        super().__init__()
        self.height = height
        self.width = width
        self.mines_q = mines_q

    def draw_sol(self):
        for row in self:
            for cell in row:
                if cell.num == -1:
                    print(" #", end=' ')
                else:
                    print(f" {cell.num}", end=' ')

            print("           ", end="")

            for cell in row:
                if cell.opened == 0:
                    print("[ ]", end=' ')
                else:
                    if cell.num == -1:
                        print(" # ", end=' ')
                    else:
                        print(f" {cell.num} ", end=' ')

            print()
