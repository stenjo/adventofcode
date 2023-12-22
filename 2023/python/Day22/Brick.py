import itertools


class Brick:
    def __init__(self, input=""):
        self.x = []
        self.y = []
        self.z = []
        if input:
            self.x = [int(c.split(",")[0]) for c in input.strip().split("~")]
            self.y = [int(c.split(",")[1]) for c in input.strip().split("~")]
            self.z = [int(c.split(",")[2]) for c in input.strip().split("~")]

        self.dim = (
            self.x[1] - self.x[0] + 1 if len(self.x) > 0 else 0,
            self.y[1] - self.y[0] + 1 if len(self.y) > 0 else 0,
            self.z[1] - self.z[0] + 1 if len(self.z) > 0 else 0,
        )
        self.supportedBy = []
        self.supports = []

    def overlaps(self, brick):
        brickGrains = self.getGrains(brick);
        myGrains = self.getGrains(self)
        if brickGrains.intersection(myGrains):
            return True
        return False

    def getGrains(self, brick):
        return set(itertools.product(range(brick.x[0], brick.x[1] + 1), range(brick.y[0], brick.y[1]+1)))

    def isSupporting(self, brick):
        if self.overlaps(brick) and (self.z[1] + 1) == brick.z[0]:
            self.setSupports(brick)
            brick.setSupportedBy(self)
            return True
        return False

    def setHeight(self, height):
        (_, _, dimZ) = self.dim
        self.z[0] = height + 1
        self.z[1] = height + dimZ

    def top(self):
        return self.z[1]
    
    def setSupportedBy(self, supported):
        if supported not in self.supportedBy:
            self.supportedBy.append(supported)
        else:
            return
    
    def setSupports(self, supports):
        if supports not in self.supports:
            self.supports.append(supports)
        else:
            return
        
    def canDisintegrate(self):
        if len(self.supports) == 0:
            return True
        for above in self.supports:
            if len(above.supportedBy) < 2:
                return False
        return True
