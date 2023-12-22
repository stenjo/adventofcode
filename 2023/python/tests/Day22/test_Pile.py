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

    assert Pile(testData).bricks[0].z == [1, 1] # A
    assert Pile(testData).bricks[1].z == [2, 2] # B
    assert Pile(testData).bricks[2].z == [2, 2] # C
    assert Pile(testData).bricks[3].z == [3, 3] # D
    assert Pile(testData).bricks[4].z == [3, 3] # E
    assert Pile(testData).bricks[5].z == [4, 4] # F
    assert Pile(testData).bricks[6].z == [5, 6] # G

    assert len(Pile(testData).bricks[0].supports) == 2
    assert len(Pile(testData).bricks[1].supportedBy) == 1
    assert len(Pile(testData).bricks[5].supportedBy) == 2 # F
    assert len(Pile(testData).bricks[6].supports) == 0
    
    assert Pile(testData).bricks[4].canDisintegrate() == True # E
    assert Pile(testData).bricks[5].canDisintegrate() == False # F
    assert Pile(testData).bricks[6].canDisintegrate() == True # G

def test_part1():
    assert Pile(testData).getBricksToSafelyDisintegrate() == 6