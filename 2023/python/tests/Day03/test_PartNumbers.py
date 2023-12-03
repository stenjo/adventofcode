from Day03.PartNumbers import Schematic

lines = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598..",
]

def test_get_partNumbers():    
    assert Schematic(lines).partNumbers(["..."]) == []
    assert Schematic(lines).partNumbers(["1..","#.."]) == [1]
    assert Schematic(lines).partNumbers(["12.","#.."]) == [12]
    assert Schematic(lines).partNumbers([".12","#.."]) == [12]
    assert Schematic(lines).partNumbers([".12.","#..."]) == [12]
    assert Schematic(lines).partNumbers([".12.","...."]) == []
    assert Schematic(lines).partNumbers(["....","....", ".12."]) == []
    assert Schematic(lines).partNumbers(["....","....", ".12.","...."]) == []
    assert Schematic(lines).partNumbers(["....",".1..","..."]) == []
    assert Schematic(lines).partNumbers(["....",".1$.","..."]) == [1]
    assert Schematic(lines).partNumbers(["U...",".1..","..."]) == [1]
    assert Schematic(lines).partNumbers(["U...",".1.2","...."]) == [1]
    assert Schematic(lines).partNumbers(".1") == []
    assert Schematic(lines).partNumbers("1.1") == []
    assert Schematic(lines).partNumbers(".1.") == []
    
    assert Schematic(lines).partNumbers(lines[0:2]) == [467]
    assert Schematic(lines).partNumbers(lines) == [467,35,633,617,592,755, 664,598]
    
    assert sum(Schematic(lines).partNumbers(lines)) == 4361
    testData = open("../data/test_input03.txt", "r").readlines()
    assert sum(Schematic(lines).partNumbers(testData)) == 4361
    inputData = open("../data/input03.txt", "r").readlines()
    assert sum(Schematic(lines).partNumbers(inputData)) == 530495
    
def test_adjacentStar():
    assert Schematic([".1."]).partNumbers() == []
    assert Schematic([".1."]).getStarIndexes("...*...") == [3]
    assert Schematic([".1."]).getStarIndexes("...*.*.") == [3,5]
    
    assert Schematic([]).hasStar(["....",".1..","..."], 1, 0,4) == []
    assert Schematic([]).hasStar(["....",".*..","..."], 1, 0,4) == [(1,1)]
    assert Schematic([]).hasStar(["*...",".*.*","..."], 1, 0,4) == [(1,1),(1,3)]
    assert Schematic([]).hasStar(["*...",".*.*","..."], 0, 0,4) == [(0,0)]
    assert Schematic([]).hasStar(["*...",".*.*","..."], 1, 3,4) == [(1,3)]
    
    assert Schematic([]).hasAdjacentStar(["*...","....","...."], 1, 3,4) == []
    assert Schematic([]).hasAdjacentStar(["*...","...*","...."], 1, 0,4) == [(0,0),(1,3)]
    
    s = Schematic(lines[0:3])
    assert s.partNumbers() == [467,35]
    assert s.starMap == {(1, 3): [467, 35]}
    
    s = Schematic(lines)
    s.partNumbers()
    assert s.getGearRatioSum() == 467835
    
    inputData = open("../data/input03.txt", "r").readlines()
    s = Schematic(inputData)
    s.partNumbers()
    assert s.getGearRatioSum() == 80253814
