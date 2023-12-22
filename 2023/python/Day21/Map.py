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
        (maxX, maxY) = self.dim
        for y, line in enumerate(input.strip().split("\n")):
            for x, c in enumerate(line.strip()):
                if c in ".S":
                    self.map[(x, y)] = Tile(x, y, c)
                if c == "S":
                    self.start = (x, y)

    def setMap(self, pos, tile):
        (dimX, dimY) = self.dim
        (x, y) = pos
        x = x % dimX
        y = y % dimY
        self.map[(x, y)] = tile

    def getMap(self, pos):
        (dimX, dimY) = self.dim
        (x, y) = pos
        x = x % dimX
        y = y % dimY
        return self.map[(x, y)]

    def getMapKeys(self):
        return self.map.keys()

    def isPlot(self, pos):
        (dimX, dimY) = self.dim
        (x, y) = pos
        x = x % dimX
        y = y % dimY
        return (x, y) in self.getMapKeys()

    def setSteps(self):
        t = self.getMap(self.start)
        t.steps = 0
        tiles = [t]
        step = 0
        (dimX, dimY) = self.dim
        while None in [
            self.map[(0, 0)],
            self.map[(0, dimY - 1)],
            self.map[(dimX - 1, 0)].steps,
            self.map[(dimX - 1, dimY - 1)].steps,
        ]:
            nextStep = []
            step += 1
            for tile in tiles:
                (x, y) = tile.position()
                for dX, dY in [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                ]:
                    if self.isPlot((x + dX, y + dY)):
                        t = self.getMap((x + dX, y + dY))
                        if t.steps == None:
                            t.steps = step
                            nextStep.append(t)
            tiles = nextStep

    def countSteps(self, steps):
        t = self.getMap(self.start)
        t.steps = 0
        tiles = [t]
        for step in range(1, steps + 1):
            nextStep = []
            for tile in tiles:
                (x, y) = tile.position()
                for dX, dY in [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                ]:
                    if self.isPlot((x + dX, y + dY)):
                        t = self.getMap((x + dX, y + dY))
                        if t.steps == None:
                            t.steps = step
                            nextStep.append(t)
            tiles = nextStep

    def tilesReachedInSteps(self, steps):
        # self.countSteps(steps)
        self.setSteps()

        l = {pos for pos, t in self.map.items() if t.isReachedBySteps(steps)}
        return len(l)
