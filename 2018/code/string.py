# Testing string handling in Python

initial = '...#..#.#..##......###...###...........'
patternstrings = [  '...## => #',
                    '..#.. => #',
                    '.#... => #',
                    '.#.#. => #',
                    '.#.## => #',
                    '.##.. => #',
                    '.#### => #',
                    '#.#.# => #',
                    '#.### => #',
                    '##.#. => #',
                    '##.## => #',
                    '###.. => #',
                    '###.# => #',
                    '####. => #']

patterns = [ p.split(' => ')[0] for p in patternstrings]
print(patterns)
generationstring = '  '+initial+'..........'
count = initial.count('#')
print('{0:2d}: {1:s}'.format(0,generationstring))
for n in range(1,21):
    nextGenString ="."*len(initial)
    length = len(generationstring)
    potsum = 0
    first = length
    for i in range(length):
        # print(generationstring[i-2:i+3], generationstring[i-2:i+3] in patterns)
        if i > 2 and i < length - 3 and generationstring[i-2:i+3] in patterns:
            nextGenString = nextGenString[:i]+'#'+nextGenString[i+1:]
            count +=1
            potsum += i-5
            if first > i: first = i

    nextGenString += '.' * (length - len(nextGenString))
    generationstring = nextGenString[:]
    print('{0:2d}: {1:s} - {2:d} pots, sum {3:d}, first: {4:d}'.format(n,generationstring, generationstring.count('#'), potsum, first))
print(count)
