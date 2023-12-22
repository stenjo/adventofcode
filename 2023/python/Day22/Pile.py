from itertools import count
from Day22.Brick import Brick


class Pile:
    def __init__(self, input=""):
        self.bricks = sorted(
            [Brick(line) for line in input.strip().split("\n") if input],
            key=lambda x: x.z[0],
        )

        # land the bricks
        for brick in self.bricks:
            below = self.getLandingOn(brick)
            brick.setHeight(below.top())
            below.isSupporting(brick)

    def getLandingOn(self, brick):
        supporting = None
        for under in self.bricks:
            if under == brick:
                break
            if under.overlaps(brick):
                supporting = under

        return Brick("0,0,0~0,0,0") if supporting is None else supporting

    def getBricksToSafelyDisintegrate(self):
        count = 0
        for b in self.bricks:
            if b.canDisintegrate():
                count += 1
        
        return count