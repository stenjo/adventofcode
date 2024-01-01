from itertools import pairwise
import matplotlib.pyplot as plt

Point = tuple[int, int]


class DigPlan:
    def __init__(self, input):
        self.plan = [
            (a[0], int(a[1]), a[2]) for a in [line.strip().split() for line in input]
        ]

    def convFromHex(self, plan):
        converted = []

        for line in plan:
            (_, _, hexStr) = line
            dir = "RDLU"[int(hexStr[-2])]
            length = int(hexStr[2:-2], 16)
            converted.append((dir, length, hexStr))

        return converted

    def dig(self, start, inst):
        directions = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}
        (x, y) = start
        holes: list[Point] = []
        (dir, length, _) = inst
        (dX, dY) = directions[dir]
        holes.append((x + (dX * length), y + (dY * length)))

        return holes, length

    def trench(self, instructions) -> list[Point]:
        trenchLength = 0
        pos = (0, 0)
        points: list[Point] = [pos]
        for inst in instructions:
            p, l = self.dig(pos, inst)
            points += p
            pos = points[-1]
            trenchLength += l

        return points, trenchLength

    def getArea(self, trench):
        # Shoelace formula. Get the area from outline of points
        parts = [x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in pairwise(trench)]
        return sum(parts) / 2

    def fill(self):
        trench, trenchLength = self.trench(self.plan)
        area = self.getArea(trench)

        # pick's theorem - find the number of points in a shape given its area
        fill = int(abs(area) - 0.5 * trenchLength + 1) + trenchLength

        return fill

    def hexFill(self):
        trench, trenchLength = self.trench(self.convFromHex(self.plan))
        area = self.getArea(trench)

        # pick's theorem - find the number of points in a shape given its area
        fill = int(abs(area) - 0.5 * trenchLength + 1) + trenchLength

        return fill
