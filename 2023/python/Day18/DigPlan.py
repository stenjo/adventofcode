from rich import print
import matplotlib.pyplot as plt

class DigPlan:
    def __init__(self,input):
        self.plan = [(a[0], int(a[1]), a[2]) for a in [line.strip().split() for line in input]]
        self.map = {}
        self.dim = {"minY": 0, "minX": 0, "maxY": 0, "maxX": 0}
        self.plot = []
        
    def dig(self, start, inst):
        directions = {"R": (1,0), "L":(-1,0), "U":(0,-1), "D": (0,1)}
        (x,y) = start
        (dir, length, color) = inst
        (dX,dY) = directions[dir]
        xPlot = []
        yPlot = []
        for n in range(length):
            self.map[(x+(dX*n), y+(dY*n))] = color
            xPlot.append(x+(dX*n))
            yPlot.append(y+(dY*n))
            
        self.plot.append((xPlot, yPlot, color[1:-1]))
        return (x+(dX*n + dX), y+(dY*n+dY))
            
    def trench(self):
        pos = (0,0)
        for inst in self.plan:
            (x,y) = self.dig(pos, inst)
            if x > self.dim["maxX"]: self.dim["maxX"] = x
            if y > self.dim["maxY"]: self.dim["maxY"] = y
            if x < self.dim["minX"]: self.dim["minX"] = x
            if y < self.dim["minY"]: self.dim["minY"] = y
            pos = (x,y)
            
        self.fill()
        
        return len(list(self.map.keys()))
            
    def fill(self):
        for y in range(self.dim["minY"], self.dim["maxY"]+1):
            color = None
            firstTrench = False
            trenchesFull = set([(xX,y) for xX in range(self.dim["minX"],self.dim["maxX"]+1)]).intersection(set(self.map.keys())) # ALl trenches on the line
            trenches = []
            for (x,y) in list(trenchesFull):
                if (x-1,y) not in self.map.keys() or self.map[(x-1,y)] != self.map[(x,y)]:
                    trenches.append((x,y))
            for x in range(self.dim["minX"], self.dim["maxX"]+1):
                if (x,y) in self.map.keys():
                    color = self.map[(x,y)]
                    if (x,y) in trenches:
                        trenches.remove((x,y))
                    firstTrench = True
                else:
                    if len(trenches) > 0 and len(trenches)%2 == 1 and firstTrench == True:
                        self.map[(x,y)] = color
        
    def print(self):
        for (xPoints, yPoints, color) in self.plot:
            plt.plot(xPoints, yPoints, 'o', color=color)
        plt.show()
    
    def plotFilled(self):
        
        xPoints = []
        yPoints = []
        for y in range(self.dim["minY"], self.dim["maxY"]+1):
            for x in range(self.dim["minX"], self.dim["maxX"]+1):
                if (x,y) in self.map.keys():
                    (color) = self.map[(x,y)]
                    xPoints.append(x)
                    yPoints.append(y)
        plt.plot(xPoints, yPoints, 'o')
        plt.show()
                    