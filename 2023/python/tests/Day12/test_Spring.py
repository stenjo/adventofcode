
from Day12.Spring import Spring, SpringStatus

testData = [
"???.### 1,1,3",
".??..??...?##. 1,1,3",
"?#?#?#?#?#?#?#? 1,3,1,6",
"????.#...#... 4,1,1",
"????.######..#####. 1,6,5",
"?###???????? 3,2,1"
]

def test_Spring():
    assert Spring("???.### 1,1,3").groups == [1,1,3]
    
    assert Spring("???.### 1,1,3").options() == 1
    assert Spring(".??..??...?##. 1,1,3").options() == 4
    assert Spring("?#?#?#?#?#?#?#? 1,3,1,6").options() == 1
    assert Spring("????.#...#... 4,1,1").options() == 1
    assert Spring("????.######..#####. 1,6,5").options() == 4
    assert Spring("?###???????? 3,2,1").options() == 10

def test_SpringStatus():
    assert SpringStatus(testData) != None
    assert SpringStatus(testData).getArrangementsSum() == 21
    
    inputData = open("../data/input12.txt", "r").readlines()
    # assert SpringStatus(inputData).getArrangementsSum() == 6958
    