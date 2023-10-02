

def getRedistributions(banks):
    
    distLog = []
    cycles = 0
    distLog.append('_'.join(str(x) for x in banks))
    
    while True:
        pos = banks.index(max(banks))
        points = banks[pos]
        banks[pos] = 0
        for i in range(points):
            banks[(pos+i+1)%len(banks)] +=1
        
        cycles += 1    
        if '_'.join(str(x) for x in banks) in distLog:
            return cycles
        
        distLog.append('_'.join(str(x) for x in banks))
