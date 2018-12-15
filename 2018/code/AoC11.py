# Advent of Code 2018: https://adventofcode.com/2018/day/10
# 
# 
import datetime, time
from datetime import timedelta
import pprint, re
from AoC11_classes import FuelCells

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


fc = FuelCells(1309)

print('\nPart 1: The X,Y coordinate of the top-left fuel cell of the 3x3 square with the largest total power is', fc.maxPower(3))

print('\nPart 2: The X,Y,size identifier of the square with the largest total power is', fc.maxPowerSize())


end = datetime.datetime.now()
duration = end-start
print('Completed in {0:02d}:{1:02d}:{2:02.5f}\n'.format(int(duration.seconds/3600), int(duration.seconds/60),duration.seconds%60 + duration.microseconds/1000000))
