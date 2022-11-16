import tkinter as tk


class Button(tk.Button):
    def __init__(self, x, y, num=0, opened=False, master=None, cnf={}, **kw):
        super().__init__(master=None, cnf={}, **kw)
        self.x = x
        self.y = y
        self.num = num
        self.opened = opened

    def make_move(self, row, col):
        if self.master.field[row][col].num == -1:
            for row in range(self.master.field.height):
                for col in range(self.master.field.width):
                    if self.master.field[row][col].num == -1:
                        self.master.field[row][col].found_mine(0)
        else:
            self.master.field[row][col].opened = 1

            self.open_cells_around(row, col)

    def open_cells_around(self, row, col):
        if self.master.field[row][col].num == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i, j) != (0, 0) \
                            and 0 <= row + i < self.master.field.height \
                            and 0 <= col + j < self.master.field.width \
                            and self.master.field[row + i][col + j].opened == 0:
                        self.master.field[row + i][col + j].opened = 1
                        if self.master.field[row + i][col + j].num == 0:
                            self.open_cells_around(row + i, col + j)

    def press_btn(self):
        self.make_move(self.y, self.x)

        for row in range(self.master.field.height):
            for col in range(self.master.field.width):
                if self.master.field[row][col].opened:
                    self.master.field[row][col].configure(relief=tk.SUNKEN)
                    self.master.field[row][col].opened = True
                    if self.master.field[row][col].num == 1:
                        self.master.field[row][col].configure(text=str(self.master.field[row][col].num),  fg='blue')
                    elif self.master.field[row][col].num == 2:
                        self.master.field[row][col].configure(text=str(self.master.field[row][col].num), fg='green')
                    elif self.master.field[row][col].num == 3:
                        self.master.field[row][col].configure(text=str(self.master.field[row][col].num), fg='red')
                    elif self.master.field[row][col].num == 4:
                        self.master.field[row][col].configure(text=str(self.master.field[row][col].num), fg='cyan')
                    elif self.master.field[row][col].num == 0:
                        pass
                    else:
                        self.master.field[row][col].configure(text=str(self.master.field[row][col].num))

    def found_mine(self, argument):
        self.configure(image=self.master.photo, width=25)
        print(1)
        # self.configure(text="P", width=3)
