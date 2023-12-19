
from Day14.Parabolic import Parabolic

testMap=[
"O....#....",
"O.OO#....#",
".....##...",
"OO.#O....O",
".O.....O#.",
"O.#..O.#.#",
"..O..#O..O",
".......O..",
"#....###..",
"#OO..#...."
]

def test_Parabolic():
    assert Parabolic() != None

    assert len(Parabolic(testMap).dishMap) == 10
    assert Parabolic(testMap).boulderDist(0,0) == 10
    
    assert Parabolic(testMap).rolledNorth()[0] == 34
    assert Parabolic(testMap).rolledNorth()[1] == 27


    assert sum(Parabolic(testMap).rolledNorth()) == 136
    
    inputData = open("../data/input14.txt", "r").readlines()
    assert sum(Parabolic(inputData).rolledNorth()) == 108889
    
    p = Parabolic(testMap)
    p.rolledNorth()

    p.printMap(p.tiltedMap)    
    assert p.tiltedMap[-1] == "OOOO.#.O.."
    
    