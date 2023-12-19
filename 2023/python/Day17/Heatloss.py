class HeatLoss:
    def __init__(self, input):
        self.city = [l.strip() for l in input]
        self.lossMap = {}
        self.dim = (len(self.city[0]), len(self.city)) if len(input) > 0 else (0, 0)

    def minHeatLoss(self, start=(0, 0)):
        (dimX, dimY) = self.dim
        steps = 0
        self.heatLoss(steps, start, dir, 0)
        (dimX, dimY) = self.dim
        (x, y) = start
        return (
            self.lossMap[(dimX - 1, dimY - 1)] - int(self.city[y][x])
            if (dimX - 1, dimY - 1) in self.lossMap.keys()
            else None
        )

    def heatLoss(self, steps, block, direction, loss):
        angles = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # angles = [(1, 0), (0, 1)]
        (x, y) = block
        (dimX, dimY) = self.dim
        if x < 0 or y < 0:
            return None
        if x >= dimX or y >= dimY:
            return None
        loss += int(self.city[y][x])
        if (x, y) in self.lossMap.keys():
            if (x, y) == (11, 11):
                self.lossMap[(x, y)] = self.lossMap[(x, y)]
            if self.lossMap[(x, y)] > 0:
                if loss < self.lossMap[(x, y)]:
                    self.lossMap[(x, y)] = loss
                return self.lossMap[(x, y)]
            if self.lossMap[(x, y)] == 0:
                return None
        if (x, y) == (dimX - 1, dimY - 1):
            self.lossMap[(x, y)] = loss
            return loss
        self.lossMap[(x, y)] = 0
        next = [(x + dx, y + dy) for (dx, dy) in angles]
        losses = [
            l for l in [self.heatLoss(steps + 1, n, dir, loss) for n in next] if l
        ]

        newLoss = (
            min(losses) + int(self.city[y][x])
            if len(losses)
            and (x, y) != (dimX - 1, dimY - 1)
            and self.lossMap[(x, y)] != 0
            else loss
        )
        self.lossMap[(x, y)] = newLoss
        return newLoss

    def getMinimumHeatLoss(self, start=(0,0)):
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        directions = [(1, 0), (0, 1)]
        blocks = [(start, 0)]
        for block,loss in blocks:
            (x, y) = block
            (dimX, dimY) = self.dim
            if x < 0 or y < 0:
                continue
            if x >= dimX or y >= dimY:
                continue

            if (x, y) not in self.lossMap.keys():
                self.lossMap[block] = loss + int(self.city[y][x])
                nextBlocks = [(x + dx, y + dy) for (dx, dy) in directions]
                for b in nextBlocks:
                    blocks.append((b, loss + int(self.city[y][x])))
            else:
                if loss < self.lossMap[block]:
                    self.lossMap[block] = loss
            
        return self.lossMap[(12,12)] - self.lossMap[start]