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
    inData = testData.readlines()
else:
    inData = liveData


### PART 1 ###


class FuelCells():
    Map = []
    GridSerialNo = 0
    def __init__(self, gsn):
        self.initialize(gsn)

    def initialize(self, gsn):
        self.Map.clear()
        self.GridSerialNo = gsn
        for x in range(300):
            col = []
            for y in range(300):
                col.append(self.calPowerLevel(x+1, y+1))
            self.Map.append(col)


    def calPowerLevel(self,x,y):
        rackId = x+10
        # print(rackId)
        pLevel = (rackId * y + self.GridSerialNo) * rackId
        pLevel = int(pLevel/100)
        if pLevel > 0:
            return  (pLevel % 10) - 5
        return -5

    def getPowerLevel(self,x,y):
        return self.Map[x-1][y-1]

    def totalPower(self,x,y,matrix,size):
        sum = 0
        for m in range(y,y+size):
            for n in range(x,x+size):
                sum += matrix[n-1][m-1]
        return sum

    def maxPower(self, size):
        position = [0,0,0,0] 
        power = 0
        for x in range(1,301-size):
            for y in range(1,301-size):
                p = self.totalPower(x,y,self.Map,size)
                if p > power:
                    power = p
                    position = [x,y,size,p]
        return position

    def maxPowerSize(self):
        savedMax =  [0,0,0,0]
        for size in range(1,300):
            p = self.maxPower(size)
            # print(p,savedMax)
            if p[3] > savedMax[3]:
                savedMax = p
            if all(x == 0 for x in p) == True:
                return savedMax
        return savedMax

    def print3x3(self, x, y, matrix):
        print('\n')
        for c in range(y-2,y+3+2):
            row = []
            for r in range(x-2,x+3+2):
                row.append(matrix[r-1][c-1])
            print(' '.join([str(elem).rjust(2) for elem in row]))

fc = FuelCells(1309)

print('\nPart 1: The X,Y coordinate of the top-left fuel cell of the 3x3 square with the largest total power is', fc.maxPower(3))

print('\nPart 2: The X,Y,size identifier of the square with the largest total power is', fc.maxPowerSize())


end = datetime.datetime.now()
duration = end-start
print('Completed in {0:02d}:{1:02d}:{2:02.5f}\n'.format(int(duration.seconds/3600), int(duration.seconds/60),duration.seconds%60 + duration.microseconds/1000000))
