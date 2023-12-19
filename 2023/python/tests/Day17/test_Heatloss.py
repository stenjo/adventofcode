from Day17.Heatloss import HeatLoss

testData = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533",
]


def test_Part1():
    assert HeatLoss([]) != None
    assert HeatLoss(testData).dim == (13, 13)
    # assert HeatLoss(testData).minHeatLoss() == 102


def test_heatLoss():
    assert HeatLoss(testData).heatLoss(0, (12, 12), (1, 0), 0) == 3
    assert HeatLoss(testData).heatLoss(0, (13, 12), (1, 0), 0) == None
    assert HeatLoss(testData).heatLoss(0, (12, -1), (1, 0), 0) == None
    assert HeatLoss(testData).heatLoss(0, (-1, 12), (1, 0), 0) == None
    # assert HeatLoss(testData).minHeatLoss((11, 12)) == 3
    # assert HeatLoss(testData).minHeatLoss((11, 10)) == 9

def test_getMinimumHeatLoss():
    
    assert HeatLoss(testData).getMinimumHeatLoss((11,12)) == 3
    assert HeatLoss(testData).getMinimumHeatLoss((10,12)) == 6