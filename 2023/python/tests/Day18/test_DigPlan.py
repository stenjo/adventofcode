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
    "U 2 (#7a21e3)",
]


def test_DigPlan():
    assert DigPlan(testData).plan[0] == ("R", 6, "(#70c710)")
    assert DigPlan(testData).fill() == 62

    inputData = open("../data/input18.txt", "r").readlines()
    assert DigPlan(inputData).fill() == 39194

    assert DigPlan(testData).hexFill() == 952408144115
    assert DigPlan(inputData).hexFill() == 78242031808225
