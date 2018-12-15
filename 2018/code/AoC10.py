# Advent of Code 2018: https://adventofcode.com/2018/day/10
# 
# 
import datetime, time
from datetime import timedelta
import pprint, re
from AoC10_classes import SkyMap

DEBUG = False

start = datetime.datetime.now()
pp = pprint.PrettyPrinter(width=180, compact=True)


inputData = open('../data/input10.txt','r')
outData = open('../data/output10.txt','w')
testData = open('../data/test10.txt','r')
liveData = inputData.readlines()

if DEBUG:
    inData = testData.readlines()
else:
    inData = liveData


### PART 1 ###


sm = SkyMap()
sm.getlines(inData)
print('X:',sm.MinX,'-',sm.MaxX)
print('Y:',sm.MinY,'-',sm.MaxY)
sm.play()
sm.plot()

# print('\nPart 1: The largest area not infinite is', saveArea)

# print('\nPart 2: The region size is', count)


end = datetime.datetime.now()
duration = end-start
print('Completed in {0:02d}:{1:02d}:{2:02.5f}\n'.format(int(duration.seconds/3600), int(duration.seconds/60),duration.seconds%60 + duration.microseconds/1000000))
