# Advent of Code 2018: https://adventofcode.com/2018/day/5
# 
# 
import datetime, time
from datetime import timedelta

start = datetime.datetime.now()

inputData = open('../data/input1.txt','r')
testData = ['1122','1111', '1234', '91212129']
testData2 = ['1212','1221', '123425', '123123', '12131415']
testResu2 = [6,0,4,12,4]

data = [inputData.readlines()[0].strip()]
# data = testData
# data = testData2

### PART 1 ###
for d in data:
    checksum = 0
    for i in range(len(d)):
        if d[i] == d[(i+1) % len(d)]:
            checksum += int(d[i])
            # print (int(d[i]), d[(i+1) % len(d)], 'index:', i, 'modulo', (i+1)%len(d), checksum)

    # print (d)
    print('\nPart 1: The checksum is', checksum)

### PART 2 ###
for d in data:
    checksum = 0
    offset = int(len(d)/2)
    for i in range(len(d)):
        if d[i] == d[(i+offset) % len(d)]:
            checksum += int(d[i])
            # print (int(d[i]), d[(i+1) % len(d)], 'index:', i, 'modulo', (i+1)%len(d), checksum)

    # print (d)
    # print('\nPart 2: The checksum is', checksum, 'correct:', testResu2[data.index(d)])
    print('\nPart 2: The checksum is', checksum)


# print('\nPart 2:', length,'units remain after removing',savedUnit, 'through optimized reduction')


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.microseconds/1000,'ms\n')
