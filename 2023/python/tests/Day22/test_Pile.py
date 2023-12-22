from Day22.Pile import Pile

testData = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def test_Pile():
    assert Pile().bricks == []

    assert Pile(testData).bricks[0].z == [1, 2]
    assert Pile(testData).bricks[1].z == [2, 3]
