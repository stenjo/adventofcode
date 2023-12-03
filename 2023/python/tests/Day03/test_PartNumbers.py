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
    