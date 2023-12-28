from Day13.Valley import Mirror, Valley

testPatterns = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

firstTestPattern = testPatterns.split("\n\n")[0].strip().splitlines()
secondTestPattern = testPatterns.split("\n\n")[1].strip().splitlines()

testPattern2 = """
.##.#..##.###
..##..####.##
##.##.###.###
.........#...
##.#...##....
...#..#...#..
####.#.####..
##..##.....##
#####..#..###""".strip().split(
    "\n"
)


def test_Valley():
    assert Valley("").patterns == [[]]
    assert len(Valley(testPatterns).patterns) == 2
    assert Valley(testPatterns).rowsByColumnsSum() == 405

    inputData = open("../data/input13.txt", "r").read()
    assert Valley(inputData).rowsByColumnsSum() == 36015


def test_Pattern():
    assert Mirror("").mirror == []
    assert len(Mirror(firstTestPattern).mirror) == 7


def test_isMirror():
    assert Mirror(firstTestPattern).isMirror("#.##..##.", 6) == False
    assert Mirror(firstTestPattern).isMirror("#.##..##.", 5) == True


def test_findCandidateSmudgedMirror():
    assert Mirror(firstTestPattern).findCandidateSmudgedMirror()[0] == (
        5,
        7,
    )
    assert Mirror(firstTestPattern).findCandidateSmudgedMirror()[1] == (
        1,
        5,
    )

    assert Mirror(firstTestPattern).findCandidateRow() == 3
    assert Mirror(secondTestPattern).findCandidateRow() == 1
    assert Mirror(firstTestPattern).findCandidateCol() == None
    assert Mirror(secondTestPattern).findCandidateCol() == None


def test_findMirrorRowAndColumn():
    assert Mirror(firstTestPattern).findMirrorCol() == 5
    assert Mirror(firstTestPattern).findMirrorRow() == None
    assert Mirror(secondTestPattern).findMirrorRow() == 4

    assert Mirror(testPattern2).findMirrorCol() == 12
    assert Mirror(testPattern2).findMirrorRow() == None


def test_findMirrorLines():
    assert Valley(testPatterns).smudgedRowsByColumnsSum() == 400

    inputData = open("../data/input13.txt", "r").read()
    assert Valley(inputData).smudgedRowsByColumnsSum() == 35335
