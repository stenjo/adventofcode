# Advent of Code 2018: https://adventofcode.com/2018/day/5
# 
# 
import datetime, time
import pprint

from datetime import timedelta

start = datetime.datetime.now()

inputData = open('../data/input2.txt','r')
liveData = inputData.readlines()

testData = ['5\t1\t9\t5','7\t5\t3', '2\t4\t6\t8']
testData2 = ['5\t9\t2\t8','9\t4\t7\t3', '3\t8\t6\t5']

# inData = testData
# inData = testData2
inData = liveData


### PART 1 ###
data = []
sum = 0
for i in range(len(inData)):
    r = inData[i].split('\t')
    a = []
    for j in range(len(r)):
        a.append(int(r[j].strip()))
    sum += max(a) - min(a)
    data.append(sorted(a[:]))

pp = pprint.PrettyPrinter(width=180, compact=True)
pp.pprint(data)

print('\nPart 1: The sum is', sum)


### PART 2 ###
sum = 0
for row in data:
    for i in range(len(row)):
        for j in range(len(row)):
            if (i != j) and (row[i]%row[j] == 0):
                sum += int(row[i]/row[j])

print('\nPart 2: The sum is', sum)


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.microseconds/1000,'ms\n')
