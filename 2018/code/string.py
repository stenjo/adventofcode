# Testing string handling in Python
# well... actually solution to Day 12 but not very pretty

# initial = '#..#.#..##......###...###...........'
initial = '##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#.'
# patternstrings = [  '...## => #','..#.. => #','.#... => #','.#.#. => #','.#.## => #','.##.. => #','.#### => #','#.#.# => #','#.### => #','##.#. => #','##.## => #','###.. => #','###.# => #','####. => #']
patternstrings = ['.#.#. => #','.#... => #','##### => #','#..#. => #','#...# => #','###.# => #','...## => #','#.##. => #','.#.## => #','##.#. => #','..### => #','###.. => #','##..# => #','#..## => #']

patterns = [ p.split(' => ')[0] for p in patternstrings]
print(patterns)
offset = 12000
generationstring = '.'*offset+initial+'.'*offset
count = initial.count('#')
savedSum = 0
numPots = 0
savedResult = 0
# print('{0:2d}: {1:s}'.format(0,generationstring[offset:]))
for n in range(1,1101):
    nextGenString ="."*len(initial)
    length = len(initial)
    potsum = 0
    first = length
    maxi = 0
    count = 0
    for i in range(-offset,length+offset+10):
        # print(generationstring[i-2:i+3], generationstring[i-2:i+3] in patterns)
        if i > 1-offset and i < length + 3 + offset:
            pattern = generationstring[i-2+offset:i+3+offset]
            if pattern in patterns:
                nextGenString = nextGenString[:i+offset]+'#'+nextGenString[i+1+offset:]
                count +=1
                potsum += i
                if first > i: first = i
                if maxi < i: maxi = i
            else:
                nextGenString = nextGenString[:i+offset]+'.'+nextGenString[i+1+offset:]


    nextGenString += '.' * (length - len(nextGenString))
    generationstring = nextGenString[:]
    # print('{0:3d}: {1:s} - sum {3:3d}, first: {4:2d}, index:{5:d}'.format(n,generationstring[offset:], generationstring.count('#'), potsum, first, maxi))
    diff = potsum-savedSum
    pots = generationstring.count('#')
    longRangeResult = (50000000000-1-n)*diff + potsum + diff
    resDiff = savedResult-longRangeResult
    # if n % 10 == 0:
    if n == 20:
        print('Part 1: Sum of number of all pots containing plants is:', potsum)
    if resDiff == 0:
        print('Part 2: After fifty billion (50000000000) generations:', longRangeResult)
        break
    # if n > 900:
    #     print('{0:3d}: - sum {3:3d}, sum diff: {6:3}, count: {4:2d}, index:{5:d}, pots: {2:d}, pots diff: {8:3}. Long range result: {7:d}, diff: {9:d}'.format(n,generationstring[offset:], pots, potsum, count, maxi, diff, longRangeResult, pots-numPots,resDiff))
    savedSum = potsum
    numPots = pots
    savedResult = longRangeResult
