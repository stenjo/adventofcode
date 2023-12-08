

from Day08.Node import NodeTree

testData = [
"RL",
"",
"AAA = (BBB, CCC)",
"BBB = (DDD, EEE)",
"CCC = (ZZZ, GGG)",
"DDD = (DDD, DDD)",
"EEE = (EEE, EEE)",
"GGG = (GGG, GGG)",
"ZZZ = (ZZZ, ZZZ)"
]

testData2 = [
"LLR",
"",
"AAA = (BBB, BBB)",
"BBB = (AAA, ZZZ)",
"ZZZ = (ZZZ, ZZZ)"
]

part2TestData = [
"LR",
"",
"11A = (11B, XXX)",
"11B = (XXX, 11Z)",
"11Z = (11B, XXX)",
"22A = (22B, XXX)",
"22B = (22C, 22C)",
"22C = (22Z, 22Z)",
"22Z = (22B, 22B)",
"XXX = (XXX, XXX)"
]

    
def test_part1():
    assert NodeTree(testData).nodes["AAA"] == ("BBB", "CCC")
    
    assert NodeTree(testData).navigateSteps() == 2
    assert NodeTree(testData2).navigateSteps() == 6
    
    inputData = open("../data/input08.txt", "r").readlines()
    assert NodeTree(inputData).navigateSteps() == 14893

def test_part2():
    assert len(NodeTree(part2TestData).getStartingNodes()) == 2    
    
    assert NodeTree(part2TestData).isEndNodes(["AAZ", "BBZ"]) == True
    assert NodeTree(part2TestData).isEndNodes(["AAZ", "BBB"]) == False
    
    assert NodeTree(part2TestData).navigateSeveralSteps() == 6
    
    inputData = open("../data/input08.txt", "r").readlines()
    assert NodeTree(inputData).navigateSeveralSteps() == 10241191004509
    