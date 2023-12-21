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
        (maxX, maxY) = self.dim
        for y in [-1,maxY+1]:
            for x in [-1,maxX+1]:
                self.map[(x, y)] = Tile(x, y, ".")
                

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
        
        l = {pos for pos,t in self.map.items() if t.isReachedBySteps(steps)}
        return len(l)
