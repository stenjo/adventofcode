class Tile:
    def __init__(self, x, y, connector):
        self.x = x
        self.y = y
        self.connector = connector
        self.next = []
        self.steps = None
