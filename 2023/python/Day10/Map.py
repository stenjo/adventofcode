from Day10.Tile import Tile


class Map:
    def __init__(self, input=""):
        self.map = {}
        self.start = None
        self.maxSteps = 0
        lines = input.strip().split("\n")
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c != ".":
                    self.map[(x, y)] = Tile(x, y, c)
                if c == "S":
                    self.start = (x, y)

        self.dim = (len(lines[0]) if len(lines) > 0 else 0, len(lines))

        self.neighbors = {
            "S": [(-1, 0), (1, 0), (0, -1), (0, 1)],
            "-": [(-1, 0), (1, 0)],
            "|": [(0, -1), (0, 1)],
            "7": [(-1, 0), (0, 1)],
            "J": [(-1, 0), (0, -1)],
            "L": [(1, 0), (0, -1)],
            "F": [(1, 0), (0, 1)],
            ".": [],
        }

        for (x, y), t in self.map.items():
            for pos in t.neighbors():
                self.addNextIfExists(t, pos)

    def addNextIfExists(self, t, pos):
        if pos in self.map.keys():
            t.next.append(pos)

    def getPipeTrail(self, start):
        trail = [self.start]
        n = start
        while n != self.start:
            trail.append(n)
            next = [nt for nt in self.map[n].next if nt not in trail]
            if len(next) > 0:
                n = next.pop(0)
            else:
                break

        return trail

    def getLoop(self):
        t = self.map[self.start]
        # to count insides correctly S needs to be replaced with a pipe
        t.setPipeByNext(self.map)
        start = [nt for nt in t.next if self.start in self.map[nt].next]
        loop = self.getPipeTrail(start[0])
        return start[0], loop

    def stepsToMostDistantPoint(self):
        _, loop = self.getLoop()
        return len(loop) // 2

    def countInside(self, y, loop=None):
        if not loop:
            loop = self.map.keys()
        (maxX, _) = self.dim
        inside = False
        count = 0
        for x in range(maxX):
            if (x, y) in loop:
                if self.map[(x, y)].pipe in "|JL":
                    inside = not inside
            else:
                count += 1 if inside else 0

        return count

    def enclosedTiles(self):
        (_, loop) = self.getLoop()
        (_, maxY) = self.dim  # (140,140)
        rowSum = [self.countInside(y, loop) for y in range(maxY)]
        return sum(rowSum)
