from Day19.Part import Part
from Day19.Sorter import Sorter


testData = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


def test_Part():
    assert Part("{a=45}").rating["a"] == 45
    assert Part("{x=2127,m=1623,a=2188,s=1013}").rating["m"] == 1623
    assert len(Part("{x=2127,m=1623,a=2188,s=1013}").rating) == 4


def test_Sorter():
    assert len(Sorter(testData).parts) == 5
    assert len(Sorter(testData).workflows) == 11
    assert Sorter(testData).workflows["in"] == ["s<1351:px", "qqz"]

    assert len(Sorter(testData).run()) == 3

    assert Sorter(testData).ratingsOfAccepted() == 19114

    inputData = open("../data/input19.txt", "r").read()
    assert Sorter(inputData).ratingsOfAccepted() == 397134

    # assert Sorter(inputData).getDistinctCombinations() == 167409079868000
