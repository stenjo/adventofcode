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

inputData = open("../data/input21.txt", "r").read()

def test_Map():
    assert len(Map().map) == 4


def test_Part1():
    assert Map(testMap).tilesReachedInSteps(1) == 2
    assert Map(testMap).tilesReachedInSteps(2) == 4
    assert Map(testMap).tilesReachedInSteps(3) == 6
    assert Map(testMap).tilesReachedInSteps(6) == 16

    assert Map(inputData).tilesReachedInSteps(64) == 3658


def test_Part2():
    
    assert Map(testMap).tilesReachedInSteps(6) == 16
    assert Map(testMap).tilesReachedInSteps(10) == 50
    assert Map(testMap).tilesReachedInSteps(50) == 1594
    assert Map(testMap).tilesReachedInSteps(100) == 6536
    assert Map(testMap).tilesReachedInSteps(500) == 167004
    
    assert Map(inputData).tilesReachedInSteps(64) == 3658
    
