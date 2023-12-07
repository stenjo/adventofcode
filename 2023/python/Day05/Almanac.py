from itertools import groupby

from Day05.SourceDestination import SourceDestination


class Almanac:
    def __init__(self, input):
        self.input = input.split("\n")
        self.sourceMap = {}
        if len(self.input) == 0:
            return
        if len(self.input[0]) == 0:
            return
        self.seeds = [int(n) for n in self.input[0].split(":")[1].split(" ") if n != ""]
        self.seedRange = [
            (self.seeds[i], self.seeds[i + 1])
            for i in range(len(self.seeds))
            if i % 2 == 0
        ]
        self.maps = [
            list(sub) for ele, sub in groupby(self.input[1::], key=bool) if ele
        ]
        for m in self.maps:
            source, dest = m[0].split(" ")[0].split("-to-")
            sdMap = SourceDestination()
            for n in m[1::]:
                sdMap.parseInput(n)
            self.sourceMap[(source, dest)] = sdMap

    def inSeeds(self, val):
        return True
    
    def getMap(self, source, num, dest):
        return self.sourceMap[(source, dest)].getMapped(num)

    def getChainedMap(self, source, num, dest):
        pairs = {s: d for (s, d) in self.sourceMap.keys()}
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

    def lowestSeedRangeLocation(self):
        if len(self.sourceMap) == 0:
            return 0
        
        for location in self.sourceMap[("humidity","location")].getDestRange():
            if self.getChainedSeed(location):
                return location

        return None
    
    
    def getChainedSeed(self, location):
        seedNo = self.getChainedSource("seed", location, "location")
        if self.inSeeds(seedNo):
            return True
        return False
    
    def getChainedSource(self, source, num, dest):
        pairs = {d: s for (s, d) in self.sourceMap.keys()}
        s = pairs[dest]
        val = self.reverseMap(s, num, dest)
        while s != source:
            val = self.reverseMap(pairs[s], val, s)
            s = pairs[s]
        return val
    
    def reverseMap(self, source, num, dest):
        return self.sourceMap[(source, dest)].getSource(num)
        
