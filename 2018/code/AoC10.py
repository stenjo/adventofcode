# Advent of Code 2018: https://adventofcode.com/2018/day/10
# 
# 
import datetime, time
from datetime import timedelta
import pprint, re

DEBUG = True

start = datetime.datetime.now()
pp = pprint.PrettyPrinter(width=180, compact=True)


inputData = open('../data/input10.txt','r')
testData = open('../data/test10.txt','r')
liveData = inputData.readlines()

if DEBUG:
    inData = testData
else:
    inData = liveData

def getPosAndVelocity(line):
    parts = re.split('<|>',line)
    return [ [s.strip() for s in parts[1].split(',')], [s.strip() for s in parts[3].split(',')] ]

### PART 1 ###

class Point():
    c = []
    v = []
    def __init__(self, ptArr):
        self.c = ptArr[0]
        self.v = ptArr[1]

    def x(self):
        return self.c[0]

    def y(self):
        return self.c[1]
    
    def vx(self):
        return self.v[0]

    def vy(self):
        return self.v[1]

    def dump(self):
        pp.pprint([self.c,self.v])

    def getArr(self):
        return [self.c,self.v]

    def manhattan(self, pt):
        return abs(self.x()-pt.x())+abs(self.y() - pt.y())

    def moveOneSecond(self):
        self.c[0] += self.v[0]
        self.c[1] += self.v[1]
        return self


class SkyMap():
    map = []
    def load(self,data):
        for d in data:
            parts = re.split('<|>',d)
            self.map.append(Point([[s.strip() for s in parts[1].split(',')], [s.strip() for s in parts[3].split(',')]]))

    def dump(self):
        pp.pprint(self.map)
    
    def moveOneSecond(self):
        return map
    
    def getManhattanOfList(self):
        sum = 0
        return sum
    
    def getManhattanOfPoints(self, point1, point2):
        return point1.manhattan(point2)
    
    def __init__(self, data):
        self.load(data)


# sm = SkyMap(inData)
# sm.dump()

# print('\nPart 1: The largest area not infinite is', saveArea)

# print('\nPart 2: The region size is', count)


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.microseconds/1000,'ms\n')
