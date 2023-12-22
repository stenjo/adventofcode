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
            self.x[1] - self.x[0] + 1,
            self.y[1] - self.y[0] + 1,
            self.z[1] - self.z[0] + 1,
        )

    def overlaps(self, brick):
        dimX = set(range(self.x[0], self.x[1] + 1))
        brickDimX = set(range(brick.x[0], brick.x[1] + 1))
        if brickDimX.intersection(dimX):
            return True
        dimY = set(range(self.y[0], self.y[1] + 1))
        brickDimY = set(range(brick.y[0], brick.y[1] + 1))
        if brickDimY.intersection(dimY):
            return True
        return False

    def willSupport(self, brick):
        if self.overlaps(brick) and self.z[1] < brick.z[0]:
            return True
        return False

    def setHeight(self, height):
        (_, _, dimZ) = self.dim
        self.z[0] = height + 1
        self.z[1] = height + 1 + dimZ

    def top(self):
        return self.z[1]
