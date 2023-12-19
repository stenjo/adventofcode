from Day10.Tile import Tile


class Map:
    def __init__(self, input=[]):
        self.map = {}
        self.dim = (len(input[0]) if len(input) > 0 else 0, len(input))
        self.start = None
        self.maxSteps = 0
        for y, line in enumerate(input):
            for x, c in enumerate(line.strip()):
                if c != ".":
                    self.map[(x, y)] = Tile(x, y, c)
                if c == "S":
                    self.start = (x, y)

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
        for (x, y), t in self.map.items():
            for dX, dY in neighbors[self.map[(x, y)].connector]:
                self.addNextIfExists(t, x + dX, y + dY)
        return

    def addNextIfExists(self, t, nx, ny):
        if (nx, ny) in self.map.keys():
            t.next.append((nx, ny))

    def countSteps(self):
        t = self.map[self.start]
        self.map[self.start].steps = 1
        stepCounts = []
        for n in t.next:
            step = 1
            while n != self.start:
                step += 1
                self.map[n].steps = step
                next = [nt for nt in self.map[n].next if self.map[nt].steps == None]
                if len(next) > 0:
                    n = next[0]
                else:
                    n = self.start

            stepCounts.append(step)
        return max(stepCounts) / 2

    def updateMaxSteps(self, steps):
        if steps > self.maxSteps:
            self.maxSteps = steps

    def stepsToMostDistantPoint(self):
        return self.countSteps()

    def removeTrashed(self):
        (maxX, maxY) = self.dim
        for y in range(maxY):
            for x in range(maxX):
                if (x, y) in self.map.keys() and self.map[(x, y)].steps == None:
                    self.map[(x, y)].connector = "."
                elif (x, y) not in self.map.keys():
                    self.map[(x, y)] = Tile(x, y, ".")

        count = len(self.map.keys())
        return count

    def countInside(self, y):
        (maxX, _) = self.dim
        inside = False
        count = 0
        for x in range(maxX):
            c = self.map[(x, y)].connector
            if c in "|JL":
                inside = not inside
            else:
                count += 1 if inside and c not in "F-" else 0

        return count

    def enclosedTiles(self):
        self.countSteps()
        self.removeTrashed()

        (maxX, maxY) = self.dim
        rowSum = [self.countInside(y) for y in range(maxY)]
        return sum(rowSum)

    def trackPipes(self, previous: Tile, tile: Tile):
        if tile == None:
            return None
        if tile == self.start:
            return 1
        steps = 0
        left = self.getTileLeft(tile)
        right = self.getTileRight(tile)
        over = self.getTileAbove(tile)
        under = self.getTileBelow(tile)
        match tile.connector:
            case "S":
                self.trackPipes(tile, self.map[(tile.x, tile.y - 1)])
                self.trackPipes(tile, self.map[(tile.x, tile.y + 1)])
                self.trackPipes(tile, self.map[(tile.x - 1, tile.y)])
                self.trackPipes(tile, self.map[(tile.x + 1, tile.y)])

            case "-":
                if left == previous:
                    steps = self.trackPipes(tile, right)
                elif right == previous:
                    steps = self.trackPipes(tile, left)
                elif over == previous or under == previous:
                    steps = max(
                        n
                        for n in [
                            self.trackPipes(tile, left),
                            self.trackPipes(tile, right),
                        ]
                        if n
                    )

            case "|":
                if over == previous:
                    steps = self.trackPipes(tile, under)
                elif under == previous:
                    steps = self.trackPipes(tile, over)
                elif left == previous or right == previous:
                    steps = max(
                        n
                        for n in [
                            self.trackPipes(tile, over),
                            self.trackPipes(tile, under),
                        ]
                        if n
                    )

            case "7":
                if left == previous:
                    steps = self.trackPipes(tile, under)
                elif under == previous:
                    steps = self.trackPipes(tile, left)
                else:
                    return None

            case "J":
                if over == previous:
                    steps = self.trackPipes(tile, left)
                elif left == previous:
                    steps = (self.trackPipes(tile, over),)
                else:
                    return None

            case "L":
                if over == previous:
                    steps = self.trackPipes(tile, right)
                elif right == previous:
                    steps = (self.trackPipes(tile, over),)
                else:
                    return None

            case "F":
                if right == previous:
                    steps = self.trackPipes(tile, under)
                elif under == previous:
                    steps = self.trackPipes(tile, right)
                else:
                    return None

            case _:
                raise ValueError("Unknown connector: ", t.connector)

        if steps != None:
            return steps + 1
        else:
            return None

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
