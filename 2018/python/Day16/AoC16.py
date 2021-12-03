# Advent of Code 2018: https://adventofcode.com/2018/day/16
# 
# Main file

import datetime, time
from datetime import timedelta

from AoC16_classes import OpCodes
start = datetime.datetime.now()


inputData = open('../../data/input16.txt','r')
liveData = inputData.readlines()

oc = OpCodes()
oc.load(liveData)
result = oc.findSamples()


print('\nPart 1: The number of samples behaving like three or more opcodes is', result)

# print('\nPart 2: The location of the last cart is', cart.print())

end = datetime.datetime.now()
duration = end-start
print('Completed in {0:02d}:{1:02d}:{2:02.5f}\n'.format(int(duration.seconds/3600), int(duration.seconds/60),duration.seconds%60 + duration.microseconds/1000000))
