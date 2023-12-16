
from Day11.StarMap import StarMap

testMap = [
"...#......",
".......#..",
"#.........",
"..........",
"......#...",
".#........",
".........#",
"..........",
".......#..",
"#...#....."
]

def test_StarMap():
    assert StarMap(testMap) != None
    assert StarMap(testMap).getGalaxies() == [(3, 0), (7, 1), (0, 2), (6, 4), (1, 5), (9, 6), (7, 8), (0, 9), (4, 9)]
    assert len(StarMap(testMap).getGalaxies()) == 9
    
    assert len(StarMap(testMap).getGalaxyPairs()) == 36
    assert StarMap(testMap).getGalaxyPairs()[(1,5),(4,9)] == 9
    assert StarMap(testMap).getGalaxyPairs()[(0,9),(4,9)] == 5
    assert StarMap(testMap).getGalaxyPairs(10)[(1,5),(4,9)] == 25
    
    assert StarMap(testMap).sumOfGalaxyDistances() == 374
    assert StarMap(testMap).sumOfGalaxyLargeDistances(1) == 374
    assert StarMap(testMap).sumOfGalaxyLargeDistances(10) == 1030
    assert StarMap(testMap).sumOfGalaxyLargeDistances(100) == 8410
    
    inputData = open("../data/input11.txt", "r").readlines()
    assert StarMap(inputData).sumOfGalaxyDistances() == 10033566
    assert StarMap(inputData).sumOfGalaxyLargeDistances(1000000) == 560822911938
    