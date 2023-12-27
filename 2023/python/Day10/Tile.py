neighbors = {
    "S": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "|": [(0, -1), (0, 1)],
    "7": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "L": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}


class Tile:
    def __init__(self, x, y, connector):
        self.x = x
        self.y = y
        self.pipe = connector
        self.next = []
        self.steps = None

    def neighbors(self):
        return [(self.x + dx, self.y + dy) for dx, dy in neighbors[self.pipe]]

    def setPipeByNext(self, grid):
        if self.next is not None:
            (sx, sy) = self.x, self.y
            self.next = [nt for nt in self.next if (sx, sy) in grid[nt].next]
            flipped = {frozenset(v): k for k, v in neighbors.items()}
            self.pipe = flipped[frozenset([(x - sx, y - sy) for (x, y) in self.next])]
