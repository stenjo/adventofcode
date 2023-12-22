class Tile:
    def __init__(self, x, y, connector):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.con = connector
        self.next = []
        self.steps = None

    def isReachedBySteps(self, steps):
        if (
            self.steps is not None
            and steps >= self.steps
            and (steps - self.steps) % 2 == 0
        ):
            return True
        else:
            return False

    def position(self):
        return self.pos
