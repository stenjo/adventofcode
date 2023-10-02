from Day06.MemoryReallocation import getRedistributions


def test_getRedistributions():
    
    assert getRedistributions([0,2,7,0]) == 5
    
    inputData = open('../data/input6.txt','r')
    data = []
    for i in inputData.read().split('\t'):
        data.append(int(i.strip()))
        
    assert getRedistributions(data) == 4074