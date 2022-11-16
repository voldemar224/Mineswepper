from field import Field
from game import Game
from window import Window


field = Field()

window = Window(field)
# field.draw_sol()

window.mainloop()
