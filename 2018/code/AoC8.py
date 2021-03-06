# Advent of Code 2018: https://adventofcode.com/2018/day/8
# 
# 

import datetime, time
from datetime import timedelta
import pprint
import collections


DEBUG = False

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

if DEBUG:
    print(inData)

### PART 1 ###

def getNode(count, num, arr):   # children, metadata items and the array
    # print(count, num, arr)
    nodes = []
    meta  = []
    for c in range(count):
        nodes.append(getNode(arr.pop(0), arr.pop(0), arr))
    for n in range(num):
        meta.append(arr.pop(0))
    # nodes.insert(0,meta)

    # print(nodes)
    return [nodes, meta]

def sumNode(children, meta):
    sum = 0
    for item in children:
        sum += sumNode(item[0], item[1])

    for d in meta:
        sum += d

    return sum

data = []
sum = 0
part1 = inData[:]
data = getNode(part1.pop(0), part1.pop(0), part1)

if DEBUG:
    pp.pprint(data)

sum = sumNode(data[0], data[1])
        
# sum = sum([sum([i]) for i in r] for r in data)

print('\nPart 1: The sum of all metadata entries:', sum, '\n')

### PART 2 ###

def getNodeSum(children, metadata):   # children, metadata items and the array
    if DEBUG:
        print('Children:',children, 'Metadata:',metadata)
    sum = 0
    if len(children) > 0:
        for n in metadata:
            if n-1 < len(children):
                child = children[n-1]
                sum += getNodeSum(child[0], child[1])
                if DEBUG:
                    print('Got', sum, 'from child', child)
    else:
        if DEBUG:
            print(metadata)
        for n in metadata:
            sum += n

    return sum



part2 = inData[:]

pp.pprint(data)

sum = getNodeSum(data[0], data[1])

print('\nPart 2: the value of the root node is:',sum)


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.seconds, 'seconds and', duration.microseconds/1000,'ms\n')
