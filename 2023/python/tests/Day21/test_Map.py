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
    assert Map(inputData).tilesReachedInSteps(64) == 3658


# def test_Part2():
