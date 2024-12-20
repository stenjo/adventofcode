import re


class Entrapment:
    def __init__(self, input):
        self.tiles = [l.strip() for l in input]
        self.dim = (len(self.tiles[0]), len(self.tiles)) if len(input) > 0 else (0, 0)
        self.energized = {}

    def beam(self, dir, pos):
        (x, y) = pos
        if x >= self.dim[0] or y >= self.dim[1]:
            return None
        if x <= -1 or y <= -1:
            return None

        if (x, y) not in self.energized.keys():
            self.energized[(x, y)] = [dir]
        else:
            if dir in self.energized[(x, y)]:
                return None
            else:
                self.energized[(x, y)].append(dir)

        match self.tiles[y][x]:
            case ".":
                if dir == ">":
                    return [(dir, (x + 1, y))]
                if dir == "V":
                    return [(dir, (x, y + 1))]
                if dir == "<":
                    return [(dir, (x - 1, y))]
                if dir == "^":
                    return [(dir, (x, y - 1))]
            case "\\":
                if dir == ">":
                    return [("V", (x, y + 1))]
                if dir == "V":
                    return [(">", (x + 1, y))]
                if dir == "<":
                    return [("^", (x, y - 1))]
                if dir == "^":
                    return [("<", (x - 1, y))]
            case "/":
                if dir == ">":
                    return [("^", (x, y - 1))]
                if dir == "V":
                    return [("<", (x - 1, y))]
                if dir == "<":
                    return [("V", (x, y + 1))]
                if dir == "^":
                    return [(">", (x + 1, y))]

            case "|":
                if dir == "V":
                    return [("V", (x, y + 1))]
                if dir == "^":
                    return [("^", (x, y - 1))]
                if dir in ["<", ">"]:
                    return [("^", (x, y - 1)), ("V", (x, y + 1))]
            case "-":
                if dir == ">":
                    return [(">", (x + 1, y))]
                if dir == "<":
                    return [("<", (x - 1, y))]
                if dir in ["^", "V"]:
                    return [("<", (x - 1, y)), (">", (x + 1, y))]
        return

    def countEnergized(self, starting=(">", (0, 0))):
        tiles = [starting]
        while len(tiles) > 0:
            m = []
            for t in tiles:
                dir, (x, y) = t
                n = self.beam(dir, (x, y))
                m += n if n is not None else []
            tiles = m

        return len(self.energized)

    def getMaxStarters(self):
        entries = {}
        entries[(">", (0, 0))] = self.countEnergized()

        for x in range(self.dim[0]):
            self.updateEntries(entries, ("V", (x, 0)))
        for x in range(self.dim[0]):
            self.updateEntries(entries, ("^", (x, self.dim[1] - 1)))
        for y in range(self.dim[1]):
            self.updateEntries(entries, (">", (0, y)))
        for y in range(self.dim[1]):
            self.updateEntries(entries, (">", (self.dim[1] - 1, y)))

        return max([c for c in entries.values()])

    def updateEntries(self, entries, key):
        if key not in entries.keys():
            (_, (x, y)) = key
            self.energized = {}
            entries[key] = self.countEnergized(key)
            for x in range(self.dim[0]):
                y = 0
                if ("V", (x, y)) in self.energized.keys():
                    entries[("V", (x, y))] = entries[key]
                y = self.dim[1] - 1
                if ("^", (x, y)) in self.energized.keys():
                    entries[("^", (x, y))] = entries[key]
            for y in range(self.dim[1]):
                x = 0
                if (">", (x, y)) in self.energized.keys():
                    entries[(">", (x, y))] = entries[key]
                x = self.dim[0] - 1
                if ("<", (x, y)) in self.energized.keys():
                    entries[("<", (x, y))] = entries[key]

    def printMap(self):
        for y, r in enumerate(self.tiles):
            row = ""
            for x, c in enumerate(r):
                if c != ".":
                    row += c
                elif (x, y) in self.energized.keys():
                    if len(self.energized[(x, y)]) > 1:
                        row += str(len(self.energized[(x, y)]))
                    else:
                        row += self.energized[(x, y)][0]
                else:
                    row += "."
            print(row)
