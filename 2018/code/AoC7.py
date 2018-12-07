# Advent of Code 2018: https://adventofcode.com/2018/day/7
# 
# 

import datetime, time
from datetime import timedelta
import pprint
import collections


DEBUG = False

start = datetime.datetime.now()
pp = pprint.PrettyPrinter(width=180, compact=True)

inputData = open('../data/input7.txt','r')
testData = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.']
liveData = inputData.readlines()

if DEBUG:
    inData = testData
    # inData = testData2
else:
    inData = liveData

### PART 1 ###
data = []
sum = 0
for item in inData:
    r = item.split(' ')
    data.append([r[7].strip(),r[1].strip()])

if DEBUG:
    pp.pprint(data)


instr = dict()

for item in sorted(data, key = lambda k:k[0]):
    if item[0] in instr:
        instr[item[0]].append(item[1])
    else:
        instr[item[0]] = [item[1]]


if DEBUG:
    pp.pprint(instr)

startchar = 'A'

for c in range(ord('A'), ord(max(instr.keys()))+1):
    if chr(c) not in instr.keys():
        instr[chr(c)]=[]
        
print(instr)

def candidate(l):
    cand = []
    for key,item in l.items():
        # print(key, len(item))
        if len(item) == 0:
            cand.append(key)
    return sorted(cand)

def remove(c, l):
    for key,item in l.items():
        # print(key, c, item)
        if c in item:
            item.remove(c)


result = ''
workers = dict()
seconds = 0
while len(instr) or max(workers) > 0:
    removeKeys = []

    for key, value in workers.items():        
        if value > 0:
            workers[key] = value-1
        else:
            removeKeys.append(key)

    # print (removeKeys, workers)
    for k in removeKeys:
        result += k
        remove(k,instr)
        del instr[k]
        del workers[k]

    
    candidates = candidate(instr)
    # print(workers, candidates)
    # print('Candidates:',candidates)
    for c in candidates:
        if len(workers) < 5 and c not in workers.keys():
            workers[c] = ord(c) - ord('A') + 60

    # print(seconds, workers, result,'\n')
    seconds += 1

    if len(workers) == 0:
        break

print('\nPart 1: The correct sequence of assembly is:', result)

print('\nPart 2: It takes', seconds-1, ' seconds to assemble using 5 workers')


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.seconds, 'seconds and', duration.microseconds/1000,'ms\n')
