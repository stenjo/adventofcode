from Day21.Map import Map

testMap = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def test_Map():
    assert len(Map().map) == 0


def test_Part1():
    assert Map(testMap).tilesReachedInSteps(1) == 2
    assert Map(testMap).tilesReachedInSteps(2) == 4
    assert Map(testMap).tilesReachedInSteps(3) == 6
    assert Map(testMap).tilesReachedInSteps(6) == 16

    inputData = open("../data/input21.txt", "r").read()
    assert Map(inputData).tilesReachedInSteps(64) == 6613


# def test_Part2():
# m = Map(testMap)
# assert m.getTileLeft(m.map[(1, 1)]) == None
# assert m.getTileLeft(m.map[(2, 1)]).connector == "S"
# assert m.getTileAbove(m.map[(1, 1)]) == None
# assert m.getTileAbove(m.map[(1, 2)]).connector == "S"

# assert Map(testMap).countSteps() == 4

# assert Map(testMap).enclosedTiles() == 1

# inputData = open("../data/input21.txt", "r").readlines()
# assert Map(inputData).enclosedTiles() == 1
