
from functools import reduce


class BoatRace:
    def __init__(self, records):
        self.records = {}
        times = [int(n) for n in records[0].split(':')[1].split(' ') if n != ""]
        dist = [int(n) for n in records[1].split(':')[1].split(' ') if n != ""]
        print(dist)
        for idx, val in enumerate(times):
            self.records[val] = dist[idx]
        
        self.oneRace = (int(records[0].split(':')[1].replace(" ", "")), int(records[1].split(':')[1].replace(" ", "")))
            
    def calculateRange(self,pressedTime, totalTime):
        return (totalTime - pressedTime)*pressedTime
    
    def getWinningWays(self, raceLength, bestLength):
        i = 0
        for pressedTime in range(raceLength):
            if self.calculateRange(pressedTime, raceLength) > bestLength:
                i += 1
        return i
    
    def getWinnerPresses(self):
        return [self.getWinningWays(t,d) for (t,d) in self.records.items()]

    def getTotal(self):
        return reduce(lambda a, b: a*b, self.getWinnerPresses())
    
    def getTotalOneRace(self):
        return self.getWinningWays(self.oneRace[0], self.oneRace[1])