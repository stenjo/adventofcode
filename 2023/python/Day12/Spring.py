from functools import reduce
from itertools import groupby
import re


class Spring:
    def __init__(self, input):
        self.pattern, groups = input.strip().split()
        self.groups = [int(group) for group in groups.split(',')]
        
    def generatePattern(self, length=3):
        p = ["".join(["."for c in range(length)])]
        for i in range(length):
            for pattern in p.copy():
                np = list(pattern)
                np[i] = "#"
                p.append("".join(np))
        return p
                    
    def options(self):
        optionGroups = list(filter(lambda x: '?' in x, [''.join(g) for _, g in groupby(self.pattern)]))
        options = []
        for o in optionGroups:
            options.append((o,self.generatePattern(len(o))))
        self.options = 0
        match = "^\.*"+"\.+".join(["#{"+str(n)+"}" for n in self.groups])+"\.*$"
        possibilities = 1
        for (_,p) in options:
            possibilities *= len(p)
        for i in range(possibilities):
            pattern = self.pattern
            shift = 0
            for (p,r) in options:
                pattern=pattern.replace(p,r[(i>>shift)%len(r)],1)
                shift += 1
            if re.search(match, pattern):
                self.options += 1   
        
        return self.options

class SpringStatus:
    def __init__(self,input):
        self.springMap = [Spring(line.strip()) for line in input if len(line.strip()) > 0]
        
    def getArrangementsSum(self):
        return sum([s.options() for s in self.springMap])