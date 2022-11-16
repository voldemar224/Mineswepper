class Cell:
    def __init__(self, num, state=0):
        # num -1 means mine inside, another nums mean quantity of mines around
        # state 0 - closed, state 1 - opened
        self.num = num
        self.state = state
