# Advent of Code 2018: https://adventofcode.com/2018/day/6
# 
# 
import datetime, time
from datetime import timedelta
import pprint


start = datetime.datetime.now()

inputData = open('../data/input6.txt','r')
testData = ['1, 1','1, 6','8, 3','3, 4','5, 5','8, 9']
liveData = inputData.readlines()

inData = testData
# inData = testData2
# inData = liveData

### PART 1 ###
data = []
sum = 0
for i in range(len(inData)):
    r = inData[i].split(',')
    a = []
    for j in range(len(r)):
        a.append(int(r[j].strip()))
    sum += max(a) - min(a)
    data.append(sorted(a[:]))

pp = pprint.PrettyPrinter(width=180, compact=True)
pp.pprint(data)

def manhattan(item1, item2):
    return abs(item1[0] - item2[0]) + abs(item1[1] - item2[1])

def manhattanArray(item, array):
    a = [[0]*2]
    for i in array:
        if i != item:
            a.append([manhattan(item, i),array.index(i)])
    # return sorted(a)
    return sorted(a, key=lambda t:t[0])


savedArea = 0
maxX = 0
maxY = 0
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
        west = sorted(w)[0]
        north = sorted(n)[0]
        east = sorted(e)[0]
        south = sorted(s)[0]
        area = (west+east)*(north+south)
        if area > savedArea:
            savedArea = area

        print(item,west,north,east,south, area)

#Create a virual chronal grid
x = maxX + 2
y = maxY + 2
matrix = [[0] * y for i in range(x)]
for item in data:
    matrix[item[0]][item[1]] = str(data.index(item))

#Print it!
print('Matrix:')
for row in matrix:
    print(' '.join([str(elem) for elem in row]))

maxNum = 0
for i in range(maxX):
    for j in range(maxY):
        points = manhattanArray([i,j],data)
        point = points[1]
        print(points)
        if [i,j] in data:
            matrix[i][j] = data.index([i,j])
            if maxNum < data.index([i,j]):
                maxNum = data.index([i,j])
            # matrix[i][j] = '#'+str(data.index([i,j]))
        elif (points[1][0] == points[2][0]):
            matrix[i][j] = '.'
        else:
            matrix[i][j] = point[1]

print('Matrix:')
for row in matrix:
    print(' '.join([str(elem) for elem in row]))

print(maxNum)

for num in range(maxNum):
    count = 0
    for i in range(maxX):
        for j in range(maxY):
            if matrix[i][j] == num:
                count += 1
    print('Found', count, 'occurrences of', num)

exit()

print('\nPart 1: The largest area not infinite is', saveArea)


print('\nPart 2:', length,'units remain after removing',savedUnit, 'through optimized reduction')


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.microseconds/1000,'ms\n')
