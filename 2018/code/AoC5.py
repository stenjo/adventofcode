# Advent of Code 2018: https://adventofcode.com/2018/day/5
# 
# 


inputData = open('../data/input5.txt','r')
testData = 'dabAcCaCBAcCcaDA'

data = inputData.readlines()[0].replace('\n','')
# data = testData

def react(polymer):
    pos = 0
    deleted = True
    newstr = polymer
    while deleted:
        deleted = False
        for pos in range(len(polymer)-1):
            if (polymer[pos].islower() and (polymer[pos].upper() == polymer[pos+1])) or (polymer[pos].isupper() and (polymer[pos].lower() == polymer[pos+1])):
                unit = polymer[pos:pos+2]
                # newstr = polymer[:pos] + polymer[pos+2:]
                newstr = polymer.replace(unit,'')
                deleted = True
                # print('removed', unit, 'at pos', pos, 'New length:', len(newstr)) #, 'New string:', newstr)
                break
        polymer = newstr
    return polymer

reacted = react(data)

print('Part 1:', len(reacted),'units remain after reduction')

length = len(reacted)
unitlist = set(reacted.lower())
# print(unitlist)
savedUnit = ''

for c in unitlist:
    data = reacted.replace(c, '').replace(c.upper(), '')
    newstr = react(data)
    if length > len(newstr):
        length = len(newstr)
        savedUnit = c
        # print('removed', c, 'New length:', len(newstr))

print('Part 2:', length,'units remain after removing',savedUnit, 'through optimized reduction')



