
from Day18.DigPlan import DigPlan


testData = [
"R 6 (#70c710)",
"D 5 (#0dc571)",
"L 2 (#5713f0)",
"D 2 (#d2c081)",
"R 2 (#59c680)",
"D 2 (#411b91)",
"L 5 (#8ceee2)",
"U 2 (#caa173)",
"L 1 (#1b58a2)",
"U 2 (#caa171)",
"R 2 (#7807d2)",
"U 3 (#a77fa3)",
"L 2 (#015232)",
"U 2 (#7a21e3)"
]


def test_DigPlan():
 
    assert DigPlan(testData).plan[0] == ("R", 6, "(#70c710)")
    
    assert DigPlan(testData).dig((0,0), ("R", 6, "(#70c710")) == (6,0)
    assert DigPlan(testData).dig((0,0), ("U", 3, "(#a77fa3)")) == (0,-3)

    inputData = open("../data/input18.txt", "r").readlines()
    dp = DigPlan(testData)
    dp.trench()
    dp.print()
    dp.plotFilled()
    
    assert DigPlan(testData).trench() == 62
    
    # assert DigPlan(inputData).trench() == 62
    