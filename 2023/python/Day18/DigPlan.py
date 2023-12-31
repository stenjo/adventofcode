from itertools import pairwise
from rich import print
import matplotlib.pyplot as plt

Point = tuple[int,int]

class DigPlan:
    def __init__(self,input):
        self.plan = [(a[0], int(a[1]), a[2]) for a in [line.strip().split() for line in input]]
        self.map = {}
        self.dim = {"minY": 0, "minX": 0, "maxY": 0, "maxX": 0}
        self.plot = []
        
    def dig(self, start, inst):
        directions = {"R": (1,0), "L":(-1,0), "U":(0,-1), "D": (0,1)}
        (x,y) = start
        holes: list[Point] = []
        (dir, length, _) = inst
        (dX,dY) = directions[dir]
        for n in range(1,length+1):
            holes.append((x+(dX*n), y+(dY*n)))
            
        return holes
            
    def hexDig(self, start, inst):
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        (x,y) = start
        holes: list[Point] = []
        (_, _, hexStr) = inst
        length = int(hexStr[2:-2], 16)
        dir = int(hexStr[-2])
        (dX,dY) = directions[dir]
        for n in range(1,length+1):
            holes.append((x+(dX*n), y+(dY*n)))
            
        return holes
            
    def trench(self) -> list[Point]:
        
        pos = (0,0)
        points: list[Point] = []
        for inst in self.plan:
            points+=self.dig(pos, inst)
            pos = points[-1]
        
        points.append((0,0))
        return points
            
    def hexTrench(self) -> list[Point]:
        trenchLength = 0
        pos = (0,0)
        points: list[Point] = []
        for inst in self.plan:
            points+=self.hexDig(pos, inst)
            pos = points[-1]
        
        points.append((0,0))
        return points, trenchLength
            
    def getArea(self, trench):
        # Shoelace formula. Get the area from outline of points
        parts = [x1*y2 - x2*y1 for (x1,y1),(x2,y2) in pairwise(trench)]
        return sum(parts) / 2
    
    def fill(self):
        trench = self.trench()
        area = self.getArea(trench)

        # pick's theorem - find the number of points in a shape given its area
        fill = int(abs(area) - 0.5*len(trench) +1) + len(trench)
        
        return fill
    
    def hexFill(self):
        trench, trenchLength = self.hexTrench()
        area = self.getArea(trench)

        # pick's theorem - find the number of points in a shape given its area
        fill = int(abs(area) - 0.5*trenchLength +1) + trenchLength
        
        return fill
                
    def print(self):
        for (xPoints, yPoints, color) in self.plot:
            plt.plot(xPoints, yPoints, 'o', color=color)
        plt.show()
                        
GridPoint = tuple[int, int]
OFFSETS: dict[str, GridPoint] = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

class Solution:
    def __init__(self, input):
        self.input = input
        
    def num_points(self, outline: list[GridPoint]) -> int:
        """
        the number of the points inside an outline plus the number of points in the outline
        """
        # shoelace - find the float area in a shape
        area = (
            sum(
                row1 * col2 - row2 * col1
                for (row1, col1), (row2, col2) in pairwise(outline)
            )
            / 2
        )
        # pick's theorem - find the number of points in a shape given its area
        return int(abs(area) - 0.5 * len(outline) + 1) + len(outline)


    def part_1(self) -> int:
        points: list[GridPoint] = [(0, 0)]

        for line in self.input:
            direction, distance_str, _ = line.split()

            for _ in range(int(distance_str)):
                points.append(self.add_points(OFFSETS[direction], points[-1]))

        return self.num_points(points)
    
    def add_points(self, a: GridPoint, b: GridPoint) -> GridPoint:
        """
        add a pair of 2-tuples together. Useful for calculating a new position from a location and an offset
        """
        return a[0] + b[0], a[1] + b[1]