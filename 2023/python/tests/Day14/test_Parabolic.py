from Day14.Parabolic import Parabolic

testMap = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]


def test_Parabolic():
    assert Parabolic() != None

    assert len(Parabolic(testMap).dishMap) == 10
    assert sum(Parabolic(testMap).rolledNorth()) == 136

    inputData = open("../data/input14.txt", "r").readlines()
    assert sum(Parabolic(inputData).rolledNorth()) == 108889


def test_calculateLoad():
    assert Parabolic(testMap).calculateLoad(testMap) == 104

    p = Parabolic(testMap)
    assert p.calculateLoad(p.tilted(testMap)) == 136

    inputData = open("../data/input14.txt", "r").readlines()
    assert p.calculateLoad(p.tilted(inputData)) == 108889


def test_rotate():
    assert Parabolic(testMap).rotate(testMap)[0] == "##..O.O.OO"


def test_tilt():
    assert Parabolic(testMap).tilted(testMap)[0] == "OOOO.#.O.."


testDataAfter1 = """
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....""".strip().splitlines()

testDataAfter2 = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O""".strip().splitlines()

testDataAfter3 = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O""".strip().splitlines()


def test_cycles():
    assert Parabolic(testMap).runCycle()[9] == "#..OO#...."
    assert Parabolic(testMap).runCycle()[0] == ".....#...."
    p = Parabolic(testMap)
    dish = p.runCycle(testMap)
    assert not (set(map(tuple, dish)) ^ set(map(tuple, testDataAfter1)))
    dish = p.runCycle(dish)
    assert not (set(map(tuple, dish)) ^ set(map(tuple, testDataAfter2)))
    dish = p.runCycle(dish)
    assert not (set(map(tuple, dish)) ^ set(map(tuple, testDataAfter3)))

    assert Parabolic(testMap).cycles(3) == 69
    assert Parabolic(testMap).cycles(11) == 69
    assert Parabolic(testMap).cycles(18) == 69

    assert Parabolic(testMap).cycles(1000000000) == 64

    inputData = open("../data/input14.txt", "r").readlines()
    assert Parabolic(inputData).cycles(1000000000) == 104671
