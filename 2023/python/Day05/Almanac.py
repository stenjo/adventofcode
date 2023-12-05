from itertools import groupby

from Day05.SourceDestination import SourceDestination


class Almanac:
    def __init__(self, input):
        self.input = input.split("\n")
        self.sourceMap = {}
        if len(self.input) == 0: return
        if len(self.input[0]) == 0: return
        self.seeds = [int(n) for n in self.input[0].split(':')[1].split(' ') if n != '']
        self.maps = [list(sub) for ele, sub in groupby(self.input[1::], key = bool) if ele]
        for m in self.maps:
            source, dest = m[0].split(' ')[0].split('-to-')
            sdMap = SourceDestination()
            for n in m[1::]:
                sdMap.parseInput(n)
            self.sourceMap[(source,dest)]=sdMap
            
    def getMap(self, source, num, dest):
        if num in self.sourceMap[(source,dest)].items().keys():
            return self.sourceMap[(source,dest)].items()[num]
        else:
            return num
        
    def getChainedMap(self, source, num, dest):
        pairs = {s:d for (s,d) in self.sourceMap.keys()}
        d = pairs[source]
        val = self.getMap(source, num, d)
        while d != dest:
            val = self.getMap(d, val, pairs[d])
            d = pairs[d]
        
        return val
            
        
    def lowestLocation(self):
        locationNums = []
        if len(self.sourceMap) == 0:
            return 0
        
        for s in self.seeds:
            locationNums.append(self.getChainedMap("seed", s, "location"))
        
        locationNums.sort()
        
        return locationNums[0]
    