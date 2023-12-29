class Parabolic:
    def __init__(self, input=[]):
        self.dishMap = [l.strip() for l in input]
        self.tiltedMap = []

    def rolledNorth(self, dish=None):
        if not dish:
            dish = self.dishMap
        dish = self.tilted(dish)
        return [self.calculateLoad(dish)]

    def tilted(self, dish):
        mirrors = self.transpose(dish)
        rowMap = []
        for i, mirror in enumerate(mirrors):
            parts = "".join(mirror).split("#")
            pos = 0
            row = []
            for part in parts:
                cnt = part.count("O")
                pos += len(part) + 1
                row.append(self.createPart(cnt, len(part)))
            rowMap.append("#".join(row))

        tilted = self.transpose(rowMap)
        return tilted

    def createPart(self, boulders, length):
        return "".join(["O"] * boulders + ["."] * (length - boulders))

    def calculateLoad(self, dish):
        max = len(dish)
        load = 0
        for row, line in enumerate(dish):
            load += (max - row) * line.count("O")

        return load

    def transpose(self, dish):
        l = ["".join(l) for l in map(list, zip(*dish))]
        return [str(ln) for ln in l]

    def flip(self, dish):
        return [mirrors[::-1] for mirrors in dish]

    def rotate(self, dish):
        return self.flip(self.transpose(dish))

    def printMap(self, dish):
        for n in dish:
            print(n)
        print()

    def runCycle(self, dish=None):
        if dish is None:
            dish = self.dishMap
        for _ in range(4):
            dish = self.tilted(dish)
            dish = self.rotate(dish)

        return dish

    def cycles(self, cycles):
        cycle = 1
        log = {}
        startSet = tuple(set(map(tuple, self.dishMap)))
        log[startSet] = 0
        dish = self.runCycle(self.dishMap)
        pattern = tuple(set(map(tuple, dish)))
        while pattern not in log.keys():
            log[pattern] = cycle
            dish = self.runCycle(dish)
            cycle += 1
            pattern = tuple(set(map(tuple, dish)))

        offset = log[pattern]
        mod = cycle - offset
        reducedCycles = (cycles - offset) % mod
        for _ in range(reducedCycles):
            dish = self.runCycle(dish)

        return self.calculateLoad(dish)
