# Advent of Code 2018: https://adventofcode.com/2018/day/3
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2

import pprint
import datetime, time
from datetime import timedelta

start = datetime.datetime.now()

inputData = open('../data/input3.txt','r')
testData = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

data = inputData.readlines()
# data = testData

rquests = dict()
requestkeys = []
maxX = 0
maxY = 0
for item in data:
    id, at, pos, size = item.replace(':','').split(' ') 
    x,y = pos.split(',')
    w,h = size.split('x')
    patches = []
    for posx in range(int(x)+1, int(x)+int(w)+1):
        for posy in range(int(y)+1,int(y)+int(h)+1):
            patches.append([posx, posy])
            if maxX < posx:
                maxX = posx
            if maxY < posy:
                maxY = posy

    rquests[id] = patches
    requestkeys.append(id)

pp = pprint.PrettyPrinter(width=180, compact=True)
# pp.pprint(rquests)

#Create a virual fabric sheet map
patchCount = 0
patchRequired = 0
x = maxX + 1
y = maxY + 1
matrix = [[0] * y for i in range(x)]
for key, value in rquests.items():
    for item in value:
        matrix[item[0]][item[1]] += 1

#Print it!
# print('Matrix:')
# for row in matrix:
#     print(' '.join([str(elem) for elem in row]))

#Find counts
for i in range(x):
    for j in range(y):
        if matrix[i][j] > 1:
            patchCount += 1
        if matrix[i][j] > 0:
            patchRequired += 1

for key, value in rquests.items():
    for item in value:
        if matrix[item[0]][item[1]] != 1:
            if key in requestkeys:
                requestkeys.remove(key)
            break
    

print('\nPart 1:', patchCount, 'square inches of fabric are within two or more claims')
print(patchRequired, 'square inches of sheet requested. Sheet size is:', maxX+1, 'width by', maxY+1, 'height')
print('\nPart 2: Request', requestkeys, 'is the only request intact\n')
end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.microseconds/1000,'ms')
