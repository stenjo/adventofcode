
from Day15.Hash import Hash

testData = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def test_Hash():
    
    assert Hash("") != None
    
    assert Hash("HASH").hash() == 52
    assert Hash("rn=1").hash() == 30
    assert Hash("cm-").hash() == 253
    assert Hash("ot=9").hash() == 9
    assert Hash("pc=6").hash() == 214
    assert Hash("ot=7").hash() == 231
    
    assert Hash(testData).sumOfHashes() == 1320
    
    inputData = open("../data/input15.txt", "r").read()
    assert Hash(inputData).sumOfHashes() == 505427
    
    
    assert Hash(testData).sumOfFocusingPower() == 145
    assert Hash(inputData).sumOfFocusingPower() == 243747
    