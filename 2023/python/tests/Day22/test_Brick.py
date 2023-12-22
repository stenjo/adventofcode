from Day22.Brick import Brick

b = [
    "1,0,1~1,2,1",  # <- A
    "0,0,2~2,0,2",  # <- B
    "0,2,3~2,2,3",  # <- C
    "0,0,4~0,2,4",  # <- D
    "2,0,5~2,2,5",  # <- E
    "0,1,6~2,1,6",  # <- F
    "1,1,8~1,1,9",  # <- G
]


def test_Brick():
    assert Brick().x == []
    assert Brick("1,0,1~1,2,1\n").x == [1, 1]
    assert Brick("1,0,1~1,2,1").y == [0, 2]
    assert Brick("1,0,1~1,2,1").z == [1, 1]

    assert (
        Brick(b[0]).willSupport(Brick(b[1])) == True
    )  # Brick A is the only brick supporting bricks B and C.
    assert (
        Brick(b[0]).willSupport(Brick(b[2])) == True
    )  # Brick A is the only brick supporting bricks B and C.

    assert Brick(b[3]).willSupport(Brick(b[5])) == True  # Brick D supports brick F.
    assert (
        Brick(b[6]).willSupport(Brick(b[5])) == False
    )  # Brick G isn't supporting any bricks
