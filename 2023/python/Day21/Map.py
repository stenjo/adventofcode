from Day21.Tile import Tile


class Map:
    def __init__(self, input=""):
        self.map = {}
        self.dim = (
            len(input.strip().split("\n")[0]) if len(input) > 0 else 0,
            len(input.strip().split("\n")),
        )
        self.start = None
        self.maxSteps = 0
        for y, line in enumerate(input.strip().split("\n")):
            for x, c in enumerate(line.strip()):
                if c in ".S":
                    self.map[(x, y)] = Tile(x, y, c)
                if c == "S":
                    self.start = (x, y)

        return

    def addNextIfExists(self, t, nx, ny):
        if (nx, ny) in self.map.keys():
            t.next.append((nx, ny))

    def countSteps(self, steps):
        t = self.map[self.start]
        self.map[self.start].steps = 0
        tiles = [self.map[self.start]]
        for step in range(1, steps + 1):
            nextStep = []
            for tile in tiles:
                (x, y) = tile.pos
                for dX, dY in [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                ]:
                    if (x + dX, y + dY) in self.map.keys():
                        t = self.map[(x + dX, y + dY)]
                        if t.steps == None:
                            t.steps = step
                            nextStep.append(t)
            tiles = nextStep

    def tilesReachedInSteps(self, steps):
        self.countSteps(steps)

        return len([t for t in self.map.values() if t.isReachedBySteps(steps)])

    def getTileLeft(self, tile):
        if tile.x == 0:
            return None
        leftTile = (tile.x - 1, tile.y)
        if leftTile in self.map.keys():
            return self.map[leftTile]
        else:
            return None

    def getTileRight(self, tile):
        if tile.x == self.dim[0] - 1:
            return None
        rightTile = (tile.x + 1, tile.y)
        if rightTile in self.map.keys():
            return self.map[rightTile]
        else:
            return None

    def getTileAbove(self, tile):
        if tile.y == 0:
            return None
        aboveTile = (tile.x, tile.y - 1)
        if aboveTile in self.map.keys():
            return self.map[aboveTile]
        else:
            return None

    def getTileBelow(self, tile):
        if tile.y == self.dim[1] - 1:
            return None
        aboveTile = (tile.x, tile.y + 1)
        if aboveTile in self.map.keys():
            return self.map[aboveTile]
        else:
            return None
