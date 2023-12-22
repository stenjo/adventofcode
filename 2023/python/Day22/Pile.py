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

    def getLandingOn(self, brick):
        supporting = None
        for under in self.bricks:
            if under == brick:
                break
            if under.willSupport(brick):
                supporting = under

        return Brick("0,0,0~0,0,0") if supporting is None else supporting
