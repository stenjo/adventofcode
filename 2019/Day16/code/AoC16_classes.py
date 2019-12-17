# Advent of Code 2019: https://adventofcode.com/2019/day/16
# 
# 

class Pattern():

    pos = 0
    basePattern = None
    def __init__(self, pattern):
        super().__init__()
        self.basePattern = pattern

    def Digit(self, elmnt):
        p = self.ExpandedPattern(elmnt)
        return p[pos]

    def ExpandedPattern(self, elmntNo):
        pattern = []
        for p in range(len(self.basePattern)):
            for n in range(elmntNo+1):
                pattern.append(self.basePattern[p])

        return pattern

class FFT():

    ptrn = None
    signal = []
    multiplier = 1

    def __init__(self, pattern, signal, multiplier = 1):
        super().__init__()
        self.ptrn = Pattern(pattern)
        self.signal = [int(n) for n in list(str(signal))]
        self.multiplier = multiplier
        
    def RunPhase(self, count, offset = 0):
        for c in range(count):
            newlist = []
            for elmntNo in range(len(self.signal)):
                sum = 0
                pattern = self.ptrn.ExpandedPattern(elmntNo)
                for i in range(len(self.signal)):
                    val = self.signal[i] * pattern[(i+1) % len(pattern)]
                    sum += val 

                newlist.append(abs(sum)%10)
            
            self.signal = newlist
            
        return ''.join(str(x) for x in [self.signal[i] for i in range(offset, offset+8)])

    def RunPhaseWithOffset(self, count, offset=0):
        for c in range(count):
            newlist = []
            for elmntNo in range(len(self.signal)):
                sum = 0
                pattern = self.ptrn.ExpandedPattern(elmntNo)
                for i in range(len(self.signal)):
                    val = self.signal[i] * pattern[(i+1) % len(pattern)]
                    sum += val 

                newlist.append(abs(sum)%10)
            
            self.signal = newlist
            
        return ''.join(str(x) for x in [self.signal[i] for i in range(len(self.signal))])

