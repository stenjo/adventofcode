from Day10.Tile import Tile


class Map:
    def __init__(self, input=[]):
        self.map = {}
        self.dim = (len(input[0]) if len(input) > 0 else 0, len(input))
        self.start = None
        self.maxSteps = 0
        for y, line in enumerate(input):
            for x, c in enumerate(line.strip()):
                # if c != ".":
                self.map[(x, y)] = Tile(x, y, c)
                if c == "S":
                    self.start = (x, y)

        for (x, y), t in self.map.items():
            match t.connector:
                case "S":
                    self.addNextIfExists(t, x - 1, y)
                    self.addNextIfExists(t, x + 1, y)
                    self.addNextIfExists(t, x, y - 1)
                    self.addNextIfExists(t, x, y + 1)
                case "-":
                    self.addNextIfExists(t, x - 1, y)
                    self.addNextIfExists(t, x + 1, y)
                case "|":
                    self.addNextIfExists(t, x, y - 1)
                    self.addNextIfExists(t, x, y + 1)
                case "7":
                    self.addNextIfExists(t, x - 1, y)
                    self.addNextIfExists(t, x, y + 1)
                case "J":
                    self.addNextIfExists(t, x - 1, y)
                    self.addNextIfExists(t, x, y - 1)
                case "L":
                    self.addNextIfExists(t, x + 1, y)
                    self.addNextIfExists(t, x, y - 1)
                case "F":
                    self.addNextIfExists(t, x + 1, y)
                    self.addNextIfExists(t, x, y + 1)
                case ".":
                    continue
                case _:
                    raise ValueError("Unknown connector: ", t.connector)

    def addNextIfExists(self, t, nx, ny):
        if (nx, ny) in self.map.keys():
            t.next.append((nx, ny))

    def countSteps(self):
        t = self.map[self.start]
        step = 0
        next = t.next
        while len(next) > 0:
            step += 1
            newNext = []
            for n in next:
                self.map[n].steps = step
                newNext += [
                    nt
                    for nt in self.map[n].next
                    if self.map[nt].steps == None or self.map[nt].steps < step - 1
                ]
            next = newNext

        return step

    def updateMaxSteps(self, steps):
        if steps > self.maxSteps:
            self.maxSteps = steps

    def stepsToMostDistantPoint(self):
        return self.countSteps()

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
