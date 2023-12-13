
from Day13.Valley import Pattern, Valley

testPatterns = [
"#.##..##.",
"..#.##.#.",
"##......#",
"##......#",
"..#.##.#.",
"..##..##.",
"#.#.##.#.",
"",
"#...##..#",
"#....#..#",
"..##..###",
"#####.##.",
"#####.##.",
"..##..###",
"#....#..#"
]

testPattern2 = [
".#.#.####.#.#.##.",
"####......#######",
"####......#######",
".#.#.####.#.#.##.",
"....######....#..",
".#..........#.##.",
".#..##..##..#.#..",
"##.##.##.##.##..#",
"####..##..####...",
"#.##..##..##.####",
"#...#....#.#.###."
]

def test_Valley():
    
    assert Valley("").patterns == []
    assert len(Valley(testPatterns).patterns) == 2
    assert Valley(testPatterns).rowsByColumnsSum() == 405
    
    inputData = open("../data/input13.txt", "r").readlines()
    assert Valley(inputData).rowsByColumnsSum() == 36015
    
    

def test_Patten():
    
    assert Pattern("").map == []
    assert len(Pattern(testPatterns[:7]).map) == 7
    
    assert Pattern(testPatterns[:7]).isMirror("#.##..##.", 6) == False
    assert Pattern(testPatterns[:7]).isMirror("#.##..##.", 5) == True
    
    assert Pattern(testPatterns[:7]).findMirrorRow() == 5
    assert Pattern(testPatterns[:7]).findMirrorCol() == 0
    assert Pattern(testPatterns[8:]).findMirrorCol() == 4
    
    assert Pattern(testPattern2).findMirrorRow() == 0
    assert Pattern(testPattern2).findMirrorCol() == 2
    