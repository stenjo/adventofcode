from Day10.Tile import Tile


class Map:
    def __init__(self, input=[]):
        self.map = {}
        self.start = None
        self.maxSteps = 0
        for y, line in enumerate(input):
            for x, c in enumerate(line.strip()):
                if c != ".":
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
