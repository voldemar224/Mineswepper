import tkinter as tk
import random
import const

from button import Button


class Window(tk.Tk):
    def __init__(self, field, screenName=None, baseName=None, className='Tk', useTk=True, sync=False,
                 use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.field = field
        self.geometry('+700+200')
        self.btns_frame = tk.Frame(self)

        self.photo = tk.PhotoImage(file=r"D:\Python\graph_libs\tkinter\mineswepper_tkinter\flag.png")

        self.create_btns_window()
        self.nums_arnd_mines()

    def create_btns_window(self):
        mines = sorted(random.sample(range(0, self.field.width * self.field.height), self.field.mines_q))

        for row in range(self.field.height):
            self.field.append([])
            for col in range(self.field.width):
                self.field[row].append(Button(x=col, y=row, master=self.btns_frame, width=3))
                self.field[row][-1].configure(command=self.field[row][-1].press_btn)
                self.field[row][-1].bind('<Button-3>', self.field[row][-1].found_mine)

                self.field[row][-1].grid(row=row, column=col)

        for mine in mines:
            row = mine // 10
            col = mine % 10
            self.field[row][col].num = -1

        self.btns_frame.grid(row=0, column=0)

    def increment_around(self, row, cell):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i, j) != (0, 0) \
                        and 0 <= row + i < self.field.height \
                        and 0 <= cell + j < self.field.width \
                        and self.field[row + i][cell + j].num != -1:
                    self.field[row + i][cell + j].num += 1
                    # вокруг мины num увеличиваем на один
                    # (-1, -1) (-1, 0) (-1,1)
                    # (0, -1)  (0, 0)  (0, 1)
                    # (1, -1)  (1, 0)  (1, 1)
                    # следим за выходом за поле
                    # не увеличиваем num у мин

    def nums_arnd_mines(self):
        for row in range(self.field.height):
            for cell in range(self.field.width):
                if self.field[row][cell].num == -1:
                    self.increment_around(row, cell)
