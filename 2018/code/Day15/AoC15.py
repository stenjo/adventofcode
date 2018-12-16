# Advent of Code 2018: https://adventofcode.com/2018/day/15
# 
# Main file

import datetime, time
from datetime import timedelta

from AoC15_classes import BeverageBandidts
start = datetime.datetime.now()


inputData = open('../../data/input15.txt','r')
liveData = inputData.readlines()

bb = BeverageBandidts()
bb.load(liveData)

scores = bb.getScores()

print('\nPart 1: The outcome of the combat is', inputData, 'is', scores)

# print('\nPart 2: The location of the last cart is', cart.print())

end = datetime.datetime.now()
duration = end-start
print('Completed in {0:02d}:{1:02d}:{2:02.5f}\n'.format(int(duration.seconds/3600), int(duration.seconds/60),duration.seconds%60 + duration.microseconds/1000000))
