from Day10.Map import Map

# from Day10.solution import main

testMap = """.....
.S-7.
.|.|.
.L-J.
....."""

testMap2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""


def test_Map():
    assert len(Map().map) == 0
    assert Map(testMap).map[(3, 3)].pipe == "J"

    assert Map(testMap).map[(1, 1)].pipe == "S"
    assert Map(testMap).map[(1, 1)].next == [(2, 1), (1, 2)]
    assert Map(testMap).map[(2, 3)].pipe == "-"
    assert Map(testMap).map[(2, 3)].next == [(1, 3), (3, 3)]


map1 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

map2 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

map3 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


def test_countInside():
    assert Map(testMap).countInside(2) == 1


def test_enclosedTiles():
    assert Map(testMap).enclosedTiles() == 1
    assert Map(testMap2).enclosedTiles() == 1
    assert Map(map1).enclosedTiles() == 4
    assert Map(map2).enclosedTiles() == 8
    assert Map(map3).enclosedTiles() == 10


def test_Part1():
    assert Map(testMap).stepsToMostDistantPoint() == 4
    assert Map(testMap2).stepsToMostDistantPoint() == 8

    inputData = open("../data/input10.txt", "r").read()
    assert Map(inputData).stepsToMostDistantPoint() == 6613


def test_Part2():
    inputData = open("../data/input10.txt", "r").read()
    assert Map(inputData).enclosedTiles() == 511
