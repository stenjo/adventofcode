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
        startchar = chr(c)
        break

instr[startchar]=[]

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
        print(key, c, item)
        if c in item:
            item.remove(c)


result = ''

while len(instr):
    savedlen = len(instr)
    candidates = candidate(instr)
    if  len(candidates) == 0:
        break
    c = candidates[0]
    result += c
    remove(c,instr)
    del instr[c]

print(result, instr)    

exit()
def manhattan(item1, item2):
    return abs(item1[0] - item2[0]) + abs(item1[1] - item2[1])

# Returns [ [distance, item no in items] ]
# sorted on distance to ever
def manhattanArray(point, items):
    a = []
    for item in items:
        if point != item:
            a.append([manhattan(item, point),items.index(item)])
    # print(a)
    # return sorted(a)
    return sorted(a, key=lambda t:t[0])


maxX = 0
maxY = 0
candidates = []
for item in data:
    w = []
    n = []
    e = []
    s = []
    for comp in data:
        if comp != item:
            dist = manhattan(item, comp)
            if comp[0] < item[0]:
                w.append(int(dist/2))
            if comp[1] < item[1]:
                n.append(int(dist/2))
            if comp[0] > item[0]:
                e.append(int(dist/2))
            if comp[1] > item[1]:
                s.append(int(dist/2))

    if maxX < item[0]: maxX = item[0]
    if maxY < item[1]: maxY = item[1]

    if len(w)>0 and len(n)>0 and len(e)>0 and len(s)>0:
        candidates.append(data.index(item))        

# Alternative candidates
candidates2 = []
for item in data:
    tr = False
    tl = False
    br = False
    bl = False
    for comp in data:
        if comp != item:
            if comp[0] < item[0] and comp[1] < item[1]: tr = True 
            if comp[0] < item[0] and comp[1] > item[1]: br = True 
            if comp[0] > item[0] and comp[1] < item[1]: tl = True 
            if comp[0] > item[0] and comp[1] > item[1]: bl = True 

    if tr and tl and br and bl:
        candidates2.append(data.index(item))        
    

#Create a virual chronal grid
x = maxX+2
y = maxY+1
matrix = [[0] * x for i in range(y)]
for item in data:
    matrix[item[0]][item[1]] = str(data.index(item))

#Print it!
# print('Matrix:')
# for row in matrix:
#     print(' '.join([str(elem) for elem in row]))

maxNum = 0
for col in range(x):
    for j in range(y):
        points = manhattanArray([col,j],data)
        point = points[0]
        # print(points)
        if [col,j] in data:
            # print([col,j])
            if DEBUG:
                value = chr(ord('A')+data.index([col,j]))
            else:
                value = data.index([col,j])

            if maxNum < data.index([col,j]):
                maxNum = data.index([col,j])
        elif (points[0][0] == points[1][0]):
            value = '.'
        else:
            if DEBUG:
                value = chr(ord('a')+point[1])
            else:
                value = point[1]

        matrix[j][col] = value
        # print(matrix[j])
if DEBUG:
    # print('Matrix:')
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))

    print('items in list:',maxNum)

print('Candidates 1:', len(candidates))
print('Candidates 2:', len(candidates2))


patches = dict()
saveArea = 0
for num in candidates2:
    count = 0
    for col in range(x):
        for j in range(y):
            if DEBUG:
                if matrix[j][col].upper() == chr(ord('A')+num):
                    count += 1
            else:
                if matrix[j][col] == num:
                    count += 1

    if saveArea < count:
        saveArea = count

    if DEBUG:
        print('Found', count, 'occurrences of', chr(ord('A')+num))
    else:
        print('Found', count, 'occurrences of', num)
    
    patches[num] = count

patch = sorted(patches.items(), key = lambda t:t[1], reverse=True)[0][0]

pp.pprint(sorted(patches.items(), key = lambda t:t[1], reverse=True))

print('\nPart 1: The largest area not infinite is', saveArea)

# print('\nPart 2:', length,'units remain after removing',savedUnit, 'through optimized reduction')


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.microseconds/1000,'ms\n')
