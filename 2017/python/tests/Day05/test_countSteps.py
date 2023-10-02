from Day05.instructionparser import countSteps, countSteps_decrease


def test_countSteps():
    
    assert countSteps([0,3,0,1,-3]) == 5
    
    inputData = open('../data/input5.txt','r')
    data = []
    for i in inputData.readlines():
        data.append(int(i.strip()))
    
    assert countSteps(data) == 359348
    
    
def test_countSteps_decrease():

    assert countSteps_decrease([0,3,0,1,-3]) == 10
    
    inputData = open('../data/input5.txt','r')
    data = []
    for i in inputData.readlines():
        data.append(int(i.strip()))
    
    assert countSteps_decrease(data) == 27688760
            
        