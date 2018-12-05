# Advent of Code 2018: https://adventofcode.com/2018/day/4
import datetime, time
from datetime import timedelta
import collections

start = datetime.datetime.now()

inputData = open('../data/input4.txt','r')
#inputData = open('test4.txt','r')

data = inputData.readlines()
lines = collections.OrderedDict()
guards = dict()
sleepTime = dict()
guardNo = 0
dt = 0
for line in data:
    l = line.replace('[','').split(']')
    date = l[0]
    log = l[1].strip().replace('\n','').split(' ')
    
    t = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
    lines[l[0]] = log
    
print('Input data:', len(lines), 'lines read')
print()

for dt, log in sorted(lines.items(), key=lambda t:t[0]):
    t = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M')
    if log[0] == 'Guard':
        guardNo = log[1]
    elif log[0] == 'falls':
        t0 = t 
    elif log[0] == 'wakes':
        t1 = t - t0
        # guards.append([guardNo, t1.seconds/60])
        # total = guards.get(guardNo, 0) + t1.seconds/60
        guards[guardNo] = guards.get(guardNo, 0) + t1.seconds/60
        sleepTime[dt] = [t0.minute, t.minute,  t1.seconds/60, guardNo]


guard = sorted(guards.items(), key = lambda t:t[1], reverse=True)[0][0]


def filterGuard(guardNo, guardList):
    result = dict()
    for k,v in guardList.items():
        if k == guardNo:
            result[k]=v

    return result


#filteredSleepTimes = dict(filter(lambda x: x == guard, sleepTime))
# filteredSleepTimes = filterGuard(guard, sleepTime)

savedMinute = 0
savedSleepCount = 0
asleepAtTime = 0
for minute in range(60):
    sleepCount = 0
    for key,times in sleepTime.items():
        # print('range ', range(times[0]-1, times[1]+1))
        if minute in range(times[0], times[1]) and times[3] == guard:
            sleepCount += 1
            # print(minute, key, times[3])

    if sleepCount > savedSleepCount:
        savedSleepCount = sleepCount
        asleepAtTime = minute

print('Part 1: Guard', guard, 'is most frequently asleep at', asleepAtTime, 'minutes of the midnight hour')
print('solution is:', int(guard.replace('#',''))*asleepAtTime)

savedGuard = ''
savedSleepCount = 0
savedMinute = 0
for guard in guards.keys():
    guardSleepCount = 0
    for minute in range(60):
        sleepCount = 0
        for key,times in sleepTime.items():
            # print('range ', range(times[0]-1, times[1]+1))
            if minute in range(times[0], times[1]) and times[3] == guard:
                sleepCount += 1
                # print(minute, key, times[3])

        if sleepCount > guardSleepCount:
            guardSleepCount = sleepCount
            asleepAtTime = minute

    if guardSleepCount > savedSleepCount:
        savedSleepCount = guardSleepCount
        savedGuard = guard
        savedMinute = asleepAtTime
        
    # print(guard, guardSleepCount, savedSleepCount)

print('Part 2: Guard', savedGuard, 'is most frequently asleep at', savedMinute, 'minutes of the midnight hour')
print('solution is:', int(savedGuard.replace('#',''))*savedMinute)

#print(filteredSleepTimes)
# print(sorted(lines.items(), key=lambda t:t[0]))
# print(sleepTime)


# dt = datetime.datetime.fromtimestamp(time.asctime)
# print(dt)
# print('hour       :', dt.hour)
# print('minute     :', dt.minute)
# print('second     :', dt.second)
# print('microsecond:', dt.microsecond)
# print('tzinfo     :', dt.tzinfo)
end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.microseconds/1000,'ms')