from Day10.Map import Map
# from Day10.solution import main

testMap = [".....", ".S-7.", ".|.|.", ".L-J.", "....."]
testMap2 = ["..F7.", ".FJ|.", "SJ.L7", "|F--J", "LJ..."]


def test_Map():
    assert len(Map().map) == 0
    assert len(Map(testMap).map) == 8

    assert Map(testMap).map[(1, 1)].connector == "S"
    assert Map(testMap).map[(1, 1)].next == [(2, 1), (1, 2)]
    assert Map(testMap).map[(2, 3)].connector == "-"
    assert Map(testMap).map[(2, 3)].next == [(1, 3), (3, 3)]


def test_Part1():
    assert Map(testMap).stepsToMostDistantPoint() == 4
    assert Map(testMap2).stepsToMostDistantPoint() == 8

    inputData = open("../data/input10.txt", "r").readlines()
    # assert main(inputData) == (6613, 511)
    # assert Map(inputData).stepsToMostDistantPoint() == 6613

    m = Map(testMap)
    assert m.getTileLeft(m.map[(1,1)]) == None
    assert m.getTileLeft(m.map[(2,1)]).connector == 'S'
    assert m.getTileAbove(m.map[(1,1)]) == None
    assert m.getTileAbove(m.map[(1,2)]).connector == 'S'
