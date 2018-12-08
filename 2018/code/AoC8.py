# Advent of Code 2018: https://adventofcode.com/2018/day/8
# 
# 

import datetime, time
from datetime import timedelta
import pprint
import collections


DEBUG = True

start = datetime.datetime.now()
pp = pprint.PrettyPrinter(width=180, compact=True)

inputData = open('../data/input8.txt','r')
testData = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
liveData = [int(c) for c in inputData.read().strip().split(' ')]

if DEBUG:
    inData = testData
    # inData = testData2
else:
    inData = liveData

print(inData)

### PART 1 ###

def getNode(count, num, arr):   # children, metadata items and the array
    # print(count, num, arr)
    nodes = []
    meta  = []
    for c in range(count):
        nodes += getNode(arr.pop(0), arr.pop(0), arr)
    for n in range(num):
        meta.append(arr.pop(0))
    nodes.insert(0,meta)

    # print(nodes)
    return nodes

data = []
sum = 0
part1 = inData[:]
data = getNode(part1.pop(0), part1.pop(0), part1)

if DEBUG:
    pp.pprint(data)

for i in data:
    for r in i:
        sum += r
        
# sum = sum([sum([i]) for i in r] for r in data)

print('\nPart 1: The sum of all metadata entries:', sum)



def getNodeSum(count, num, arr):   # children, metadata items and the array
    print(count, num, arr)
    sum = 0
    if count > 0:
        for c in range(count):
            sum += getNodeSum(arr.pop(0), arr.pop(0), arr)
    else:
        for n in range(num):
            p = arr.pop(0)
            if p <= len(data):
                for i in data[p-1]:
                    sum += i
                print(data[p-1])

    return sum


part2 = inData[:]

sum = getNodeSum(part2.pop(0), part2.pop(0), part2)

print('\nPart 2: the value of the root node is:',sum)


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.seconds, 'seconds and', duration.microseconds/1000,'ms\n')
